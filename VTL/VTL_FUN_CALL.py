from VTL_Modbus_fun import *
from time import sleep
import datetime
import time

while True:
    while True:
        try:

            now = datetime.datetime.now()
            min = now.minute

            MB_WRITE()
            print('Value Write')
            MB_Couch(ZONE3_SLAGE_FARM, 'vtlzone3', '101')
            print('ZONE3_SLAGE_FARM ')
            MB_Couch(ZONE3_JAL_NIGAM, 'vtlzone3', '102')
            print('ZONE3_JAL_NIGAM')
            MB_Couch(ZONE1_GDHAI_VALI_GALI, 'vtlzone1', '101')
            print('ZONE1_GDHAI VALI GALI')
            MB_Couch(ZONE1_MATRANCHAL, 'vtlzone1', '102')
            print('ZONE1_MATRANCHAL')
            MB_Couch(ZONE2_SIDHESWAR, 'vtlzone2', '101')
            print('ZONE2_SIDHESWAR')
            MB_Couch(ZONE2_GURUKUL_KANGRI_CAMPUS, 'vtlzone2', '102')
            print('ZONE2_GURUKUL_KANGRI_CAMPUS')
            MB_Couch(ZONE2_GATE_NO_6, 'vtlzone2', '103')
            print('ZONE2_GATE_NO_6')
            MB_Couch(ZONE2_GURUKUL_CAMPUS, 'vtlzone2', '104')
            print('ZONE2_GURUKUL_CAMPUS')
            MB_Couch(ZONE4_DR_AMBEDKAR_PARK, 'vtlzone4', '101')
            print('ZONE4_DR_AMBEDKAR_PARK')
            MB_Couch(ZONE4_RAMLEELA, 'vtlzone4', '102')
            print("ZONE4_ACHIVER_HOMES")
            MB_Couch(ZONE4_ACHIVER_HOMES, 'vtlzone4', '103')
            print("ZONE4_ACHIVER_HOMES")

            print("here")
            time.sleep(5)

        except Exception as e:
            print(e)










