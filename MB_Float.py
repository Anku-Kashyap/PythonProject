import struct
from pyModbusTCP.client import ModbusClient
from datetime import *

def Float_Val(a,b):
    # Read two 16-bit Modbus registers as integers
    register1 = a  # Replace with your actual register value
    register2 =  b# Replace with your actual register value

    # Combine the two registers into a 32-bit integer (Little Endian)
    combined_value = (register2 << 16) | register1

    # Convert the 32-bit integer to a float using struct
    val = struct.unpack('<f', struct.pack('<i', combined_value))[0]

    # Now, float_value contains the floating-point value from the Modbus registers
    print("Floating-Point Value:", val)
    return(val)
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 1502

# Create a Modbus TCP client
client = ModbusClient()

# Set the Modbus server host and port
client.host = SERVER_HOST
client.port = SERVER_PORT
Val=[0]
for i in range(9019, 9021):
        value=(client.read_holding_registers(i-1,2))
        Val.append(value[0])







