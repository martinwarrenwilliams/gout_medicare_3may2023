import pandas as pd
import plotly.express as px

# Load a smaller portion of the dataset
data = pd.read_csv('test_file_1.csv', nrows=9000000, encoding='ISO-8859-1')

# Filter for Allopurinol prescriptions and rheumatologists
allopurinol_data = data[(data['Gnrc_Name'] == 'Allopurinol') & (data['Prscrbr_Type'] == 'Rheumatology')]

# Group by state and aggregate the number of patients
state_counts = allopurinol_data.groupby('Prscrbr_State_Abrvtn')['Tot_Benes'].sum().reset_index()

# Create a choropleth map of the data
fig = px.choropleth(state_counts,
                    locations='Prscrbr_State_Abrvtn',
                    color='Tot_Benes',
                    color_continuous_scale='Viridis',
                    locationmode='USA-states',
                    scope='usa',
                    title='Number of Patients Prescribed Allopurinol by Rheumatologists by State',
                    labels={'Tot_Benes': 'Total Patients', 'Prscrbr_State_Abrvtn': 'State'})

fig.show()
