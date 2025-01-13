<p align="center"><img src="https://i.ibb.co/2nsppDF/PDL-header.png"></align>

## **&#128218; Table of Contents**

- [About](#-about)
- [Before you run](#-installation)
- [Output](#-about)
- [Acknowledgements](#acknowledgements)
- [Options](#addtional-options)


## &#128300; About 

This script is designed to be a speedy tool to calculate the population doubling level (**PDL**) from cell culture experiments with **two** conditions. In addition to calculation, the script will also generate graphs and perform regression analysis.

The [sample data](https://raw.githubusercontent.com/kelli-gallacher/population-doubling/refs/heads/main/SampleData.csv) is taken from an experiment using a human keratinocyte cell line (referred to as 'MEM' in the data). The two conditions the cells were grown in are control ('CON') and with a Rho-kinase inhibitor ('ROCKi'). 

The number of cells retrieved and seeded was recorded every week. These values can be used to calculate the PDL, using the below equation:

> **PDL = PDL<sub>0</sub> + 3.22 * (log<sub>Cf</sub> - log<sub>Ci</sub>)**
> 
**PDL** initial population doubling level
**C<sub>i</sub>** Initial cell number seeded
**C<sub>f</sub>** Number of cells retrieved

If you are interested, this [article](https://www.roosterbio.com/blog/best-practices-in-msc-culture-tracking-and-reporting-cellular-age-using-population-doubling-level-pdl-and-not-passage-number/) provides a more in-depth overview of PDL.

## &#128187; Before you run

**1**. Please ensure that you have downloaded [SampleData.csv](https://raw.githubusercontent.com/kelli-gallacher/populationdoubling/refs/heads/main/SampleData.csv%29) and PDLCalc.py, which should be saved in your working directory.

**2**. In order for this script to work, the following packages are    required:

|Library |URL  |
|--|--|
|Pandas| https://pandas.pydata.org/
|NumPy| https://numpy.org/
|Math|https://docs.python.org/3/library/math.html|
|MatPlot (PyPlot)|  https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html|
|SciPy (Stats) | https://docs.scipy.org/doc/scipy/reference/stats.html |

The script should automatically import these libraries upon running. The code is also provided below if there are any issues:

    import pandas as pd
    import math as math
    import numpy as np
    import seaborn as sns
    import matplotlib.pyploy as plt
    from scipy import stats
    



**3**. Run the pipeline with **SampleData.csv.**

**4**.  If you would like to use **your own data**, please ensure that you have only **two** conditions and use the column headers:
 - Cells
 - Treatment
 - Seeded
 - Retrieved

## &#128200; Output
After successful running of the script, you should see the following output. All images will be saved to your working directory. 

See [Options](#addtional-options) for customisation of appearance and file name(s).

**1. A graph comparing the cumulative PDL for both conditions**

![An x y plot of passage number against cumulative PDL for control and ROCKi treated cells](https://i.ibb.co/g7KLdWM/cumulative-pdl-comparison.png)

**2. Individual graphs of the cumulative PDL for each condition**

![Separate x y plots of passage number against cumulative PDL for control and ROCKi treated cells](https://i.ibb.co/LPRG5hm/cumulative-pdl-both-conditions.png)

**3. A text readout of the the regression analysis for both conditions**

![White text on a black background with a text readout of the regression analysis for both conditions](https://i.ibb.co/BcR718Y/Regression-Read-Our.png)

**4.  A graph comparing the cumulative PDL in both conditions with a fitted linear regression line**

![An x y plot of passage number against cumulative PDL for control and ROCKi treated cells, with a dotted line showing the linear regression for each condition](https://i.ibb.co/rMSYxmf/regression-cumulative-pdl-both-conditions.png)


## &#127912; Addtional options

 - You can amend the file name(s) and type when saving the images of graphs by amending the code below:

```plt.savefig('INSERTFILENAMEHERE.filetype', dpi=300, bbox_inches='tight')```

 - The appearance of the graph can also be changed to your preference using the marker, line and colour options included with [MatPlotLib](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html) 


## &#129309;&#127995;Acknowledgements

 - The PDL calculation used in this script is from [RoosterBio](https://www.roosterbio.com/blog/what-is-population-doubling-level-pdl-why-is-it-important-for-cell-age/).
 - The sample data was produced by the author (Kelli Gallacher) and she has given permission for its use.


