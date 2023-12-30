import datetime
import os
import csv


def writeToCsv(payload,place):
    logs_folder = 'logs'
    os.makedirs(logs_folder, exist_ok=True)
    current_date = datetime.datetime.now().strftime('%Y%m%d')

    csv_file = os.path.join(logs_folder, place + f'{current_date}_payload.csv')

    # Check if the CSV file exists
    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            fieldnames = reader.fieldnames
    except FileNotFoundError:

        fieldnames = payload.keys()
        with open(csv_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

    with open(csv_file, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(payload)
