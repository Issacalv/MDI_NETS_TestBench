import serial
import serial.tools.list_ports
from variables import *


def scan_COMports(HARDWARE_ID = None, MANUFACTURE_NAME = None, port_name = None):
    ports = serial.tools.list_ports.comports()

    for port in ports:
        if str(port.device) == str(port_name):
            print(f"COM port located at {port.device}")
            return port.device
        elif str(port.hwid) == str(HARDWARE_ID):
            print(f"COM port located at {port.device}")
            # print(f"  Port: {port.device}")
            # print(f"  Description: {port.description}")
            # print(f"  Hardware ID: {port.hwid}")
            # print("-" * 20)
            return port.device
        elif str(MANUFACTURE_NAME) in str(port.description):
            print(f"COM port located at {port.device}")
            return port.device

    raise OSError(f"""\
Could not locate the machine on any available COM port.

Troubleshooting steps:
1. Ensure the device is properly connected via USB/Serial cable.
2. Verify that the correct drivers are installed for your operating system.
3. Double-check that the expected COM port is visible in your system’s device manager.
4. If using `port_name`, confirm it matches exactly (e.g., 'COM3' on Windows). call with scan_COMports(port_name = "COM2")
5. If using hardware ID or manufacturer name, confirm those constants are correct in the "variables.py" file.
6. Try disconnecting and reconnecting the device, then rerun this program.

Current variables (Atleast one needs to be populated):
MANUFACTURE_NAME = {MANUFACTURE_NAME}
HARDWARE_ID = {HARDWARE_ID}
port_name = {port_name}
""")


def initialize_devices():
    Harvard_Port = scan_COMports(HARDWARE_ID = HARVARD_APARATUS_HARDWARE_ID, MANUFACTURE_NAME = HARVARD_APARATUS_DESCRIPTION)
    print(f"Harvard Aparatus Port: {Harvard_Port}")
    
    
    return Harvard_Port


