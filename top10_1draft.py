import pandas as pd

# Load the entire dataset
data = pd.read_csv('test_file_1.csv', encoding='ISO-8859-1')

# Filter for rheumatologists
rheumatologist_data = data[data['Prscrbr_Type'] == 'Rheumatology']

# Calculate the total number of patients for each rheumatologist
total_patients = rheumatologist_data.groupby('Prscrbr_NPI')['Tot_Benes'].sum().reset_index()
total_patients.columns = ['Prscrbr_NPI', 'Total_Patients']

# Filter for Allopurinol prescriptions
allopurinol_data = rheumatologist_data[rheumatologist_data['Gnrc_Name'] == 'Allopurinol']

# Group by rheumatologist and aggregate the number of patients
allopurinol_counts = allopurinol_data.groupby('Prscrbr_NPI')['Tot_Benes'].sum().reset_index()

# Merge the data with total patients data
allopurinol_data = allopurinol_counts.merge(total_patients, on='Prscrbr_NPI')

# Calculate the percentage of patients receiving Allopurinol
allopurinol_data['Percentage'] = allopurinol_data['Tot_Benes'] / allopurinol_data['Total_Patients'] * 100

# Sort the data by percentage, descending
allopurinol_data = allopurinol_data.sort_values(by='Percentage', ascending=False)

# Display the top 5000 rheumatologists
pd.set_option('display.max_rows', 5000)
print(allopurinol_data.head(5000))
