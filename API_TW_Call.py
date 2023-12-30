import requests
import json
import csv
import random
import datetime
import time

# Open the CSV file for reading
with open('DATA.csv', 'r') as csvfile:
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
        Par_VAl.append([a])  # Convert to list of lists
        API_VAL.append(column_value)


"2023-04-16 11:59:00.00"

def randm_val():
    random_val=[]
    R_V=random.randint(10,20)
    random_val.append(R_V)
    R_V = random.randint(50, 60)
    random_val.append(R_V)
    R_V = random.randint(10, 20)
    random_val.append(R_V)
    R_V = random.randint(-2, 2)
    random_val.append(R_V)
    R_V = random.randint(-2, 2)
    random_val.append(R_V)
    R_V = random.randint(-2, 1)
    random_val.append(R_V)
    return (random_val)



def Api_Insert(val_0,val_1,val_2,val_3,val_4,val_5,val_6,val_7,val_8,val_9,val_10):
    url = 'https://uwsp.uk.gov.in/api/Scada/InsertDetail'
    headers = {'Content-type': 'application/json'}
    date = datetime.datetime.now()
    date = str(date)
    payload = {
        "auth_token": val_0,
        "data": [
            {
                "nSchemeId": val_1,
                "nStructureId": val_2,
                "sPumpStatus": val_3,
                "nPumpDischarge": val_4,
                "nPumpTotalDischarge": val_5,
                "nTankDischarge": val_6,
                "nTankTotalDischarge": val_7,
                "nRunHours": val_8,
                "nWaterSupplyHours": val_9,
                "nPowerOnHours": val_10,
                "dUpdateDate": "2022-11-04 23:59:01.000428"        }
        ]
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers)

    print(response.text)


now = datetime.datetime.now()
min = now.minute
#if min != 0:
 #   Set_Flag = 0

#if now.hour ==23  and now.minute ==51 and now.second > 0 and Set_Flag != 1:


Set_Flag = 1
print(now)
# office _KHA
Api_Insert(API_VAL[0],
           API_VAL[1],
           API_VAL[2],
           API_VAL[3],
           API_VAL[4],
           API_VAL[5],
           API_VAL[6],
           API_VAL[7],
           API_VAL[8],
           API_VAL[9],
           API_VAL[10])
# chopra Farm KHA
Api_Insert(API_VAL[11],
           API_VAL[12],
           API_VAL[13],
           API_VAL[14],
           API_VAL[15],
           API_VAL[16],
           API_VAL[17],
           API_VAL[18],
           API_VAL[19],
           API_VAL[20],
           API_VAL[21])

Api_Insert(API_VAL[22],
           API_VAL[23],
           API_VAL[24],
           API_VAL[25],
           API_VAL[26],
           API_VAL[27],
           API_VAL[28],
           API_VAL[29],
           API_VAL[30],
           API_VAL[31],
           API_VAL[32]
           )

Api_Insert(API_VAL[33],
           API_VAL[34],
           API_VAL[35],
           API_VAL[36],
           API_VAL[37],
           API_VAL[38],
           API_VAL[39],
           API_VAL[40],
           API_VAL[41],
           API_VAL[42],
           API_VAL[43])

Api_Insert(API_VAL[44],
           API_VAL[45],
           API_VAL[46],
           API_VAL[47],
           API_VAL[48],
           API_VAL[49],
           API_VAL[50],
           API_VAL[51],
           API_VAL[52],
           API_VAL[53],
           API_VAL[54])

Api_Insert(API_VAL[55],
           API_VAL[56],
           API_VAL[57],
           API_VAL[58],
           API_VAL[59],
           API_VAL[60],
           API_VAL[61],
           API_VAL[62],
           API_VAL[63],
           API_VAL[64],
           API_VAL[65])

Api_Insert(API_VAL[66],
           API_VAL[67],
           API_VAL[68],
           API_VAL[69],
           API_VAL[70],
           API_VAL[71],
           API_VAL[72],
           API_VAL[73],
           API_VAL[74],
           API_VAL[75],
           API_VAL[76])

Api_Insert(API_VAL[77],
           API_VAL[78],
           API_VAL[79],
           API_VAL[80],
           API_VAL[81],
           API_VAL[82],
           API_VAL[83],
           API_VAL[84],
           API_VAL[85],
           API_VAL[86],
           API_VAL[87])

Api_Insert(API_VAL[88],
           API_VAL[89],
           API_VAL[90],
           API_VAL[91],
           API_VAL[92],
           API_VAL[93],
           API_VAL[94],
           API_VAL[95],
           API_VAL[96],
           API_VAL[97],
           API_VAL[98])

Api_Insert(API_VAL[99],
           API_VAL[100],
           API_VAL[101],
           API_VAL[102],
           API_VAL[103],
           API_VAL[104],
           API_VAL[105],
           API_VAL[106],
           API_VAL[107],
           API_VAL[108],
           API_VAL[109])

Api_Insert(API_VAL[110],
           API_VAL[111],
           API_VAL[112],
           API_VAL[113],
           API_VAL[114],
           API_VAL[115],
           API_VAL[116],
           API_VAL[117],
           API_VAL[118],
           API_VAL[119],
           API_VAL[120],
           )

Api_Insert(API_VAL[121],
           API_VAL[122],
           API_VAL[123],
           API_VAL[124],
           API_VAL[125],
           API_VAL[126],
           API_VAL[127],
           API_VAL[128],
           API_VAL[129],
           API_VAL[130],
           API_VAL[131])

Api_Insert(API_VAL[132],
           API_VAL[133],
           API_VAL[134],
           API_VAL[135],
           API_VAL[136],
           API_VAL[137],
           API_VAL[138],
           API_VAL[139],
           API_VAL[140],
           API_VAL[141],
           API_VAL[142])

Api_Insert(API_VAL[143],
           API_VAL[144],
           API_VAL[145],
           API_VAL[146],
           API_VAL[147],
           API_VAL[148],
           API_VAL[149],
           API_VAL[150],
           API_VAL[151],
           API_VAL[152],
           API_VAL[153])

Api_Insert(API_VAL[154],
           API_VAL[155],
           API_VAL[156],
           API_VAL[157],
           API_VAL[158],
           API_VAL[159],
           API_VAL[160],
           API_VAL[161],
           API_VAL[162],
           API_VAL[163],
           API_VAL[164])

Api_Insert(API_VAL[165],
           API_VAL[166],
           API_VAL[167],
           API_VAL[168],
           API_VAL[169],
           API_VAL[170],
           API_VAL[171],
           API_VAL[172],
           API_VAL[173],
           API_VAL[174],
           API_VAL[175])

Api_Insert(API_VAL[176],
           API_VAL[177],
           API_VAL[178],
           API_VAL[179],
           API_VAL[180],
           API_VAL[181],
           API_VAL[182],
           API_VAL[183],
           API_VAL[184],
           API_VAL[185],
           API_VAL[186])

print(API_VAL)
print('Done')
time.sleep(120)





