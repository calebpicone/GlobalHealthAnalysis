
# Global Health Statistics Dataset Analysis with Pandas & PandasGUI

Caleb Picone

For my first project in data analysis, I decided to use a global health dataset found on Kaggle, which the full dataset can be found here https://www.kaggle.com/datasets/malaiarasugraj/global-health-statistics/data. Due to its large size, I decided it would be more manageable to narrow down the data analysis to just the CSV entries for the USA from 2020 to 2024. 


## The Dataset

The dataset used for this project provides insight on various diseases outbreaking in various countries throughout time. Due to its large amount of entries, Pandas was used to narrow down the dataset and create a new CSV with only entries for the USA from 2020 to 2024, shown in the code here:

```
# Load the full dataset into a df
df = pd.read_csv('Global_Health_Statistics_Full_Dataset.csv')

# Filter the rows only showing data for the USA
df_usa = df[df['Country'] == 'USA'] 

# Convert the 'Year' column to numeric 
df_usa['Year'] = pd.to_numeric(df_usa['Year'], errors='coerce')

# Filter the rows only showing data from 2014 - 2024
df_usa_filtered = df_usa[(df_usa['Year'] >= 2020) & (df_usa['Year'] <= 2024)]

# Save the filtered data to a new CSV file
df_usa_filtered.to_csv('USA_Health_Data_2020_2024.csv', index=False)
```

Using the subset of USA data, these are some questions that this project aims to answer:

1. Which diseases are most prevelant in the dataset?
2. Which diseases have the highest mortality rates?
2. Are there any correlations in the mortality rates of each disease throughout the provided years?
3. Are there any correlations to the mortality rates of the provided years and healtcare access?
4. Are there any correlations between male mortality rates?
5. Are there any correlations between female mortality rates?
6. Are there any correlations between other gender mortality rates?


## Dataset Description

Firstly, it's important to clean up the CSV dataset. This was done with the following Python code using Pandas:

```
# Count null values
print(df.isnull().sum())

# Drop rows with missing values
df = df.dropna()

# Drop columns with missing values
df = df.dropna(axis = 1)

# Remove duplicate rows
df = df.drop_duplicates()

# Row and column counting
num_rows, num_columns = df.shape
print(f'# of rows: {num_rows}')
print(f'# of columns: {num_columns}')
```

Fortunately, the CSV had no null values that needed to be cleaned or converted, so before and after clean up the 'USA_Health_Data_2020_2024.csv' has 22 columns and 10,035 rows. 

![USa_Health_Data_2020_2024_Columns](https://github.com/user-attachments/assets/7a1ce4d7-b57a-4d51-b904-37dde60a225f)

# Answering the Project Questions

After narrowing down the data from the original dataset, and cleaning the subset of data, it's time to find the answers to the questions mentioned above.

## 1. Which diseases are most prevelant in the dataset?
