# Population Doubling Level (PDL) Calculator

## **&#128218; Table of Contents**

- [About](https://github.com/kelli-gallacher/population-doubling/tree/main?tab=readme-ov-file#-about)
- [Installation](https://github.com/kelli-gallacher/population-doubling/tree/main?tab=readme-ov-file#-installation)
-  [Output](https://github.com/kelli-gallacher/population-doubling/tree/main?tab=readme-ov-file#-about)


## &#128300; About 

This script is designed to calculate the population doubling level (**PDL**) from cell culture experiments with multiple conditions.

The [sample data](https://raw.githubusercontent.com/kelli-gallacher/population-doubling/refs/heads/main/SampleData.csv) is taken from an experiment using a human keratinocyte cell line.

## &#128187; Installation

In order for this script to work, the following packages are required:
|Library |URL  |
|--|--|
|Pandas| https://pandas.pydata.org/
|NumPy| https://numpy.org/
|Math|https://docs.python.org/3/library/math.html|
|Seaborn  |  https://seaborn.pydata.org/index.html#|
|MatPlot (PyPlot)|  https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html|
|SciPy (Stats) | https://docs.scipy.org/doc/scipy/reference/stats.html |
|  |  |

The script should automatically import these libraries upon running. The code is also provided below if there are any issues:

    import pandas as pd
    import math as math
    import numpy as np
    import seaborn as sns
    import matplotlib.pyploy as plt
    from scipy import stats
    
## &#128200; Output
After successful running of the script, you should see the following output:

**A graph with both conditions**

![An x y plot of passage number against cumulative PDL for control and ROCKi treated cells](https://i.ibb.co/g7KLdWM/cumulative-pdl-comparison.png)

**Individual graphs for each condition**

![Separate x y plots of passage number against cumulative PDL for control and ROCKi treated cells](https://i.ibb.co/LPRG5hm/cumulative-pdl-both-conditions.png)

**A graph with both conditions and a fitted linear regression line**
![An x y plot of passage number against cumulative PDL for control and ROCKi treated cells, with a dotted line showing the linear regression for each condition](https://i.ibb.co/rMSYxmf/regression-cumulative-pdl-both-conditions.png)
