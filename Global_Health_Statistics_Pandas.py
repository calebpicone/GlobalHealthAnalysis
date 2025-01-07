import pandas as pd  # type: ignore
import pandasgui as pdgui
from pandasgui import show

# # Load the full dataset into a df
df = pd.read_csv('Global_Health_Statistics_Full_Dataset.csv')

# # Filter the rows only showing data for the USA
df_usa = df[df['Country'] == 'USA'] 

# # Convert the 'Year' column to numeric 
df_usa['Year'] = pd.to_numeric(df_usa['Year'], errors='coerce')

# # Filter the rows only showing data from 2014 - 2024
df_usa_filtered = df_usa[(df_usa['Year'] >= 2020) & (df_usa['Year'] <= 2024)]

# # Save the filtered data to a new CSV file
df_usa_filtered.to_csv('USA_Health_Data_2020_2024.csv', index=False)

##PANDAS##

df = pd.read_csv('USA_Health_Data_2020_2024.csv')


## CSV CLEANUP

# # Count null values
print(df.isnull().sum())

# # Drop rows with missing values
df = df.dropna()

# # Drop columns with missing values
df = df.dropna(axis = 1)

# # Remove duplicate rows
df = df.drop_duplicates()

# # Row and column counting
num_rows, num_columns = df.shape
print(f'# of rows: {num_rows}')
print(f'# of columns: {num_columns}')

##PANDASGUI 
show(df)
