#define voltage_generator 5
#define equivalent_resistor 12.5

int pinOut = 10;
static bool circuit_on = false;

void circuit_on_off() {
  
  if(circuit_on){
    digitalWrite(pinOut, LOW);
    circuit_on = false;
  }else{
    digitalWrite(pinOut, HIGH);
    circuit_on = true;
  }
}

void setup() {
  Serial.begin(9600);
  pinMode(A0, OUTPUT);
  pinMode(A1, INPUT);
  pinMode(pinOut, OUTPUT);
}

// the loop routine runs over and over again forever:
void loop() {

  int sensorValue = analogRead(A2)-analogRead(A3);
  //Serial.println(sensorValue);
  //analogWrite(A0, sensorValue);

  // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
  float voltage = sensorValue * (5.0 / 1023.0);
  Serial.print("voltage: ");
  Serial.println(voltage);
  int voltage2 = 255 * voltage / 5;
  //Serial.println(voltage2);
  Serial.write(voltage2);
  
  delay(5000);
  circuit_on_off();
}