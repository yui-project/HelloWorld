#!/bin/sh

arduino-cli lib install ArduinoUnit

cd src/

echo "cd src/"

arduino-cli compile --fqbn arduino:avr:mega:cpu=atmega2560  HelloWorld

arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:mega:cpu=atmega2560 HelloWorld