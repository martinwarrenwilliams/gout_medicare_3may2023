import pandas as pd
import plotly.express as px

# Replace 'medicare_data.csv' with the actual file name
data_file = 'test_file_1.csv'
df = pd.read_csv('test_file_1.csv', encoding='ISO-8859-1')

gout_meds = ['Allopurinol', 'Colchicine']
gout_df = df[df['Gnrc_Name'].isin(gout_meds)]

# Group the data by state
state_group = gout_df.groupby('Prscrbr_State_Abrvtn')

# Calculate the gout specialization index
state_gout_index = (state_group['Tot_Clms'].sum() / df.groupby('Prscrbr_State_Abrvtn')['Tot_Clms'].sum()) * 100

# Create a DataFrame with the gout specialization index by state
state_gout_index_df = pd.DataFrame(state_gout_index).reset_index()
state_gout_index_df.columns = ['State', 'Gout_Specialization_Index']

print(gout_df.head())
print(state_group['Tot_Clms'].sum())
print(df.groupby('Prscrbr_State_Abrvtn')['Tot_Clms'].sum())
print(state_gout_index)


# Plot the US map
fig = px.choropleth(state_gout_index_df, locations='State',
                    locationmode='USA-states',
                    color='Gout_Specialization_Index',
                    color_continuous_scale='Viridis',
                    scope='usa',
                    title='Gout Specialization Index by State')

fig.show()
