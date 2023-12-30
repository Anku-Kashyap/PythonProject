from pyModbusTCP.client import ModbusClient
from datetime import *
import couchdb

MB_W_LIST = [
    1301, 1302, 1303, 1304, 1313, 1306, 1307, 1308, 1309, 1310, 1311, 1312, 1313,
    1321, 1322, 1323, 1324, 1333, 1326, 1327, 1328, 1329, 1330, 1331, 1332, 1333,
    1431, 1342, 1343, 1344, 1353, 1346, 1347, 1348, 1349, 1350, 1351, 1352, 1353,
    1361, 1362, 1363, 1364, 1373, 1366, 1367, 1368, 1369, 1370, 1371, 1372, 1373,
    1381, 1382, 1383, 1384, 1393, 1386, 1387, 1388, 1389, 1390, 1391, 1392, 1393,
    1401, 1402, 1403, 1404, 1413, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413,
    1421, 1422, 1423, 1424, 1433, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433,
    1441, 1442, 1443, 1444, 1453, 1446, 1447, 1448, 1449, 1450, 1451, 1452, 1453,
    1461, 1462, 1463, 1464, 1473, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473,
    1481, 1482, 1483, 1484, 1493, 1486, 1487, 1488, 1489, 1490, 1491, 1492, 1493,
    301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313,
    321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333

]

MB_VAL = [
    4, 4, 4, 22, 22, 22, 440, 440, 440, 100, 100, 100, 1,
    4, 4, 4, 22, 22, 22, 440, 440, 440, 100, 100, 100, 1,
    4, 4, 4, 22, 22, 22, 440, 440, 440, 100, 100, 100, 1,
    4, 4, 4, 22, 22, 22, 440, 440, 440, 100, 100, 100, 1,
    4, 4, 4, 22, 22, 22, 440, 440, 440, 100, 100, 100, 1,
    4, 4, 4, 22, 22, 22, 440, 440, 440, 100, 100, 100, 1,
    4, 4, 4, 22, 22, 22, 440, 440, 440, 100, 100, 100, 1,
    4, 4, 4, 22, 22, 22, 440, 440, 440, 100, 100, 100, 1,
    4, 4, 4, 22, 22, 22, 440, 440, 440, 100, 100, 100, 1,
    4, 4, 4, 22, 22, 22, 440, 440, 440, 100, 100, 100, 1,
    4, 4, 4, 22, 22, 22, 440, 440, 440, 100, 100, 100, 1,
    4, 4, 4, 22, 22, 22, 440, 440, 440, 100, 100, 100, 1,
]

ZONE3_JAL_NIGAM = [2305, 2306, 2307, 2308, 2309, 2310, 2311, 2314, 2340, 2313, 2315, 2314, 1307, 1310, 1301, 1304, 1304,
                   1305, 1303, 1306, 2304, 2302, 2303, 2301, 2322, 2323, 2324, 2325, 2326, 2327, 2330, 9021, ]
ZONE1_GDHAI_VALI_GALI = [2365, 2366, 2367, 2368, 2369, 2370, 2371, 2372, 2380, 2373, 2375, 2374, 1347, 1350, 1341, 1344,
                         1342, 1345, 1343, 1346, 2364, 2362, 2363, 2361, 2382, 2383, 2384, 2385, 2386, 2387, 2390,
                         9023, ]
ZONE2_SIDHESWAR = [2425, 2426, 2427, 2428, 2429, 2430, 2431, 2432, 2440, 2433, 2435, 2434, 1387, 1390, 1381, 1384, 1382,
                   1385, 1383, 1386, 2424, 2422, 2423, 2421, 2442, 2443, 2444, 2445, 2446, 2447, 2450, 9025, ]
ZONE2_GURUKUL_KANGRI_CAMPUS = [2455, 2456, 2457, 2458, 2459, 2460, 2461, 2462, 2470, 2463, 2465, 2464, 1407, 1410, 1401,
                               1404, 1402, 1405, 1403, 1406, 2454, 2452, 2453, 2451, 2472, 2473, 2474, 2475, 2476, 2477,
                               2480, 9026, ]
