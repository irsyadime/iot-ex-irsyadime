const int sensorPin = A0;
const int ledPin = 13;
unsigned long previousMillis = 0
const long interval = 60000;


void setup() {
  pinMode(sensorPin,INPUT);
  pinMode(ledPin,OUTPUT);
  Serial.begin(9600)

}

void loop() {
  unsigned long currentMillis = millis();

  if(currentMillis - previousMillis >= interval){
    previousMillis = currentMillis;
    send_data();
  }

}

void send_data(){
  int sensorValue = analogRead(sensorPin);
  String dataToString = String(sensorValue);
  Serial.println(dataToString);

  digitalWrite(ledPin,HIGH);
  delay(100);
  digitalWrite(ledPin,LOW);
}
