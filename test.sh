#!/bin/sh

io_test() {
    echo IO_TEST : $1
    arduino-cli compile --fqbn arduino:avr:mega:cpu=atmega2560 --build-properties build.extra_flags=-I/`pwd`/src $1
    arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:mega:cpu=atmega2560 $1
    poetry run pytest $1.py
}

poetry install -v
for dir_path in `\find ./test/IO -maxdepth 1 -mindepth 1 -type d`; do
    dir_name=`basename ${dir_path}`
    io_test ${dir_path}"/"${dir_name}
done