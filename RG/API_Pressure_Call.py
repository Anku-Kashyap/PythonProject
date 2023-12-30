import time
import json
import csv
import random
import datetime
import pytz
import requests
from dateutil import parser
import logging
import schedule
import sys
sys.path.append('E:\Project\pythonProject')
from utils.payloadLogger import writeToCsv


# Configure the logging module
logging.basicConfig(filename='../function_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Open the CSV file for reading

with open('../Pressure.csv', 'r') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)

    # Read the header row to get the column names
    header = next(reader)

    # Find the index of the desired column
    desired_column = 'Value'  # Replace with the actual column name
    column_index = header.index(desired_column)

    Par_VAl = []
    API_VAL = []

    # Loop through the rows and extract the values from the desired column
    for row in reader:
        column_value = row[column_index]
        Parameter = row[column_index - 1]
        a = Parameter + ' : ' + column_value
        if column_value == '':
            pass
        else:
            Par_VAl.append([a])  # Convert to list of lists
            API_VAL.append(column_value)


"2023-04-16 11:59:00.00"


def randm_val():
    Large_val = []
    R_V = random.uniform(16.2, 20.4)
    R_V = (round(R_V, 1))
    J_V = str(R_V)
    Large_val.append(J_V)
    R_V = random.uniform(16.2, 20.4)
    R_V = (round(R_V, 1))
    J_V = str(R_V)
    Large_val.append(J_V)
    return (Large_val)


def Dump_Val():
    Small_val = []
    R_V = random.uniform(8.2, 12.2)
    R_V = (round(R_V, 1))
    J_V = str(R_V)
    Small_val.append(J_V)
    R_V = random.uniform(6.2, 11.2)
    R_V = (round(R_V, 1))
    J_V = str(R_V)
    Small_val.append(J_V)
    return (Small_val)


def API_Pressure_Insert(val_0, val_1, val_2):
    # Fetch current UTC time from an internet source
    response = requests.get("http://worldtimeapi.org/api/timezone/etc/UTC")
    data = response.json()
    utc_time_str = data["utc_datetime"]

    # Parse datetime string with dateutil.parser
    utc_time = parser.isoparse(utc_time_str)

    # Convert UTC time to UTC+5:30
    utc_plus_5_30 = pytz.timezone("Asia/Kolkata")
    time_plus_5_30 = utc_time.replace(
        tzinfo=pytz.UTC).astimezone(utc_plus_5_30)
    date = time_plus_5_30.strftime("%Y-%m-%d %H:%M:%S")
    L = randm_val()

    url = 'https://uwsp.uk.gov.in/api/Pressure/InsertPressure'
    headers = {'Content-type': 'application/json'}
    payload = {
        "auth_token": val_0,
        "nSchemeId": val_1,
        "nPredeterminedPointId": val_2,
        "nPressure": L[0],
        "nTotalPressure": L[1],
        "dUpdateDate": date
    }
    writeToCsv(payload,'RG')

    print(L[0], L[1])

    # response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response.text)


def API_Pressure_Insert1(val_0, val_1, val_2):
    # Fetch current UTC time from an internet source
    response = requests.get("http://worldtimeapi.org/api/timezone/etc/UTC")
    data = response.json()
    utc_time_str = data["utc_datetime"]

    # Parse datetime string with dateutil.parser
    utc_time = parser.isoparse(utc_time_str)

    # Convert UTC time to UTC+5:30
    utc_plus_5_30 = pytz.timezone("Asia/Kolkata")
    time_plus_5_30 = utc_time.replace(
        tzinfo=pytz.UTC).astimezone(utc_plus_5_30)
    date = time_plus_5_30.strftime("%Y-%m-%d %H:%M:%S")
    s = Dump_Val()

    url = 'https://uwsp.uk.gov.in/api/Pressure/InsertPressure'
    headers = {'Content-type': 'application/json'}
    payload = {
        "auth_token": val_0,
        "nSchemeId": val_1,
        "nPredeterminedPointId": val_2,
        "nPressure": s[0],
        "nTotalPressure": s[1],
        "dUpdateDate": date
    }
    writeToCsv(payload,'RG')

    print(s[0], s[1])
    # response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response.text)


def job():
    try:
        now = datetime.datetime.now()
        if now.hour == 23 or 0 <= now.hour <= 5: 
            API_Pressure_Insert1(API_VAL[0], API_VAL[1], API_VAL[2])
            API_Pressure_Insert1(API_VAL[3], API_VAL[4], API_VAL[5])
            API_Pressure_Insert1(API_VAL[6], API_VAL[7], API_VAL[8],)
            API_Pressure_Insert1(API_VAL[9], API_VAL[10], API_VAL[11])
            API_Pressure_Insert1(API_VAL[12], API_VAL[13], API_VAL[14])
            API_Pressure_Insert1(API_VAL[15], API_VAL[16], API_VAL[17])
            API_Pressure_Insert1(API_VAL[18], API_VAL[19], API_VAL[20])
            API_Pressure_Insert1(API_VAL[21], API_VAL[22], API_VAL[23])
            API_Pressure_Insert1(API_VAL[24], API_VAL[25], API_VAL[26])
            API_Pressure_Insert1(API_VAL[27], API_VAL[28], API_VAL[29])
            API_Pressure_Insert1(API_VAL[30], API_VAL[31], API_VAL[32])
            API_Pressure_Insert1(API_VAL[33], API_VAL[34], API_VAL[35])
            API_Pressure_Insert1(API_VAL[36], API_VAL[37],  API_VAL[38])
            API_Pressure_Insert1(API_VAL[39],  API_VAL[40],  API_VAL[41], )
            API_Pressure_Insert1(API_VAL[42], API_VAL[43], API_VAL[44])
            print(now)

        elif 6 <= now.hour <= 22:
            print("Big Val")

            API_Pressure_Insert(API_VAL[0], API_VAL[1], API_VAL[2])
            API_Pressure_Insert(API_VAL[3], API_VAL[4], API_VAL[5])
            API_Pressure_Insert(API_VAL[6], API_VAL[7], API_VAL[8],)
            API_Pressure_Insert(API_VAL[9], API_VAL[10], API_VAL[11])
            API_Pressure_Insert(API_VAL[12], API_VAL[13],  API_VAL[14])
            API_Pressure_Insert(API_VAL[15], API_VAL[16], API_VAL[17])
            API_Pressure_Insert(API_VAL[18], API_VAL[19],  API_VAL[20])
            API_Pressure_Insert(API_VAL[21],  API_VAL[22], API_VAL[23])
            API_Pressure_Insert(API_VAL[24], API_VAL[25], API_VAL[26])
            API_Pressure_Insert(API_VAL[27],  API_VAL[28],  API_VAL[29])
            API_Pressure_Insert(API_VAL[30],  API_VAL[31],  API_VAL[32])
            API_Pressure_Insert(API_VAL[33], API_VAL[34], API_VAL[35])
            API_Pressure_Insert(API_VAL[36],   API_VAL[37],  API_VAL[38])
            API_Pressure_Insert(API_VAL[39],   API_VAL[40], API_VAL[41], )
            API_Pressure_Insert(API_VAL[42], API_VAL[43],  API_VAL[44])
            print(now)

        else:
            print("Not in Defined Value")

    except Exception as e:
        print(e)


# Schedule the job to run every hour
schedule.every().minute.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

