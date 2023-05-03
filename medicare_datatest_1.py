import pandas as pd
from tqdm import tqdm

# Load the dataset in chunks
chunksize = 10 ** 5
chunks = []
progress_bar = tqdm(pd.read_csv('test_file_1.csv', chunksize=chunksize), total=20_000_000 // chunksize, unit='chunk')

for chunk in progress_bar:
    # Filter the dataset for Allopurinol prescriptions and rheumatologists
    allopurinol_data = chunk[(chunk['Gnrc_Name'] == 'Allopurinol') & (chunk['Prscrbr_Type'] == 'Rheumatology')]
    
    # If at least one rheumatologist is found, print their name and exit the loop
    if not allopurinol_data.empty:
        rheumatologist = allopurinol_data.iloc[0]
        print(f"Rheumatologist who prescribes Allopurinol: {rheumatologist['Prscrbr_First_Name']} {rheumatologist['Prscrbr_Last_Org_Name']}")
        break

    progress_bar.update(1)

progress_bar.close()
