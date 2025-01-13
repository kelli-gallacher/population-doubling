# Install required libraries

import pandas as pd
import math as math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

data=pd.read_csv("https://raw.githubusercontent.com/kelli-gallacher/population-doubling/refs/heads/main/SampleData.csv")

# Check that data table has imported successfully

data.head()

# Drop the zero values from the data frame

df = pd.DataFrame(data)
df = df.drop([0,1])
print(df)

# Check all data points have been imported (there should be 32 in total)

df.count()

# Rename the columns for 'seeded' and 'retrieved' to 'Ci' and 'Cf' for ease of calculation in the next step

df.columns = ['Cells', 'Treatment', 'Passage', 'Ci', 'Cf']
df.head()

# Split the data into CON and ROCKi data frames, resetting the index to start from 0. Print the new data frames to check this has been successful.

df_con = df[df['Treatment'] == 'CON'].reset_index(drop=True)
df_rocki = df[df['Treatment'] == 'ROCKi'].reset_index(drop=True)

print(df_con)
print(df_rocki)

## CALCULATING POPULATION DOUBLING LEVEL (PDL)

# Define the equation to calculate the cumulative PDL, following the equation stated in the README file

def calculate_pdl(row, prev_pdl):
    pdl = prev_pdl + 3.322 * (np.log10(row['Cf']) - np.log10(row['Ci']))
    return pdl

# Define the function to apply cumulative PDL calculations for each condition, adding new columns with these values to both CON and ROCKi data frames

def PDL_all(df_all):
    pdl_values = []
    current_pdl = 0
    
    for idx, row in df_all.iterrows():
        new_pdl = calculate_pdl(row, current_pdl)
        pdl_values.append(new_pdl)
        current_pdl = new_pdl

    df_all['Cumulative_PDL'] = pdl_values
    return df_all

# Apply this function to both data frames

PDL_con = PDL_all(df_con)
PDL_rocki = PDL_all(df_rocki)

# Combine the results for both conditions into one data frame

PDLfinal = pd.concat([PDL_con, PDL_rocki]).sort_index()

# Print the data frames

print("Calculated PDL and cumulative PDL for all conditions:")
print(PDLfinal)
print(PDL_con)
print(PDL_rocki)

# PLOTTING THE DATA

# Create a plot of the cumulative PDL for Con and ROCKi
plt.figure(figsize=(10, 6))
plt.plot(df_con['Passage'], df_con['Cumulative_PDL'], 'b-o', label='Control')
plt.plot(df_rocki['Passage'], df_rocki['Cumulative_PDL'], 'r-o', label='ROCKi')

# customise axis titles and appearance of the graph
plt.title('Control vs ROCKi', fontsize=12)
plt.xlabel('Passage Number')
plt.ylabel('Cumulative PDL')
plt.legend()
plt.grid(True)

# Save a png version of the graph
plt.savefig('cumulative_pdl_comparison.png', dpi=300, bbox_inches='tight')

# Print the plot
plt.show()

# Create a side-by-side view for the graphs
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Set the y axes to have the same maximum for comparative visualisation
y_max_rocki = PDLfinal['Cumulative_PDL'].max()

# Plot Control (CON) data
ax1.plot(df_con['Passage'], df_con['Cumulative_PDL'], 'b-o')
ax1.set_title('Control')
ax1.set_xlabel('Passage Number')
ax1.set_ylabel('Cumulative PDL')
ax1.set_ylim(0, y_max_rocki)
ax1.grid(True)

# Plot ROCKi data
ax2.plot(df_rocki['Passage'], df_rocki['Cumulative_PDL'], 'r-o')
ax2.set_title('ROCKi')
ax2.set_xlabel('Passage Number')
ax2.set_ylabel('Cumulative PDL')
ax1.set_ylim(0, y_max_rocki)
ax2.grid(True)

# Set the layout to 'tight'
plt.tight_layout()

# Save a png version of the graphs
plt.savefig('cumulative_pdl_both conditions.png', dpi=300, bbox_inches='tight')

# Print the plot
plt.show()

# ANALYSIS OF DATA


# Calculate the linear regression for each condition
slopeCON, interceptCON, r_valueCON, p_valueCON, std_errCON = stats.linregress(df_con['Passage'], df_con['Cumulative_PDL'])
slopeROCKi, interceptROCKi, r_valueROCKi, p_valueROCKi, std_errROCKi = stats.linregress(df_rocki['Passage'], df_rocki['Cumulative_PDL'])

# Print the output of this function for each condition - this will output slope, R squared value, p-value and standard error

print("Control:",
      "Slope",slopeCON, 
      "R-value:", r_valueCON, 
      "P-value:", p_valueCON,
      "Standard error:",std_errCON)
print("ROCKi:",
      "Slope:",slopeROCKi, 
      "R-value:", r_valueROCKi, 
      "P-value:", p_valueROCKi,
      "Standard error:",std_errROCKi)
print("For each passage, PDL increases by:", slopeCON, "in control cells and", slopeROCKi, "in ROCKi treated cells")

# Plot another comparison graph with the regression line

plt.figure(figsize=(10,6))
plt.scatter(df_con['Passage'], df_con['Cumulative_PDL'], color='red', label='Control')
plt.scatter(df_rocki['Passage'], df_rocki['Cumulative_PDL'], color='blue', label='ROCKi')

# Calculate y = mx + c and plot the line on the graph 
# x = passage, m = slope, c = intercept

plt.plot(df_con['Passage'], slopeCON*df_con['Passage'] + interceptCON, 'k', ls=':', label='Control fit')
plt.plot(df_rocki['Passage'],slopeROCKi*df_rocki['Passage'] + interceptROCKi, 'k', ls=':', label='ROCKi fit')

plt.xlabel('Passage')
plt.ylabel('Cumulative PDL')
plt.legend(['Control', 'ROCKi', 'Linear regression'])
plt.title('Control vs ROCKi')
plt.show()