ZONE2_GATE_NO_6 = [2485, 2486, 2487, 2488, 2489, 2490, 2491, 2492, 2500, 2493, 2495, 2494, 1427, 1430, 1421, 1424, 1422,
                   1425, 1423, 1426, 2484, 2482, 2483, 2481, 2502, 2503, 2504, 2505, 2506, 2507, 2510, 9027, ]
ZONE2_GURUKUL_CAMPUS = [2515, 2516, 2517, 2518, 2519, 2520, 2521, 2522, 2530, 2523, 2525, 2524, 1447, 1450, 1441, 1444,
                        1442, 1445, 1443, 1446, 2514, 2512, 2513, 2511, 2532, 2533, 2534, 2535, 2536, 2537, 2540,
                        9028, ]
ZONE3_SLAGE_FARM = [2395, 2396, 2397, 2398, 2399, 2400, 2401, 2402, 2410, 2403, 2405, 2404, 1367, 1370, 1361, 1364,
                    1362, 1365, 1363, 1366, 2394, 2392, 2393, 2391, 2412, 2413, 2414, 2415, 2416, 2417, 2420, 9024, ]
ZONE1_MATRANCHAL = [2335, 2336, 2337, 2338, 2339, 2340, 2341, 2342, 2350, 2343, 2345, 2344, 1327, 1330, 1321, 1324,
                    1322, 1325, 1323, 1326, 2334, 2332, 2333, 2331, 2352, 2353, 2354, 2355, 2356, 2357, 2360, 9022, ]
ZONE4_DR_AMBEDKAR_PARK = [2545, 2546, 2547, 2548, 2549, 2550, 2551, 2552, 2560, 2553, 2555, 2554, 1467, 1470, 1461,
                          1464, 1462, 1465, 1463, 1466, 2544, 2542, 2543, 2541, 2562, 2563, 2564, 2565, 2566, 2567,
                          2570, 9029, ]
ZONE4_ACHIVER_HOMES = [2575, 2576, 2577, 2578, 2579, 2580, 2581, 2582, 2590, 2583, 2585, 2584, 1487, 1490, 1481, 1484,
                       1482, 1485, 1483, 1486, 2574, 2572, 2573, 2571, 2592, 2593, 2594, 2595, 2596, 2597, 2600, 9030, ]
ZONE4_RAMLEELA = [2605, 2606, 2607, 2608, 2609, 2610, 2611, 2612, 2620, 2613, 2615, 2614, 307, 310, 301, 304, 302, 305,
                  303, 306, 2604, 2602, 2603, 2601, 2622, 2623, 2624, 2625, 2626, 2627, 2630, 9031, ]

Nat_Zone = [1531, 1532, 1534, 4000, 4014, 4012, 4002, 4006, 4014, 1592, 1501, 4004, 1502,
            1504]  # 4000(5000),4012(5012),4004(5004),5014(4004)
kah_Zone = [1711, 1712, 1714, 4016, 1741, 4018, 4020, 1774, 1742, 1771, 4022, 4024, 1772, 1774]  #
Pat_Zone = [4042, 1832, 4043, 4026, 6044, 1862, 4045, 4028, 4040, 6892, 4041, 4030, 6038, 6892, 4039, 4032, 4036, 1952,
            4037, 4034]

SERVER_HOST = '192.168.1.14'
SERVER_PORT = 1502

# Create a Modbus TCP client
client = ModbusClient()

# Set the Modbus server host and port
client.host = SERVER_HOST
client.port = SERVER_PORT


def Test_for_power():
    for i in range(2301, 2630):
        value = client.write_single_register(i - 1, 0)
        value = (client.read_holding_registers(i - 1, 1))
    print('Test for power')


