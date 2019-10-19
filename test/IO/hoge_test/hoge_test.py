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
    # https://www.ingenious.jp/raspberry-pi/2019/03/gpio-uart/
    # デフォルトで存在するUART0を除去する
    for info in ports:
        print(info.device)
        print(info.description)
        if info.description == 'ttyAMA0':
            print("remove UART0")
        else:
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

    arduino_serial = serial.Serial(port=select_serial_port() ,baudrate=9600, timeout=10)
    
    arduino_serial.write("RUN".encode("utf-8"))
    assert str(arduino_serial.readline()) == "FIN"

    assert GPIO.input(2) == GPIO.HIGH


