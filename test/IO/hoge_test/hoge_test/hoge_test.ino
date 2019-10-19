#include "HelloWorld/hoge.hpp"

int outputPin = 9;

void test()
{
    int val = (int)((255 / 5) * 3.3);
    analog_write(outputPin, val);
}

void setup()
{
    // put your setup code here, to run once:
    pinMode(outputPin, OUTPUT); // ピンを出力に設定する
    Serial.begin(9600);         // 9600bpsでシリアルポートを開く
}

void loop()
{
    // put your main code here, to run repeatedly:
    if (!Serial.available())
        return;

    // 改行コード(10)を検出したら、そこまでの文字列を取得
    String input = Serial.readStringUntil('\n');
    Serial.flush();

    // 改行コードを取り除く
    input.trim();

    if (input == "RUN")
    {
        test();
        Serial.println("FIN");
    }
}
