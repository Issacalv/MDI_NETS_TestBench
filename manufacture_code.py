'''
Main Article:
https://support.harvardapparatus.com/hc/en-us/articles/1500007007721-Configuring-Syringe-Pumps-for-Automation-Controlling-pumps-from-a-PC

List of Commands:
https://support.datasci.com/hc/article_attachments/1500011159481/PHD_Ultra_user_Commands.pdf

Python Sample Code:
https://datasci.zendesk.com/hc/article_attachments/4426726873363/Python_serial_snippet.txt

'''
import serial
import time

ser = serial.Serial(
    port='COM4',
    baudrate=115200,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS,
    timeout=1
)

if ser.isOpen():
    print("Serial port opened successfully")

command = 'run'

ser.write((command + '\r\n').encode('ascii'))
print(f"Sent command: {command}")


try:
    while True:
        response = ser.readline().decode('ascii', errors='ignore').strip()
        if response:
            print("Pump response:", response)
    time.sleep(0.1)
    
except KeyboardInterrupt:
    print("Stopped by user")
    ser.close()
