# Global Health Analysis
A project where I used Pandas, PandasGUI, and SciPy to conduct statistical analyses on a global health dataset found on Kaggle
PROJECT: Analyzing Mortality Rates of Various Countries

OBJECTIVE: To investigate the relationship between income per capita and mortality rates across countries, and to explore the finding that there may be no significant correlation between these two factors. This lack of correlation could suggest that other factors, beyond just income, play a critical role in determining a country’s health outcomes.

TOOLS: Python, Pandas, PandasGUI, NumPy, SciPy, Kaggle, VSCode

DATASET: https://www.kaggle.com/datasets/malaiarasugraj/global-health-statistics (NOTE: The CSV is not uploaded to the GitHub due to its large size. In order to access it, you'll have to use the URL here to get to the Kaggle page.)

STEPS:

1) The first step was to compare Mortality Rates (%) to Income Per Capita (%). Using PandasGUI, a scatterplot was made by using a subset DataFrame of the first 300 entries in the CSV file. The scatterplot appeared to show no correlation between the two variables.
In order to determine correlation, a few arithmetic calculations were conducted using SciPy. 
The first of which was Pearson’s correlation coefficient. Calculating the Pearson’s correlation coefficient from the main df gave a result of r = -0.00 with p-value of 0.1327.
The second calculation was a logarithmic transformation on the Income Per Capita (%) variable. This gave a result of r = -0.00 with a p-value of 0.3543. 
The third calculation was a Spearman’s rank correlation (rho). This gave a result of r = -0.00 with a p-value of 0.1329.
The fourth calculation was a Kendall’s Tau correlation (tau). This gave a result of r = -0.00 with a p-value of 0.1328.

Takeaway: As you can see from the calculations above, the correlation between Mortality Rates (%) and Income Per Capita (%) is practically nonexistent. There is no linear, logarithmic, or exponential correlation between the two valuables. Thus, it was probable to look into other factors which may have affected mortality rates. The next step was to look into the variable Healthcare Access (%).

2) Similar to before, four calculations were done to compare Mortality Rates (%) to Healthcare Access (%). The results are below:
The first of which was Pearson’s correlation coefficient. This gave a result of r = 0.00 with p-value of 0.9385.
The second calculation was a logarithmic transformation. This gave a result of r = 0.00 with a p-value of 0.9873. 
The third calculation was a Spearman’s rank correlation (rho). This gave a result of r = 0.00 with a p-value of 0.9383.
The fourth calculation was a Kendall’s Tau correlation (tau). This gave a result of r = -0.00 with a p-value of 0.9385.

Takeaway: Similar to the previous comparison in Step 1, the calculations of correlation between Mortality Rates (%) and Healthcare Access (%) show practically no relationship between the two variables.
