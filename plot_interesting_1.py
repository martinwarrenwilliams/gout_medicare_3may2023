import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('test_file_1.csv', encoding='ISO-8859-1')

# Filter data for allopurinol and colchicine
df_gout = df[df['Gnrc_Name'].isin(['ALLOPURINOL', 'COLCHICINE'])]

# Generate charts and graphs
fig1 = px.bar(df_gout, x='Gnrc_Name', y='Tot_Clms', color='Gnrc_Name', 
              title='Number of Medicare Part D claims for gout medications')
fig2 = px.bar(df_gout, x='Gnrc_Name', y='Tot_30day_Fills', color='Gnrc_Name', 
              title='Number of standardized 30-day fills for gout medications')
fig3 = px.bar(df_gout, x='Gnrc_Name', y='Tot_Day_Suply', color='Gnrc_Name', 
              title='Number of days of supply for gout medications')
fig4 = px.bar(df_gout, x='Gnrc_Name', y='Tot_Drug_Cst', color='Gnrc_Name', 
              title='Total drug cost for gout medications')

# Prescribing behavior of physicians
df_phys = df_gout[['Prscrbr_NPI', 'Prscrbr_Last_Org_Name', 'Prscrbr_First_Name', 
                   'Prscrbr_City', 'Prscrbr_State_Abrvtn', 'Prscrbr_Type']]
num_prescribers = len(df_phys['Prscrbr_NPI'].unique())
fig5 = px.bar(df_phys, x='Prscrbr_State_Abrvtn', color='Prscrbr_Type', 
              title=f'Distribution of {num_prescribers} prescribers of gout medications by state and specialty')

# Top prescribers of gout medications
top_prescribers = df_gout.groupby(['Prscrbr_Last_Org_Name', 'Prscrbr_First_Name']).sum()
top_prescribers = top_prescribers.sort_values('Tot_Clms', ascending=False).reset_index()[:10]
fig6 = px.bar(top_prescribers, x='Prscrbr_Last_Org_Name', y='Tot_Clms', 
              title='Top 10 prescribers of gout medications')

# Additional ideas for generating insights
# fig7 = px.bar(df_phys, x='Prscrbr_State_Abrvtn', color='Prscrbr_Type', facet_col='Is_Rural', 
#              title='Distribution of prescribers of gout medications by state, specialty, and rural/urban location')
# fig8 = px.histogram(df_gout, x='Tot_Benes', nbins=50, 
#                    title='Distribution of Medicare beneficiaries by number of gout medication claims')
# fig9 = px.line(df_gout, x='Year', y='Tot_Clms', color='Gnrc_Name', 
#               title='Trends in Medicare Part D claims for gout medications')
# fig10 = px.line(df_gout, x='Year', y='Tot_Drug_Cst', color='Gnrc_Name', 
#                title='Trends in total drug cost for gout medications')

# Show the charts and graphs
fig1.show()
fig2.show()
fig3.show()
fig4.show()
fig5.show()
fig6.show()
#fig7.show()
#fig8.show()
#fig9.show()
#fig10.show()
