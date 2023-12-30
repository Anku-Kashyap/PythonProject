import pyodbc
import pandas as pd

# Establish the database connection
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-GMTJHQG;DATABASE=ZONEWISE;UID=Admin;PWD=Pascal@123')
cursor = conn.cursor()

def read_excel_file(file_path):
    try:
        df = pd.read_excel(file_path, engine='openpyxl', usecols=lambda x: x != 'Time')
        return df
    except Exception as e:
        print("Error reading Excel file:", str(e))
        return None

# Path to the Excel file
file_path = "pat_MAY_12_july'.xlsx"
dataframe = read_excel_file(file_path)

if dataframe is not None:
    # Drop columns with "Unnamed" values
    unnamed_columns = [col for col in dataframe.columns if 'Unnamed' in col]
    dataframe = dataframe.drop(unnamed_columns, axis=1)
    # Convert the "Power_On_Hours" column to string



    # Exclude rows with NaN values
    dataframe = dataframe.dropna()

    # Convert DataFrame to list of tuples
    data_list = [tuple(row) for row in dataframe.itertuples(index=False)]

    # Insert the DataFrame into the SQL Server table
    for row in data_list:
        cursor.execute(
                "INSERT INTO data(Division, Station, Date_time, Date, mode, Staus, Volts_R_Y, Volts_Y_B, Volts_B_R, Amp_R, Amp_Y, Amp_B, HZ, Power_factor, Power_KW, Energry_KWH, Pump_Discharge_m3_h, Pump_Total_Discharge_m3_day, OTH_Discharge_m3_h, OTH_Total_Discharge_m3_day, OTH_Level_m, Run_Hours, Power_On_Hours, Presure_kg_cm2,Chlorine) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?)",
            *row)
        # ...

    # Commit the changes to the database
    conn.commit()
    print('Completed')
    # Print the DataFrame
    if not dataframe.empty:
        pass
        print(dataframe.to_string(index=True))
    else:
        print("DataFrame is empty")
