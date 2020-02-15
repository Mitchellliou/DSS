void setup() {
  Serial.begin(9600);
}

void loop () {
  for (int i = 0; i< 1000; i++) {
    Serial.write("Goddamn it MItchell");
    delay(50);
  }
}
