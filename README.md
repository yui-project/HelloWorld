[![Build Status](http://sat-dev.kz.tsukuba.ac.jp/jenkins/job/HelloWorld/job/master/badge/icon)](http://sat-dev.kz.tsukuba.ac.jp/jenkins/job/HelloWorld/job/master/)

# Arduino CLi
How to Setup

## Downloading file
```
$ wget http://downloads.arduino.cc/arduino-cli/arduino-cli-0.2.1-alpha.preview-linuxarm.tar.bz2
$ tar xf arduino-cli*
$ mv arduino-cli-0.2.1-alpha.preview-linuxarm arduino-cli
$ sudo mv arduino-cli /usr/local/bin
```
## Creating sketch
```
$ arduino-cli sketch new Test
Sketch created in: /home/pi/Arduino/Test
```
## Configuration
```
$ mkdir /home/pi/.arduino15/
$ arduino-cli core update-index
(うまくいかなかったら、package_log.json を手動でダウンロード)
$ arduino-cli core install arduino:avr
pi@raspberrypi:~/Arduino/Test$ arduino-cli board list
FQBN                    Port            ID              Board Name              
arduino:avr:mega        /dev/ttyACM0    2341:0042       Arduino/Genuino Mega or Mega 2560
```
## Compile
```
pi@raspberrypi:~/Arduino$ arduino-cli compile --fqbn arduino:avr:mega:cpu=atmega2560  Test
(注意：Arduinoディレクトリで実行すること　、Testフォルダが入ってるフォルダ）
```
## Upload
```
pi@raspberrypi:~/Arduino$ arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:mega:cpu=atmega2560 Test
```

