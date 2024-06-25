#import library
import pandas as pd

print('2022605')

# Define column names because name of first column was missing 
column_names = ['Location', 'Year', 'Total number of accidents', 'Fatal accidents', 'Non-fatal accidents', 'Killed', 'Injured', 'Vehicles involved']

# Read the CSV file, skipping the first 3 rows because they were unnecessary and creating problems, and using the defined column names
df = pd.read_csv(r'D:/Semester 4/TDS/Pakistani_Traffic_Accidents.csv', skiprows=3, names=column_names)

# Filtering out rows not containing "pakistan" in the specified column 'Location' because it was not needed in province trends
filtered_data = df[~df['Location'].str.contains("pakistan", case=False)]


# Grouping by 'Location' and calculating the sum of accidents
grouped_data = filtered_data.groupby('Location')['Total number of accidents'].sum()

# Sorting the grouped DataFrame of 'Total number of accidents' in descending order
sorted_data = grouped_data.sort_values(ascending=False)
#Getting only top row
top_rows = sorted_data.head(1)
print('Province with most accidents is')
print(top_rows)

# Sorting the grouped DataFrame of 'Total number of accidents' in ascending order
sorted_data1 = grouped_data.sort_values(ascending=True)
#Getting only top row
top_rows1 = sorted_data1.head(1)
print('Province with least accidents is')
print(top_rows1)

#Grouping by 'Location' and calculating total number of kills
grouped_data1 = filtered_data.groupby('Location')['Killed'].sum()

# Sorting the grouped DataFrame of number of kills in descending order
sorted_data2 = grouped_data1.sort_values(ascending=False)
#Getting only top row
top_rows2 = sorted_data2.head(1)
print('Province with most kills is')
print(top_rows2)

# Sorting the grouped DataFrame of number of kills in ascending order
sorted_data3 = grouped_data1.sort_values(ascending=True)
#Getting only top row
top_rows3 = sorted_data3.head(1)
print('Province with least kills is')
print(top_rows3)

#Grouping by 'Location' and calculating total number of injuries
grouped_data2 = filtered_data.groupby('Location')['Injured'].sum()

# Sorting the grouped DataFrame of number of injuries in descending order
sorted_data4 = grouped_data2.sort_values(ascending=False)
#Getting only top row
top_rows4 = sorted_data4.head(1)
print('Province with most injuries is')
print(top_rows4)

# Sorting the grouped DataFrame of number of injuries in ascending order
sorted_data5 = grouped_data2.sort_values(ascending=True)
#Getting only top row
top_rows5 = sorted_data5.head(1)
print('Province with least injuries is')
print(top_rows5)

# Filtering out rows containing "pakistan" in the specified column 'Location' because only it was needed in this trends
filtered_data1 = df[df['Location'].str.contains("pakistan", case=False, regex=False)]

#Grouping by 'Year' and calculating total number of accidents
grouped_data3 = filtered_data1.groupby('Year')['Total number of accidents'].sum()

# Sorting the grouped DataFrame of 'Total number of accidents' in descending order
sorted_data6 = grouped_data3.sort_values(ascending=False)
#Getting only top row
top_rows6 = sorted_data6.head(1)
print('Year with most accidents is')
print(top_rows6)

# Sorting the grouped DataFrame of 'Total number of accidents' in ascending order
sorted_data7 = grouped_data3.sort_values(ascending=True)
#Getting only top row
top_rows7 = sorted_data7.head(1)
print('Year with least accidents is')
print(top_rows7)