
from time import sleep
from Report_Data import *
import datetime

while True:
    while True:

        try:
            sleep(10)
            now = datetime.datetime.now()
            min = now.minute
            if min != 0:
                Set_Flag = 0

            if now.minute == 18and now.second > 0 and Set_Flag != 1:


                Data_Sql(NAT_1_Zone_1GujarowaliOffice, 'NATHUAWALA', '1_Zone_1GujarowaliOffice')
                Data_Sql(NAT_2_Zone_1GaneshVihar, 'NATHUAWALA', '2_Zone_1GaneshVihar')
                Data_Sql(NAT_3_Zone_2Khadar_1, 'NATHUAWALA', '3_Zone_2Khadar_1')
                Data_Sql(NAT_4_Zone_2Khadar_2, 'NATHUAWALA', '4_Zone_2Khadar_2')
                Data_Sql(NAT_5_Zone_2DhobalChowk, 'NATHUAWALA', '5_Zone_2DhobalChowk')
                Data_Sql(NAT_6_Zone_3BistAttaChakki, 'NATHUAWALA', '6_Zone_3BistAttaChakki')
                Data_Sql(NAT_7_MadhavVihar, 'NATHUAWALA', '7_MadhavVihar')
                print('Nathuawala')

                Data_Sql(KAH_1_Office, 'KAHRAKMAFF', Station_Name[7])
                Data_Sql(KAH_2_GuljarFarm, 'KAHRAKMAFF', Station_Name[8])
                Data_Sql(KAH_3_ChopraFarm, 'KAHRAKMAFF', Station_Name[9])
                Data_Sql(KAH_4_Khadri, 'KAHRAKMAFF', Station_Name[10])
                print('Kharakmaf')

                Data_Sql(PRA_1_Zone_1, Division_Name[2], Station_Name[11])
                Data_Sql(PRA_2_Zone_2, Division_Name[2], Station_Name[12])
                Data_Sql(PRA_3_Zone_3_I, Division_Name[2], Station_Name[13])
                Data_Sql(PRA_4_Zone_3_II, Division_Name[2], Station_Name[14])
                Data_Sql(PRA_5_Zone_4, Division_Name[2], Station_Name[15])
                Data_Sql(PRA_6_Zone_5, Division_Name[2], Station_Name[16])
                print('Pratitnagar')
                sleep(60)

                print('Value to database')
                'Nathuawala'
                Pt_Sql(4000, 'NATHUAWALA', '1_Zone_1_PT_1')
                Pt_Sql(4004, 'NATHUAWALA', '2_Zone_1_PT_2')
                Pt_Sql(4002, 'NATHUAWALA', '3_Zone_2_PT_1')
                Pt_Sql(4006, 'NATHUAWALA', '4_Zone_2_PT_2')
                Pt_Sql(4014, 'NATHUAWALA', '5_Zone_3_PT_1')

                'Kharakmaf'
                Pt_Sql(4016, 'KAHRAKMAFF', '1 -Chopra Farm Zone-1')
                Pt_Sql(4018, 'KAHRAKMAFF', '2 -Gulzar Farm Zone-2 Sensor-1')
                Pt_Sql(4020, 'KAHRAKMAFF', '3 -Gulzar Farm Zone-2 Sensor-2')
                Pt_Sql(4022, 'KAHRAKMAFF', '4 -Khadri Zone3 sensor-1')
                Pt_Sql(4024, 'KAHRAKMAFF', '5 -Khadri Zone3 sensor-2')

                'Pratitnagar'
                Pt_Sql(4026, Division_Name[2], '1 -Zone_1')
                Pt_Sql(4028, Division_Name[2], '2 -Zone_2')
                Pt_Sql(4030, Division_Name[2], '3 -Zone_3')
                Pt_Sql(4032, Division_Name[2], '4 -Zone_4')
                Pt_Sql(4034, Division_Name[2], '5 -Zone_5')
                print('Value to database')
                Set_Flag = 1
                print(Set_Flag)
                Test_for_power()
                sleep(60)







        except Exception as e:
            print(e)
