
input_directory = "C:/Users/Lenovo/Desktop/KM Pressure Data June 22-Feb 23/KM Zone 3 PT 2 Data"
output_file = "C:/Users/Lenovo/Desktop/KM Pressure Data June 22-Feb 23/KM Zone 3 PT 2 Data/3.xlsx"
sheet_name = "Sheet1"


import os
import pandas as pd


sheet_name = "Sheet1"


# Get a list of all Excel files in the input directory
excel_files = [f for f in os.listdir(input_directory) if f.endswith('.xlsx')]

# Create an empty DataFrame to store the combined data
combined_data = pd.DataFrame()

# Loop through each Excel file and read the data into the combined DataFrame
for file in excel_files:
    file_path = os.path.join(input_directory, file)
    df = pd.read_excel(file_path, engine='openpyxl')
    combined_data = combined_data.append(df, ignore_index=True)

# Write the combined data to a new Excel file
combined_data.to_excel(output_file, sheet_name=sheet_name, index=False, engine='openpyxl')
