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
file_path = "Copy of NW Zone 1 PT 2 Dec Jan 23(1).xlsx"

dataframe = read_excel_file(file_path)
# ...

if dataframe is not None:
    # Drop columns with "Unnamed" values
    unnamed_columns = [col for col in dataframe.columns if 'Unnamed' in col]
    dataframe = dataframe.drop(unnamed_columns, axis=1)

    # Convert the "Power_On_Hours" column to string


    # Exclude rows with NaN values
    dataframe = dataframe.dropna()

    # Convert DataFrame to list of tuples
    data_list = [tuple(row) for row in dataframe.itertuples(index=False)]
    print(dataframe)
    print(data_list)

    # Insert the DataFrame into the SQL Server table
    # ...
    for index, row in dataframe.iterrows():
        cursor.execute(
            "INSERT INTO Pt_Data(Division, Date, Station, Date_time, Pressure) "
            "VALUES (?, ?, ?, ?, ?)",
                row['Division'], row['Date'], row['Station'], row['Date_time'], float(row['Pressure']))
    # ...

    # Commit the changes to the database
    conn.commit()
    print('Done')
