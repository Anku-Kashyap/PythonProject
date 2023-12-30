from pyModbusTCP.client import ModbusClient
from datetime import *
import couchdb
import time
MB_W_LIST=[
8001,	8002,	8003,	8004,	8013,	8006,	8007,	8008,	8009,	8010,	8011,	8012,	8013,
8021,	8022,	8023,	8024,	8033,	8026,	8027,	8028,	8029,	8030,	8031,	8032,	8033,
8041,	8042,	8043,	8044,	8053,	8046,	8047,	8048,	8049,	8050,	8051,	8052,	8053,
8061,	8062,	8063,	8064,	8073,	8066,	8067,	8068,	8069,	8070,	8071,	8072,	8073,
8081,	8082,	8083,	8084,	8093,	8086,	8087,	8088,	8089,	8090,	8091,	8092,	8093,
8101,	8102,	8103,	8104,	8113,	8106,	8107,	8108,	8109,	8110,	8111,	8112,	8113,
]


MB_VAL=[
4,	4,	4,	22,	22,	22,	440,	440,	440,	100,	100,	100,	1,
4,	4,	4,	22,	22,	22,	440,	440,	440,	100,	100,	100,	1,
4,	4,	4,	22,	22,	22,	440,	440,	440,	100,	100,	100,	1,
4,	4,	4,	22,	22,	22,	440,	440,	440,	100,	100,	100,	1,
4,	4,	4,	22,	22,	22,	440,	440,	440,	100,	100,	100,	1,
4,	4,	4,	22,	22,	22,	440,	440,	440,	100,	100,	100,	1,
]
Gauri_Talab= 	[	9105,	9106,	9107,	9108,	9109,	9110,	9111,	9112,	9120,	9113,	9115,	9114,	8007,	8010,	8001,	8004,	8004,	8005,	8003,	8006,	9104,	9102,	9103,	9101,	9122,	9123,	9124,	9125,	9126,	9137,	9130,60007	]
Anganwadi	=[	9135,	9136,	9137,	9138,	9139,	9140,	9141,	9142,	9150,	9143,	9145,	9144,	8027,	8030,	8021,	8024,	8024,	8025,	8023,	8026,	9134,	9132,	9133,	9131,	9152,	9153,	9154,	9155,	9156,	9167,	9180,60008	]
Mokshdham	=[	9165,	9166,	9167,	9168,	9169,	9191,	9171,	9172,	9180,	9173,	9175,	9174,	8047,	8050,	8041,	8044,	8044,	8045,	8043,	8046,	9164,	9162,	9163,	9161,	9182,	9183,	9184,	9185,	9186,	9197,	9190,60009	]
Along_NHAI	=[	9195,	9196,	9197,	9198,	9199,	7100,	7101,	7102,	7110,	7103,	7105,	7104,	8067,	8091,	8061,	8064,	8064,	8065,	8063,	8066,	9194,	9192,	9193,	9191,	7112,	7113,	7114,	7115,	7116,	7127,	7120,60010	]
Near_Deep_public_School	=[	9225,	9226,	9227,	9228,	9229,	9230,	9231,	9232,	9240,	9233,	9235,	9234,	8087,	8090,	8081,	8084,	8084,	8085,	8083,	8086,	9224,	9222,	9223,	9221,	9242,	9243,	9244,	9245,	9246,	9257,	9250,60011	]
TW_BLOCK=	[	9255,	9256,	9257,	9258,	9259,	9280,	9261,	9262,	9291,	9263,	9265,	9264,	6107,	6110,	6101,	6104,	6104,	6105,	6103,	6106,	9254,	9252,	9253,	9251,	9272,	9273,	9274,	9275,	9276,	9287,	9280,60012]



Nat_Zone=[1531,1532,1534,4000,4014,4012,4002,4006,4014,1592,1501,4004,1502,1504]#4000(5000),4012(5012),4004(5004),5014(4004)
kah_Zone=[1711,1712,1714,4016,1741,4018,4020,1774,1742,1771,4022,4024,1772,1774] #
Pat_Zone=[4042,1832,4043,4026,6044,1862,4045,4028,4040,6892,4041,4030,6038,6892,4039,4032,4036,1952,4037,4034]


