from TP_Modbus_fun import *
from time import sleep
import datetime

while True:
    while True:
            try:

                    now = datetime.datetime.now()
                    min = now.minute

                    MB_WRITE()
                    MB_Couch(police_station, 'tpzone3', '101')
                    print('police_station ')
                    MB_Couch(Dream_City, 'tpzone3', '102')
                    print('Dream City')
                    MB_Couch(TW_BLOCK, 'tpzone1', '101')
                    print('TW_ZONE')
                    MB_Couch(Near_Deep_public_School, 'tpzone1', '102')
                    print('Near_deep_Public_School')
                    MB_Couch(Mokshdham, 'tpzone2', '101')
                    print('Mokshdham')
                    MB_Couch(Along_NHAI, 'tpzone2', '102')
                    print('Along_Nhai')
                    print("here\n")
                    print(now)
                    time.sleep(5)

            except Exception as e:
                    print(e)










