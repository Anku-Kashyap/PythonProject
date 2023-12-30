import pyodbc
from pyModbusTCP.client import ModbusClient
from datetime import *

NAT_6_Zone_3BistAttaChakki= [
    1515,
    1514,
    1505,
    1506,
    1507,
    1508,
    1509,
    1510,
    1511,
    1520,
    1512,
    1513,
    1503,
    1526,
    1504,
    1527,
    1501,
    1522,
    1523,
    1524,
    1525,
    1502,
    64400
]
NAT_1_Zone_1GujarowaliOffice=	[
1545,
1544,
1535,
1536,
1537,
1538,
1539,
1540,
1541,
1550,
1542,
1543,
1533,
1556,
1534,
1557,
1531,
1552,
1553,
1554,
1555,
1532,
64401
    ]
NAT_3_Zone_2Khadar_1= [
1575,
1574,
1565,
1566,
1567,
1568,
1569,
1570,
1571,
1580,
1572,
1573,
1563,
1586,
1564,
1587,
1561,
1582,
1583,
1584,
1585,
1562,
64402
]
NAT_2_Zone_1GaneshVihar= [
    1605,
    1604,
    1595,
    1596,
    1597,
    1598,
    1599,
    1600,
    1601,
    1610,
    1602,
    1603,
    1593,
    1616,
    1594,
    1617,
    1531,
    1612,
    1613,
    1614,
    1615,
    1592,
    64403

    ]
NAT_4_Zone_2Khadar_2= [
1635,
1634,
1625,
1626,
1627,
1628,
1629,
1630,
1631,
1640,
1632,
1633,
1623,
1646,
1624,
1647,
1621,
1642,
1643,
1644,
1645,
1622,
64404

]
NAT_7_MadhavVihar= [
    1665,
    1664,
    1655,
    1656,
    1657,
    1658,
    1659,
    1660,
    1661,
    1670,
    1662,
    1663,
    1653,
    1676,
    1654,
    1677,
    1501,
    1672,
    1673,
    1674,
    1675,
    1652,
64405

]
NAT_5_Zone_2DhobalChowk= [	1695,
1694,
1685,
1686,
1687,
1688,
1689,
1690,
1691,
1700,
1692,
1693,
1683,
1706,
1684,
1707,
1681,
1702,
1703,
1704,
1705,
1682,
64406
]
'KHARAKMAF RISHIKESH SITE'
KAH_1_Office= [	1725,
1724,
1715,
1716,
1717,
1718,
1719,
1720,
1721,
1730,
1722,
1723,
1713,
1736,
1714,
1737,
1711,
1732,
1733,
1734,
1735,
1712,
64407
]
KAH_2_GuljarFarm= [	1755,
1754,
1745,
1746,
1747,
1748,
1749,
1750,
1751,
1760,
1752,
1753,
1743,
1766,
1744,
1757,
1741,
1762,
1763,
1764,
1765,
1742,
64408
]
KAH_3_ChopraFarm= [1785,
1784,
1775,
1776,
1777,
1778,
1779,
1780,
1781,
1790,
1782,
1783,
1773,
1796,
1774,
1797,
1771,
1792,
1793,
1794,
1795,
1772,
64409
]
KAH_4_Khadri= [	1815,
1814,
1805,
1806,
1807,
1808,
1809,
1810,
1811,
1820,
1812,
1813,
1803,
1826,
1804,
1827,
1801,
1822,
1823,
1824,
1825,
1802,
64400
]
'PRATITNAGAR RISHIKESH SITE'
PRA_1_Zone_1= [	1845,
1844,
1835,
1836,
1837,
1838,
1839,
1840,
1841,
1850,
1842,
1843,
1833,
1856,
1834,
1857,
1831,
1852,
1853,
1854,
1855,
1832,
64401
]
PRA_2_Zone_2= [	1875,
1874,
1865,
1866,
1867,
1868,
1869,
1870,
1871,
1880,
1872,
1873,
1863,
1886,
1864,
1887,
1861,
1882,
1883,
1884,
1885,
1862,
64402
]
PRA_3_Zone_3_I= [	1905,
1904,
1895,
1896,
1897,
1898,
1899,
1900,
1901,
1910,
1902,
1903,
1893,
1916,
1894,
1917,
1891,
1912,
1913,
1914,
1915,
1892,
64403
]
PRA_4_Zone_3_II= [	1935,
1934,
1925,
1926,
1927,
1928,
1929,
1930,
1931,
1940,
1932,
1933,
1923,
1946,
1924,
1947,
1921,
1942,
1943,
1944,
1945,
1922,
64404
]
PRA_5_Zone_4= [	1965,
1964,
1955,
1956,
1957,
1958,
1959,
1960,
1961,
1970,
1962,
1963,
1953,
1976,
1954,
1977,
1951,
1972,
1973,
1974,
1975,
1952,
64405
]
PRA_6_Zone_5= [	1995,
1994,
1985,
1986,
1987,
1988,
1989,
1990,
1991,
2000,
1992,
1993,
1983,
2006,
1984,
2007,
1981,
2002,
2003,
2004,
2005,
1982,
64406
]