SERVER_HOST = '192.168.1.14'
SERVER_PORT = 1502

# Create a Modbus TCP client
client = ModbusClient()

# Set the Modbus server host and port
client.host = SERVER_HOST
client.port = SERVER_PORT

def Test_for_power():
    for i in range(7001, 7190):
                value = client.write_single_register(i - 1, 0)
                value = (client.read_holding_registers(i - 1, 1))
    print('Test for power')
def MB_WRITE():
    for i in range(77):
        Reg = MB_W_LIST[i]
        Reg = Reg - 1
        wr = client.write_single_register(Reg, MB_VAL[i])
        value = client.read_holding_registers(Reg, 1)
        # time.sleep(0.5)

        if i == 77:
            print('Val_writeen__To_Reg')


def MB_Couch(NAME,DB,ID):
        server = couchdb.Server('http://Admin:War_ship_84@192.168.1.14:5984/')
        doc_id = ID
        db=server[DB]
        doc = db[doc_id]

        Val = []
        now = datetime.now()
        today = date.today()
        today = str(today)
        time = now.strftime("%H:%M:%S")
        for Reg in NAME:
            value = client.read_holding_registers(Reg - 1, 1)
            

            if value:
                """
                """
                if value[0] > 65300 and value[0] < 67000:
                    data = 0
                else:
                    data = (value[0])
                    """print(type(data))"""
                Val.append(data)
        print(Val)
        if Val[7] == 1:
            Val[7] = 0.95
        else:
            Val[7] = Val[7]
        if Val[10] > 0:
            Val[10] = 'Auto'
        elif Val[10]==0 and Val[0]>0 and Val[1]>0 and Val[2]>0:
            Val[10] = 'Manual'
        else:
            Val[10]='POWER FAIL'
        if Val[11] > 0:
            Val[11] = 'RUNNING'
        else:
            Val[11] = 'STOP'
        Val[22]=0
        doc['tag0'] = Val[0],
        doc['R VOLT'] = Val[0],
        doc['tag1'] = Val[1],
        doc['Y_VOlt'] = Val[1]
        doc['tag2'] = Val[2],
        doc['B_VOlt'] = Val[2]

        doc['tag6'] = round(Val[6] / 10, 2),
        doc['Freq'] = round(Val[6] / 10, 2),

        if Val[11]=='RUNNING':

            doc['tag3'] = Val[3],
            doc['R-Amps'] = Val[3]
            doc['tag4'] = Val[4],
            doc['Y-Amps'] = Val[4]
            doc['tag5'] = Val[5],
            doc['B-Amps'] = Val[5]
            doc['tag7'] = Val[7] / 100,
            Pwr_fac=(Val[7] / 100),
            doc['Pwr_Fac'] = Val[7] / 100,
            Avg_Current = ((float(Val[4]) + float(Val[5]) + float(Val[3])) / 3)
            Avg_Volt = ((float(Val[0]) + float(Val[1]) + float(Val[2])) / 3)
            KW = (Avg_Volt * Avg_Current * Pwr_fac[0] * 1.732) / 1000
            print(KW)
            print('KWH ' , Val[31])
            if min != 0:
                Set_Flag = 0

            if now.minute == 15 and now.second > 0 and Set_Flag != 1:
                read_Kwh = client.read_holding_registers(Reg - 1, 1)
                Wr_Value = client.write_single_register(Reg - 1, int(KW) + int(read_Kwh[0]))
                print('Value to database')

                Set_Flag = 1
                print(Set_Flag)
                Test_for_power()
                time.sleep(60)


            doc['tag8'] = round(KW,2),
            doc['tag30'] = Val[21] / 100,
            doc['Inlet_Press'] = Val[21] / 100,
            doc['tag31'] = Val[22] / 10,
            doc['Inlet_Flow'] = Val[22] / 10,
        else:
            doc['tag7'] = 0,
            doc['KW']=0,
            doc['tag8'] = 0,
            doc['tag3'] = 0,
            doc['R-Amps'] = 0,
            doc['tag4'] = 0,
            doc['Y-Amps'] =0,
            doc['tag5'] = 0,
            doc['B-Amps'] = 0,
            doc['Inlet_Press'] = 0,
            doc['tag30'] =0,
            doc['tag31'] = 0,
            doc['Inlet_Flow'] = 0,



        doc['tag9'] = Val[31],
        doc['KWH'] = Val[31],
        doc['tag10'] = Val[10],
        doc['Oper_Mode'] = Val[10],
        doc['tag11'] = (Val[27], " H ", Val[26], " M ",),
        doc['Power_On_Hrs'] = (Val[27], " H ", Val[26], " M ",),
        doc['tag12'] = Val[11],
        doc['Status'] = Val[11],
        doc['tag13'] = (Val[25], " H ", Val[24], " M "),
        doc['Pump_on_Hrs'] = (Val[25], " H ", Val[24], " M "),
        doc['tag14'] = Val[12],
        doc['Max_Volt'] = Val[12],
        doc['tag15'] = 350,
        doc['Min_Volt'] = 350,
        doc['tag16'] = Val[13],
        doc['Max_Cur'] = Val[13],
        doc['tag17'] = 50,
        doc['Min_Cur'] = 50,
        doc['tag18'] = 25,
        doc['Unblance_Current'] = 25,
        doc['tag19'] = Val[14],
        doc['1st_On_Time'] = Val[14],
        doc['tag20'] = Val[15],
        doc['1st_Off_Time'] = Val[15],
        doc['tag21'] = Val[16],
        doc['2nd_On_Time'] = Val[16],
        doc['tag22'] = Val[17],
        doc['2nd_Off_Time'] = Val[17],
        doc['tag23'] = Val[18],
        doc['3rd_On_Time'] = Val[18],
        doc['tag24'] = Val[19],
        doc['3rd_Off_Time'] = Val[19],
        doc['tag25'] = Val[22] / 10,
        doc['Pump_Dis'] = Val[22] / 10,
        a = (Val[22] * Val[25])/10
        doc['tag26'] = round(a),
        doc['Pump_Dis_tot'] = round(Val[28] * 0.01, 2),
        doc['tag27'] = Val[20] / 10,
        doc['Tank_Dis'] = Val[20] / 10,

        doc['tag28'] =round(a),
        doc['Tank_Dis_Tot'] = round(Val[29] * 0.01, 2),
        doc['tag29'] = 0,
        doc['Event'] = 0,
        doc['tag32'] = Val[23] / 100,
        print(Val[23]/100)
        doc['Level'] = Val[23] / 100,
        doc['tag33'] = today,
        doc['Date'] = today,
        doc['tag34'] = time,
        doc['Time'] = time,
        doc['tag35'] = Val[30]/100,
        doc['Ground_Water_Level'] = Val[30]/100,



        #print(doc)
        print("    \n")
        db.save(doc)









