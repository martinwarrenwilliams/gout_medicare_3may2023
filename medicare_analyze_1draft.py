import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load the dataset (assuming it's a CSV file)
data = pd.read_csv('test_file_1.csv')

# Filter the dataset for Allopurinol prescriptions and rheumatologists
allopurinol_data = data[(data['Gnrc_Name'] == 'Allopurinol') & (data['Prscrbr_Type'] == 'Rheumatology')]

# Group data by state and count the number of prescriptions
state_counts = allopurinol_data.groupby('Prscrbr_State_Abrvtn')['Tot_Clms'].sum().reset_index()

# Load US shapefile data
us_shapefile = gpd.read_file('https://eric.clst.org/assets/wiki/uploads/Stuff/gz_2010_us_040_00_5m.json')

# Merge the state_counts dataframe with the US shapefile data
merged_data = us_shapefile.set_index('STUSPS').join(state_counts.set_index('Prscrbr_State_Abrvtn'))

# Plot the choropleth map
fig, ax = plt.subplots(1, figsize=(20, 10))
merged_data.plot(column='Tot_Clms', cmap='coolwarm', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
ax.axis('off')
ax.set_title('Prevalence of Allopurinol Prescriptions by Rheumatologists in the US', fontdict={'fontsize': '20', 'fontweight': '3'})
plt.show()
