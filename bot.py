import pandas as pd

# Provide the correct path to the CSV file as a string
file_path = "/kaggle/input/total-number-of-prisoners-in-malaysia/Number_of_Prisoners_by_Gender_by_State_2016-2019.csv"

# Read the CSV file into a DataFrame
data = pd.read_csv(file_path)

# Now you can work with the 'data' DataFrame as needed.
data.head(10)

import pandas as pd
import plotly.express as px

# Create a dictionary from the provided data
data = {
    'State': ['Perlis', 'Kedah', 'Pulau Pinang', 'Perak', 'Selangor', 'Negeri Sembilan',
              'Melaka', 'Johor', 'Kelantan', 'Terengganu', 'Pahang', 'Sabah', 'Sarawak'],
    '2016': [1212, 7669, 7596, 8605, 34944, 4497, 6045, 11065, 7284, 4728, 8529, 14783, 3840],
    '2017': [1223, 7045, 8324, 8565, 37862, 5115, 6000, 11589, 7066, 4676, 7317, 12205, 4284],
    '2018': [1592, 6975, 7951, 7362, 34903, 4086, 5744, 11898, 7006, 4963, 7555, 13210, 3845],
    '2019': [1893, 7505, 10050, 9882, 40882, 4828, 7279, 14297, 7330, 5123, 7847, 15695, 5433]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Reshape the data using pd.melt()
df_long = pd.melt(df, id_vars=['State'], var_name='Year', value_name='Number of Prisoners')

# Convert 'Year' column to datetime for proper sorting
df_long['Year'] = pd.to_datetime(df_long['Year'], format='%Y')

# Create the pie chart using Plotly
fig = px.pie(df_long[df_long['Year'] == '2019'], values='Number of Prisoners', names='State', title='Population Distribution in 2019')

# Convert 'Year' column back to string representation
df_long['Year'] = df_long['Year'].dt.year.astype(str)

# Create a stacked bar chart using Plotly to show the distribution of prisoners by state for each year
fig_bar = px.bar(df_long, x='State', y='Number of Prisoners', color='Year',
             title='Distribution of Total Number of Prisoners by State and Year')

# Create a line chart using Plotly to show the trend of total number of prisoners in Malaysia by year
fig_line = px.line(df_long, x='Year', y='Number of Prisoners', color='State',
              title='Trend of Total Number of Prisoners in Malaysia by State')

# Display both the bar chart and the line chart
fig.show()
fig_bar.show()
fig_line.show()