def NAT_Zone_MB_Couch(NAME, DB, ID):
    server = couchdb.Server('http://Admin:War_ship_84@192.168.1.14:5984/')
    doc_id = ID
    db = server[DB]
    doc = db[doc_id]
    Val = []
    Val = []


    now = datetime.now()
    today = date.today()
    today = str(today)
    time = now.strftime("%H:%M:%S")
    for Reg in NAME:
        value = client.read_holding_registers(Reg-1, 1)
        
        if value:
            
            if value[0] > 65300 and value[0] < 67000:
                data = 0
            else:
                data = (value[0])
            Val.append(data)
    doc['tag0'] = Val[0] / 100,

    doc['tag1'] = Val[1] / 100,
    doc['tag2'] = Val[2] / 10,
    doc['tag3'] = Val[3] / 100,
    doc['tag4'] = Val[4] / 100,
    doc['tag5'] = Val[5] / 100,
    doc['tag6'] = Val[6] / 100,
    doc['tag7'] = Val[7] / 100,
    doc['tag8'] = Val[8] / 10,
    doc['tag9'] = Val[9] / 100,
    doc['tag10'] = Val[10] / 100,
    doc['tag11'] = Val[11] / 100,
    doc['tag12'] = Val[13] / 10,
    doc['tag13'] = Val[12] / 100,
    doc['tag34'] = today
    doc['tag15'] = time
    db.save(doc)
    print("\n")

    client.close()



