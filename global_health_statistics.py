import pandas as pd
import numpy as np
import scipy.stats as stats
import pandasgui as pdgui
from pandasgui import show

df = pd.read_csv('global_health_statistics.csv')

# Organize and display data
print(df.head(n=22))
print(df.info())
print(df.describe()) 

# Data subset for easier graphing
# Due to the large amount of data in the dataset, narrowing it down to the first 300 
# entries will help with creating graphs via PandasGUI. However, when doing the statistical
# analyses, the full dataset was used
subset_df = df.head(300)

# DATA VISUALIZATION USING PANDASGUI
show(subset_df) # Use the subset_df since the main df is too dense to graph

## INCOME PER CAPITA COMPARISONS AND ANALYSES

# Pearson's Correlation Coefficient for main df
r, p_value = stats.pearsonr(df['Per Capita Income (USD)'], df['Mortality Rate (%)'])
print(f'Correlation coefficient (r): {r:.2f}')
print(f'P-value: {p_value:.4f}')

# Log transformation
df['log_income'] = np.log10(df['Per Capita Income (USD)'])
r, p_value = stats.pearsonr(df['log_income'], df['Mortality Rate (%)'])
print(f'Log Transformation Correlation coefficient (r): {r:.2f}')
print(f'P-value: {p_value:.4f}')

# Spearman's rank correlation
rho, p_value_spearman = stats.spearmanr(df['Per Capita Income (USD)'], df['Mortality Rate (%)'])
print(f'Spearman rank correlation (rho): {rho:.2f}')
print(f'P-value: {p_value_spearman:.4f}')

# # Kendall's tau correlation
tau, p_value_kendall = stats.kendalltau(df['Per Capita Income (USD)'], df['Mortality Rate (%)'])
print(f'Kendall Tau correlation (tau): {tau:.2f}')
print(f'P-value: {p_value_kendall:.4f}')

## HEALTHCARE ACCESS COMPARISONS AND ANALYSES

# # Pearson's Correlation Coefficient for main df
r_healthcare, p_value_healthcare = stats.pearsonr(df['Healthcare Access (%)'], df['Mortality Rate (%)'])
print(f'Correlation coefficient (r): {r_healthcare:.2f}')
print(f'P-value: {p_value_healthcare:.4f}')

# # Log transformation
df['log_healthcare'] = np.log10(df['Healthcare Access (%)'])
r_healthcare, p_value_healthcare = stats.pearsonr(df['log_healthcare'], df['Mortality Rate (%)'])
print(f'Log Transformation Correlation coefficient (r): {r_healthcare:.2f}')
print(f'P-value: {p_value_healthcare:.4f}')

# # Spearman's rank correlation
rho_healthcare, p_value_spearman_healthcare = stats.spearmanr(df['Healthcare Access (%)'], df['Mortality Rate (%)'])
print(f'Spearman rank correlation (rho): {rho_healthcare:.2f}')
print(f'P-value: {p_value_spearman_healthcare:.4f}')

# # Kendall's tau correlation
tau_healthcare, p_value_kendall_healthcare = stats.kendalltau(df['Healthcare Access (%)'], df['Mortality Rate (%)'])
print(f'Kendall Tau correlation (tau): {tau_healthcare:.2f}')
print(f'P-value: {p_value_kendall_healthcare:.4f}')