def MB_WRITE():
    for i in range(156):
        Reg = MB_W_LIST[i]
        Reg = Reg - 1
        wr = client.write_single_register(Reg, MB_VAL[i])
        value = client.read_holding_registers(Reg, 1)
        # time.sleep(0.5)

        if i == 220:
            print('Val_writeen__To_Reg')


def MB_Couch(NAME, DB, ID):
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

        if value:
            """
            """
            if value[0] > 65200 and value[0] < 67000:
                data = 0
            else:
                data = (value[0])
                """print(type(data))"""
            Val.append(data)
    if Val[7] == 1:
        Val[7] = 0.95
    else:
        Val[7] = Val[7]
    if Val[10] > 0:
        Val[10] = 'Auto'
    else:
        Val[10] = 'Manual'
    if Val[11] > 0:
        Val[11] = 'RUNNING'
    else:
        Val[11] = 'STOP'
        Val[22] = 0
    doc['tag0'] = Val[0],
    doc['R VOLT'] = Val[0],
    doc['tag1'] = Val[1],
    doc['Y_VOlt'] = Val[1]
    doc['tag2'] = Val[2],
    doc['B_VOlt'] = Val[2]

    doc['tag6'] = round(Val[6] / 10, 2),
    doc['Freq'] = round(Val[6] / 10, 2),

    if Val[11] == 'RUNNING':

        doc['tag3'] = Val[3],
        doc['R-Amps'] = Val[3]
        doc['tag4'] = Val[4],
        doc['Y-Amps'] = Val[4]
        doc['tag5'] = Val[5],
        doc['B-Amps'] = Val[5]
        doc['tag7'] = Val[7] / 100,
        Pwr_fac = (Val[7] / 100),
        doc['Pwr_Fac'] = Val[7] / 100,
        Avg_Current = ((float(Val[4]) + float(Val[5]) + float(Val[3])) / 3)
        Avg_Volt = ((float(Val[0]) + float(Val[1]) + float(Val[2])) / 3)
        KW = (Avg_Volt * Avg_Current * Pwr_fac[0] * 1.732) / 10
        print(NAME, Val[7] / 100)
        print(KW)

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

        doc['tag8'] = round(KW, 2),
        doc['tag30'] = Val[21] / 100,
        doc['Inlet_Press'] = Val[21] / 100,
        doc['tag31'] = Val[22] / 10,
        doc['Inlet_Flow'] = Val[22] / 10,
    else:
        doc['tag7'] = 0,
        doc['KW'] = 0,
        doc['tag8'] = 0,
        doc['tag3'] = 0,
        doc['R-Amps'] = 0,
        doc['tag4'] = 0,
        doc['Y-Amps'] = 0,
        doc['tag5'] = 0,
        doc['B-Amps'] = 0,
        doc['Inlet_Press'] = 0,
        doc['tag30'] = 0,
        doc['tag31'] = 0,
        doc['Inlet_Flow'] = 0,

    doc['tag7'] = Val[7],
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
    a = (Val[22] * Val[25]) / 10
    doc['tag26'] = round(a),
    doc['Pump_Dis_tot'] = round(Val[28] * 0.01, 2),
    doc['tag27'] = Val[20] / 10,
    doc['Tank_Dis'] = Val[20] / 10,

    doc['tag28'] = round(a),
    doc['Tank_Dis_Tot'] = round(Val[29] * 0.01, 2),
    doc['tag29'] = 0,
    doc['Event'] = 0,
    doc['tag32'] = Val[23] / 100,
    print(Val[23] / 100)
    doc['Level'] = Val[23] / 100,
    doc['tag33'] = today,
    doc['Date'] = today,
    doc['tag34'] = time,
    doc['Time'] = time,
    doc['tag35'] = Val[30] / 100,
    doc['Ground_Water_Level'] = Val[30] / 100,

    # print(doc)
    print(Val)
    print('Power_Factor', Val[7])
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
        value = client.read_holding_registers(Reg - 1, 1)

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
    # print(doc)
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
    # print(doc)
    print("\n")
    client.close()


MB_Couch(ZONE3_SLAGE_FARM, 'vtlzone3', '101')