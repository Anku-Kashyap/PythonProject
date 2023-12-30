from RG.Modbus_fun import *
import datetime
import time

while True:
    while True:

        try:
            now = datetime.datetime.now()
            min = now.minute
            MB_WRITE()
            print('Kharakmaff')
            MB_Couch(KAHRAKMAFF_1_Office, 'kah', '101')
            print('kah office 1')
            MB_Couch(KAHRAKMAFF_2_GuljarFarm, 'kah', '102')
            print("kah Guljar farm")
            MB_Couch(KAHRAKMAFF_4_Khadri, 'kah', '103')
            print("kah Khadri")
            MB_Couch(KAHRAKMAFF_3_ChopraFarm, 'kah', '104')
            print("kah ChopraFarm")
            print("\n")
            print('Nathuawala')

            MB_Couch(NATHUAWALA_1_Zone_1GujarowaliOffice, 'nat', '201')

            print('Gujarowalioffice')
            MB_Couch(NATHUAWALA_2_Zone_1GaneshVihar, 'nat', '202')
            print("Ganeshvihar")
            MB_Couch(NATHUAWALA_3_Zone_2Khadar_1, 'nat', '203')
            print('khadar 1')
            MB_Couch(NATHUAWALA_4_Zone_2Khadar_2, 'nat', '204')
            print('khadar 2')
            MB_Couch(NATHUAWALA_5_Zone_2DhobalChowk, 'nat', '205')
            print('Dobal_Chock')
            MB_Couch(NATHUAWALA_6_Zone_3BistAttaChakki, 'nat', '206')
            print('BistAttachakki')
            MB_Couch(NATHUAWALA_7_MadhavVihar, 'nat', '207')
            print('Madav vihar')
            print("\n")
            print("PRATITNAGAR")

            MB_Couch(PRATITNAGAR_1_Zone_1, 'pat', '301')
            print('Zone 1')
            MB_Couch(PRATITNAGAR_2_Zone_2, 'pat', '302')
            print('Zone 2')
            MB_Couch(PRATITNAGAR_3_Zone_3_I, 'pat', '303')
            print('Zone 3 I')
            MB_Couch(PRATITNAGAR_4_Zone_3_II, 'pat', '304')
            print('Zone 3 II')
            MB_Couch(PRATITNAGAR_5_Zone_4, 'pat', '305')
            print('Zone 4')
            MB_Couch(PRATITNAGAR_6_Zone_5, 'pat', '306')
            print('Zone 5')
            NAT_Zone_MB_Couch(Nat_Zone, 'zone', '102')
            print('NAT Zone wise data')
            KAH_Zone_MB_Couch(kah_Zone, 'zone', '101')
            print('kah Zone wise data')
            PAT_Zone_MB_Couch(Pat_Zone, 'zone', '103')
            print('Pat Zone wise data')
            print("\n")

            time.sleep(5)







        except Exception as e:
            print(e)