def KAH_Zone_MB_Couch(NAME, DB, ID):
    server = couchdb.Server('http://Admin:War_ship_84@192.168.1.14:5984/')
    doc_id = ID
    db = server[DB]
    doc = db[doc_id]
    Val = []
    now = datetime.now()
    today = date.today()
    today = str(today)
    time = now.strftime("%H:%M:%S")
    for Reg in NAME:
        print(Reg)
        value = client.read_holding_registers(Reg - 1, 1)

        if value:
            """"""
            if value[0] > 65300 and value[0] < 67000:
                data = 0
            else:
                data = (value[0])
            Val.append(data)
    print(len(Val))
    print(Val)

    doc['tag0'] = Val[0] / 100,
    doc['tag1'] = Val[1] / 100,
    doc['tag2'] = Val[2] / 10,
    doc['tag3'] = Val[3] / 100,
    doc['tag4'] = Val[4] / 100,
    if Val[5] == 0:
        Val[5] = 120
    doc['tag5'] = Val[5] / 100,
    doc['tag6'] = Val[6] / 100,
    doc['tag7'] = Val[7] / 10,
    doc['tag8'] = Val[8] / 100,
    doc['tag9'] = Val[9] / 100,
    doc['tag10'] = Val[10] / 100,
    doc['tag11'] = Val[11] / 100,
    doc['tag12'] = Val[13] / 10,
    doc['tag13'] = Val[12] / 100,
    doc['tag14'] = today
    doc['tag15'] = time
    db.save(doc)
    #print(doc)
    print("\n")
    client.close()


def PAT_Zone_MB_Couch(NAME, DB, ID):
    server = couchdb.Server('http://Admin:War_ship_84@192.168.1.14:5984/')
    doc_id = ID
    db = server[DB]
    doc = db[doc_id]
    Val = []
    now = datetime.now()
    today = date.today()
    today = str(today)
    time = now.strftime("%H:%M:%S")

    for Reg in NAME:
        value = client.read_holding_registers(Reg - 1, 1)
        
        print(Reg)
        if value:
            """"""
            if value[0] > 65300 and value[0] < 67000:
                data = 0

            else:
                data = (value[0])
        print(data)
        Val.append(data)
    doc['tag0'] = Val[0] / 100,
    doc['tag1'] = Val[1] / 100,
    doc['tag2'] = Val[2] / 10,
    doc['tag3'] = Val[3] / 100,
    doc['tag4'] = Val[4] / 100,
    doc['tag5'] = Val[5] / 100,
    doc['tag6'] = Val[6] / 10,
    doc['tag7'] = Val[7] / 100,
    doc['tag8'] = Val[8] / 100,
    doc['tag9'] = Val[9] / 100,
    doc['tag10'] = Val[10] / 10,
    doc['tag11'] = Val[11] / 100,
    doc['tag12'] = Val[12] / 100,
    doc['tag13'] = Val[13] / 100,
    doc['tag14'] = Val[14] / 10,
    doc['tag15'] = Val[15] / 100,
    doc['tag16'] = Val[16] / 100,
    doc['tag17'] = Val[17] / 100,
    doc['tag18'] = Val[18] / 10,
    doc['tag19'] = Val[19] / 100,
    doc['tag34'] = today
    doc['tag35'] = time
    db.save(doc)
    #print(doc)
    print("\n")
    client.close()


