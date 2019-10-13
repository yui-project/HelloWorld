#include "hoge.hpp"

int outputPin = 9;
int LED = 13;

void setup() {
    // put your setup code here, to run once:
    pinMode(outputPin, OUTPUT);   // ピンを出力に設定する
    pinMode(LED, OUTPUT);
}

void loop() {
    // put your main code here, to run repeatedly:
    int val = (int)((254 / 5) * 3.3);
    //analogWrite(outputPin, 3.3);  // analogReadの値は0から1023まで，analogWriteの値は0から255まで
    analog_write(outputPin, val);
    digitalWrite(LED,HIGH);
}
