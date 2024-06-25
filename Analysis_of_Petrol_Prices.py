#import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv(r'D:/Semester 4/TDS/Petrol_Gas_Prices_Worldwide.csv', encoding='latin-1')

print('2022605')

#Comparing petrol prices across different countries using bar graph
# Sort the dataset by petrol prices per gallon in decending order so we can know countries with highest petrol prices
df_sorted = df.sort_values(by='Price Per Gallon (USD)', ascending=False)
# Plot the top N countries petrol prices in the list because there were too many countries and graph was becoming messy
top_n = 20     # Change the number as needed
# plot the petrol prices
plt.figure(figsize=(10, 6)) 
plt.bar(df_sorted['Country'][:top_n], df_sorted['Price Per Gallon (USD)'][:top_n], color='blue')
plt.xlabel('Countries')
plt.ylabel('Petrol Price per Gallon(USD)')
plt.title('Petrol Prices Across Countries')
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()

# Comparing petrol price after changing of currency from USD to PKR
# Filtering Pakistan because we only need Pakistan for this comparison
df_filtered = df[df['Country'].isin(['Pakistan'])]
#plot petrol price in different currencies
plt.figure(figsize=(10, 6))
plt.bar(df_filtered['Country'] + ' (PKR)', df_filtered['Price Per Liter (PKR)'], color='blue', label='Petrol Price (PKR)')
plt.bar(df_filtered['Country'] + ' (USD)', df_filtered['Price Per Liter (USD)'], color='red', label='Petrol Price (USD)')
plt.xlabel('Country')
plt.ylabel('Petrol Price')
plt.title('Petrol Prices Comparison (PKR vs USD)')
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.legend()
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()