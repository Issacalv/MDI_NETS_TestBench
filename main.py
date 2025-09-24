from serial_connection import initialize_devices
from harvard_aparatus import harvard_control

def main():
    Harvard_Port = initialize_devices()
    harvard_control(Harvard_Port, BAUD_RATE = 115200)

main()

