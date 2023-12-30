from OP_Modbus_fun import *
from time import sleep
import datetime

while True:
    while True:
            try:

                    now = datetime.datetime.now()
                    min = now.minute

                    MB_WRITE()
                    MB_Couch(Gauri_Talab, 'opzone2', '101')
                    print('Gauri_Talab ')
                    MB_Couch(Anganwadi, 'opzone2', '102')
                    print('Anganwadi')
                    """MB_Couch(TW_BLOCK, 'tpzone1', '101')
                    print('TW_ZONE')
                    MB_Couch(Near_Deep_public_School, 'tpzone1', '102')
                    print('Near_deep_Public_School')
                    MB_Couch(Mokshdham, 'tpzone2', '101')
                    print('Mokshdham')
                    MB_Couch(Along_NHAI, 'tpzone2', '102')
                    print('Along_Nhai')
                    print("here\n")"""
                    print(now)
                    time.sleep(5)

            except Exception as e:
                    print(e)










