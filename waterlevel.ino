int Liquid_level = 0;

void setup() {
  // put your setup code here, to run once:
   Serial.begin(9600);
   pinMode(5,INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  Liquid_level = digitalRead(5);
  Serial.print("Liquid_level = ");
  Serial.println(Liquid_level,DEC);
  delay(500);
}
