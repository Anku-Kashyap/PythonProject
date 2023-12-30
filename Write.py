
import json
import csv
import random
import datetime
import time
print(datetime.date.today())
# Open the CSV file for reading
with open('DATA.csv', 'r') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)

    # Read the header row to get the column names
    header = next(reader)

    # Find the index of the desired columnac
    desired_column = 'Value'  # Replace with the actual column name
    column_index = header.index(desired_column)

    Par_VAl = []
    API_VAL = []

    # Loop through the rows and extract the values from the desired column
    for row in reader:
        column_value = row[column_index]
        Parameter = row[column_index - 1]
        a = Parameter + ' : ' + column_value
        Par_VAl.append([a])  # Convert to list of lists
        API_VAL.append(column_value)

    print(API_VAL)