import pandas as pd
import plotly.subplots as sp
import plotly.graph_objs as go

# Load the entire dataset
data = pd.read_csv('test_file_1.csv', encoding='ISO-8859-1')

# Hardcoded state population data
state_population_data = {
    'AL': 4903185, 'AK': 731545, 'AZ': 7278717, 'AR': 3017804, 'CA': 39538223,
    'CO': 5758736, 'CT': 3565287, 'DE': 989948, 'FL': 21538187, 'GA': 10711908,
    'HI': 1455271, 'ID': 1839106, 'IL': 12812508, 'IN': 6785528, 'IA': 3190369,
    'KS': 2937880, 'KY': 4505836, 'LA': 4657757, 'ME': 1362359, 'MD': 6177224,
    'MA': 7029917, 'MI': 10077331, 'MN': 5706494, 'MS': 2966786, 'MO': 6160281,
    'MT': 1084225, 'NE': 1961504, 'NV': 3104614, 'NH': 1377529, 'NJ': 9288994,
    'NM': 2117522, 'NY': 20111634, 'NC': 10488084, 'ND': 779094, 'OH': 11799448,
    'OK': 3963516, 'OR': 4237256, 'PA': 13002700, 'RI': 1097379, 'SC': 5118425,
    'SD': 886667, 'TN': 6916897, 'TX': 29145505, 'UT': 3271616, 'VT': 643077,
    'VA': 8631393, 'WA': 7693612, 'WV': 1793716, 'WI': 5832655, 'WY': 577719
}

state_population = pd.DataFrame(list(state_population_data.items()), columns=['Prscrbr_State_Abrvtn', 'Population'])

# Filter for Allopurinol prescriptions and rheumatologists
allopurinol_data = data[(data['Gnrc_Name'] == 'Allopurinol') & (data['Prscrbr_Type'] == 'Rheumatology')]

# Filter for Colchicine prescriptions and rheumatologists
colchicine_data = data[(data['Gnrc_Name'] == 'Colchicine') & (data['Prscrbr_Type'] == 'Rheumatology')]

# Group by state and aggregate the number of patients for Allopurinol
allopurinol_state_counts = allopurinol_data.groupby('Prscrbr_State_Abrvtn')['Tot_Benes'].sum().reset_index()

# Group by state and aggregate the number of patients for Colchicine
colchicine_state_counts = colchicine_data.groupby('Prscrbr_State_Abrvtn')['Tot_Benes'].sum().reset_index()

# Merge the data with state population data
allopurinol_state_counts = allopurinol_state_counts.merge(state_population, on='Prscrbr_State_Abrvtn')
colchicine_state_counts = colchicine_state_counts.merge(state_population, on='Prscrbr_State_Abrvtn')

# Calculate the prevalence ratio for Allopurinol and Colchicine
allopurinol_state_counts['Prevalence_Ratio'] = allopurinol_state_counts['Tot_Benes'] / allopurinol_state_counts['Population']
colchicine_state_counts['Prevalence_Ratio'] = colchicine_state_counts['Tot_Benes'] / colchicine_state_counts['Population']

# Create a subplot with shared x-axis
fig = sp.make_subplots(rows=1, cols=2, subplot_titles=("Allopurinol Prescriptions", "Colchicine Prescriptions"))

# Create the Allopurinol map
allopurinol_map = go.Choropleth(
    locations=allopurinol_state_counts['Prscrbr_State_Abrvtn'],
    z=allopurinol_state_counts['Prevalence_Ratio'],
    color_continuous_scale='Viridis',
    locationmode='USA-states',
    text=allopurinol_state_counts['Prscrbr_State_Abrvtn'],
    showscale=False
)

# Create the Colchicine map
colchicine_map = go.Choropleth(
    locations=colchicine_state_counts['Prscrbr_State_Abrvtn'],
    z=colchicine_state_counts['Prevalence_Ratio'],
    color_continuous_scale='Viridis',
    locationmode='USA-states',
    text=colchicine_state_counts['Prscrbr_State_Abrvtn'],
    showscale=False
)


# Add the Allopurinol map to the subplot
fig.add_trace(allopurinol_map, row=1, col=1)

# Add the Colchicine map to the subplot
fig.add_trace(colchicine_map, row=1, col=2)

# Update layout settings
fig.update_layout(
    title_text='Prevalence Ratio of Patients Prescribed Allopurinol and Colchicine by Rheumatologists by State',
    geo=dict(scope='usa', projection_type='albers usa', showlakes=True, lakecolor='rgb(255, 255, 255)'),
    geo2=dict(scope='usa', projection_type='albers usa', showlakes=True, lakecolor='rgb(255, 255, 255)'),
    legend=dict(x=0.5, y=-0.1, bgcolor='rgba(255, 255, 255, 0.5)', bordercolor='rgba(0, 0, 0, 0.5)'),
    margin=dict(r=10, t=25, b=40, l=60)
)

fig.show()

