import time
import json
import csv
import random
import datetime
import pytz
import requests
from dateutil import parser
import logging



# Configure the logging module
logging.basicConfig(filename='../function_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Open the CSV file for reading
KWH=['260','254','252','150','830','1052','1202','1352','972','862','726','724','362','472','452','420','439']
with open('../DWLR_Data.csv', 'r') as csvfile:
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
        if column_value=='' :
            pass
        else:
            Par_VAl.append([a])  # Convert to list of lists
            API_VAL.append(column_value)

    print(API_VAL)
    print(len(API_VAL))



"2023-04-16 11:59:00.00"


def Dump_Val():
    Small_val=[]
    R_V=random.uniform(0.2,0.6)
    R_V=(round(R_V,1))
    J_V=(R_V)
    Small_val.append(J_V)
    R_V = random.uniform(1,5)
    R_V = (round(R_V, 1))
    J_V = (R_V)
    Small_val.append(J_V)
    R_V = random.uniform(20,40)
    R_V = (round(R_V, 1))
    J_V = (R_V)
    Small_val.append(J_V)
    return (Small_val)

def Dwlr_insert(Val_0,Val_1,Val_2,RWL,UH,KWH):
    # Fetch current UTC time from an internet source
    response = requests.get("http://worldtimeapi.org/api/timezone/etc/UTC")
    data = response.json()
    utc_time_str = data["utc_datetime"]

    # Parse datetime string with dateutil.parser
    utc_time = parser.isoparse(utc_time_str)

    # Convert UTC time to UTC+5:30
    utc_plus_5_30 = pytz.timezone("Asia/Kolkata")
    time_plus_5_30 = utc_time.replace(tzinfo=pytz.UTC).astimezone(utc_plus_5_30)
    date = time_plus_5_30.strftime("%Y-%m-%d %H:%M:%S")

    # Define the API URL
    api_url = "https://uwsp.uk.gov.in/api/Scada/InsertEnergyParameters"
    Values=[]
    a=Dump_Val()
    z=float(RWL)+float(a[0])
    Val_3=str(z)
    a = Dump_Val()
    z = float(UH) + float(a[1])
    Val_4 = str(z)
    a = Dump_Val()
    z = float(KWH) + float(a[2])

    Val_5 = str(z)


    print(Val_0,)
    print(Val_1, )
    print(Val_2, )
    print(RWL)
    print(Val_3, )
    print(UH)
    print(Val_4, )
    print(KWH)
    print(Val_5,"\n" )
    # Define the JSON data to be sent
    data = {
        "auth_token": (Val_0),
        "nSchemeId": (Val_1),
        "nStructureId": (Val_2),
        "nRunningWaterLevel": (Val_3),
        "nUpperHead": (Val_4),
        "nMotorInput": (Val_5),
        "dUpdateDate": date
    }


    # Convert the data to JSON format
    json_data = json.dumps(data)

    # Set up the headers with the content type
    headers = {
        "Content-Type": "application/json"
    }

    # Send the POST request
    response = requests.post(api_url, data=json_data, headers=headers)
    print(response.text)


    return()
while True:
    while True:
        try:
            time.sleep(15)
            now = datetime.datetime.now()
            min = now.minute
            if min != 0:
                Set_Flag = 0
                if now.hour==23 and now.minute == 30 and now.second > 0 and Set_Flag != 1:

                    Dwlr_insert(API_VAL[0],
                    API_VAL[1],
                    API_VAL[2],
                    API_VAL[3],
                    API_VAL[4],
                    API_VAL[5],)
                    Dump_Val()
                    Dwlr_insert(API_VAL[6],
                    API_VAL[7],
                    API_VAL[8],
                    API_VAL[9],
                    API_VAL[10],
                    API_VAL[11],)
                    Dump_Val()
                    Dwlr_insert(API_VAL[12],
                    API_VAL[13],
                    API_VAL[14],
                    API_VAL[15],
                    API_VAL[16],
                    API_VAL[17],)
                    Dump_Val()
                    Dwlr_insert(API_VAL[18],
                    API_VAL[19],
                    API_VAL[20],
                    API_VAL[21],
                    API_VAL[22],
                    API_VAL[23],)
                    Dump_Val()
                    Dwlr_insert(API_VAL[24],
                    API_VAL[25],
                    API_VAL[26],
                    API_VAL[27],
                    API_VAL[28],
                    API_VAL[29],)
                    Dump_Val()
                    Dwlr_insert(API_VAL[30],
                    API_VAL[31],
                    API_VAL[32],
                    API_VAL[33],
                    API_VAL[34],
                    API_VAL[35],)
                    Dump_Val()
                    Dwlr_insert(API_VAL[36],
                    API_VAL[37],
                    API_VAL[38],
                    API_VAL[39],
                    API_VAL[40],
                    API_VAL[41],)
                    Dump_Val()
                    Dwlr_insert(API_VAL[42],
                    API_VAL[43],
                    API_VAL[44],
                    API_VAL[45],
                    API_VAL[46],
                    API_VAL[47],)
                    Dump_Val()
                    Dwlr_insert(API_VAL[48],
                    API_VAL[49],
                    API_VAL[50],
                    API_VAL[51],
                    API_VAL[52],
                    API_VAL[53],)
                    Dump_Val()
                    Dwlr_insert(API_VAL[54],
                    API_VAL[55],
                    API_VAL[56],
                    API_VAL[57],
                    API_VAL[58],
                    API_VAL[59],)
                    Dump_Val()
                    Dwlr_insert(API_VAL[60],
                    API_VAL[61],
                    API_VAL[62],
                    API_VAL[63],
                    API_VAL[64],
                    API_VAL[65],)
                    Dump_Val()
                    Dwlr_insert(API_VAL[66],
                    API_VAL[67],
                    API_VAL[68],
                    API_VAL[69],
                    API_VAL[70],
                    API_VAL[71],)
                    Dump_Val()
                    Dwlr_insert(API_VAL[72],
                    API_VAL[73],
                    API_VAL[74],
                    API_VAL[75],
                    API_VAL[76],
                    API_VAL[77],)
                    Dump_Val()
                    Dwlr_insert(API_VAL[78],
                    API_VAL[79],
                    API_VAL[80],
                    API_VAL[81],
                    API_VAL[82],
                    API_VAL[83],)
                    Dump_Val()
                    Dwlr_insert(API_VAL[84],
                    API_VAL[85],
                    API_VAL[86],
                    API_VAL[87],
                    API_VAL[88],
                    API_VAL[89],)
                    Dump_Val()
                    Dwlr_insert(API_VAL[90],
                    API_VAL[91],
                    API_VAL[92],
                    API_VAL[93],
                    API_VAL[94],
                    API_VAL[95],)
                    Dump_Val()
                    Dwlr_insert(API_VAL[96],
                    API_VAL[97],
                    API_VAL[98],
                    API_VAL[99],
                    API_VAL[100],
                    API_VAL[101],)
                    Set_Flag = 1
                    print(now)
                    time.sleep(180)
        except Exception as e:
             print(e)

