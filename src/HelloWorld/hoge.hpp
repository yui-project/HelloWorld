#ifndef HOGE_HPP_
#define HOGE_HPP_

#include <Arduino.h>

void analog_write(int pin, int value) {
    analogWrite(pin, value);  // analogReadの値は0から1023まで，analogWriteの値は0から255まで
}

#endif /* HOGE_HPP_ */