Division_Name=['NATHUAWALA','KAHRAKMAFF','PRATITNAGAR']
Station_Name=['6_Zone_3BistAttaChakki',	'1_Zone_1GujarowaliOffice',	'3_Zone_2Khadar_1',	'2_Zone_1GaneshVihar',	'4_Zone_2Khadar_2',	'7_MadhavVihar', '5_Zone_2DhobalChowk',
              '1_Office',	'2_GuljarFarm', '3_ChopraFarm','4_Khadri',
              '1_Zone_1',	'2_Zone_2',	'3_Zone_3_I',	'4_Zone_3_II',  '5_Zone_4',	'6_Zone_5',]

SERVER_HOST = '192.168.1.14'
SERVER_PORT = 1502

# Create a Modbus TCP client
client = ModbusClient()

# Set the Modbus server host and port
client.host = SERVER_HOST
client.port = SERVER_PORT
def Data_Sql(NAME,Division,Zone):
    Val = []
    now = datetime.now()
    today = date.today()
    today = str(today)
    time = now.strftime("%H:%M:%S")

    for  i in range(23):
            Reg = NAME[i]

            Reg = Reg - 1

            Reg = NAME[i]

            value = client.read_holding_registers(Reg - 1, 1)

            if value:
                """
                """
                if value[0] > 65300 and value[0] < 67000:
                    data = 0
                else:
                    data = (value[0])
            Val.append((data))

            if  i == 21:
                Pwr_fac = Val[7] / 100,

                Datetime = datetime.now()
                print(Datetime)
                Val.append(Division)
                Val.append(Zone)
                Val.append(Datetime)
                Val.append(today)
                Run_hours=Val[18]+(Val[17]/100)
                Power_On_Hours=Val[20]+(Val[19]/100)
                Reg = NAME[i+1]
                Pwr_fac = Val[10] / 100,
                Avg_Current = ((float(Val[5]) + float(Val[6]) + float(Val[7])) / 3)
                Avg_Volt = ((float(Val[2]) + float(Val[3]) + float(Val[4])) / 3)
                KW = (Avg_Volt * Avg_Current * Pwr_fac[0] * 1.72) / 1000
                KW = round(KW)
                print('\nVolt ', Avg_Volt, 'Amp ', Avg_Current)
                print('\nPwr_fac', Pwr_fac)
                print(Zone, 'KW is', KW)
                read_Kwh = client.read_holding_registers(Reg - 1, 1)
                Wr_Value = client.write_single_register(Reg - 1, int(KW) + int(read_Kwh[0]))
                read_Kwh = client.read_holding_registers(Reg - 1, 1)
                KWH = read_Kwh[0]

                conn = pyodbc.connect(
                    'DRIVER={SQL Server};SERVER=' + 'DESKTOP-KS0FE98' + ';DATABASE=' + 'ZONEWISE' + ';UID=' + "Admin" + ';PWD=' + 'Pascal@123')
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO data(Division,	Station,	Date_time, Date,mode,Staus,	Volts_R_Y,	Volts_Y_B,	Volts_B_R,Amp_R,	Amp_Y,	Amp_B,	HZ,	Power_KW,Power_factor,Energry_KWH,	Pump_Discharge_m3_h,Pump_Total_Discharge_m3_day,	OTH_Discharge_m3_h, OTH_Total_Discharge_m3_day,OTH_Level_m,Run_Hours,	Power_On_Hours,Presure_kg_cm2) VALUES (?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?,	?)",
                    Val[22], Val[23], Val[24], Val[25], Val[0], Val[1], Val[2], Val[3], Val[4], Val[5], Val[6],
                    Val[7], Val[8]/10, KW, Val[10]/100, KWH, Val[12]/10, Val[13]*0.6, Val[14]/10, Val[15]*0.6, Val[16]/100, Run_hours,
                    Power_On_Hours, Val[21]/100)

                conn.commit()






def Pt_Sql(Add,Division,Zone):
    Val = []
    now = datetime.now()
    today = date.today()
    today = str(today)
    time = now.strftime("%H:%M:%S")

    Reg = Add

    Reg = Reg - 1

    value = client.read_holding_registers(Reg, 1)
    if value[0] > 65300 and value[0] < 67000:
        data = 0
    else:
        data = (value[0])
    Val.append((data))
    Datetime = datetime.now()
    Val.append(Division)
    Val.append(Zone)
    Val.append(Datetime)
    Val.append(today)
    print(Val)

    conn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + 'DESKTOP-KS0FE98' + ';DATABASE=' + 'ZONEWISE' + ';UID=' + "Admin" + ';PWD=' + 'Pascal@123')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Pt_Data(Division,     Station,	Date_time,  Date,    Pressure) VALUES (?,	?,	?,	?,	?)",
        Val[1], Val[2], Val[3], Val[4],Val[0]/100 )

    conn.commit()
def Test_for_power():
    for i in range(1500, 2010):
                value = client.write_single_register(i - 1, 0)
                value = (client.read_holding_registers(i - 1, 1))
    print('Test for power')


NAT_PT=[4000,4004,4002,4006,4014]
KAH_PT=[4016,4018,4020,4022,4024]
PAT_PT=[4026,4028,4030,4032,4032]
