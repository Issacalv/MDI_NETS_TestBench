import serial
import time

def harvard_control(COM_PORT = None, BAUD_RATE = None):
    if COM_PORT is None:
        raise ValueError("COM not set")

    if BAUD_RATE is None:
        raise ValueError("BAUD_RATE not set")
    ser = serial.Serial(
    port=COM_PORT,
    baudrate=BAUD_RATE,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS,
    timeout=1
    )

    if ser.isOpen():
    print("Serial port opened successfully")

    
