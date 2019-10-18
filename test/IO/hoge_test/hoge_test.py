from serial.tools import list_ports
import serial
import sys

# use pytest

import RPi.GPIO as GPIO  #GPIOにアクセスするライブラリをimportします。 

GPIO.setmode(GPIO.BCM)  #GPIOへアクセスする番号をBCMの番号で指定することを宣言します。                                           
GPIO.setup(2,GPIO.IN)   #BCM 2番ピンを入力に設定します。 

def select_serial_port():
    ports = list_ports.comports()

    devices = []
    for info in ports:
        print(info.device)
        print(info.description)
        devices.append(info.device)

    if len(devices) == 0:
        print("Device not found.")
        sys.exit(0)

    elif len(devices) == 1:
        port_num = 0

    else:
        for i in range(len(devices)):
            print("input " + str(i)+":\topen "+devices[i])
        
        print("input number of Serial com Port\n>> ",end="")
        port_num = int(input())

    return devices[port_num]

def test_analog_output():

    serial = serial.Serial(port=select_serial_port() ,baudrate=9600, timeout=10)
    
    serial.write("RUN".encode("utf-8"))
    assert str(serial.readline()) == "FIN"

    assert GPIO.input(2) == GPIO.LOW


