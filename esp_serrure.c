String msg;
#define POWER 4

void setup() {
  pinMode(POWER, OUTPUT);
  Serial.begin(115200);

}

void loop() {
   readSerialPort();
   //digitalWrite(POWER, HIGH);
   //delay(1000);
   //digitalWrite(POWER, LOW);
   //delay(1000);


}


void readSerialPort() {
  msg = "";
  if (Serial.available()) {
    delay(10);
    while (Serial.available() > 0) {
      msg += (char)Serial.read();
      //Serial.println(msg);
      if (msg == "ok") {
          digitalWrite(4, HIGH);
          delay(1000);
          digitalWrite(4, LOW);

      } else {
          digitalWrite(4, LOW);

      }
    }
    Serial.flush();
  }
}
