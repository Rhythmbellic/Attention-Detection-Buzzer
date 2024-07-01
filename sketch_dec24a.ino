int ledPin = 4;      // Connect LED to digital pin 4
int buzzerPin = 5;   // Connect buzzer to digital pin 5

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();

    if (command == '1') {
      digitalWrite(ledPin, HIGH);  // Turn on LED
      digitalWrite(buzzerPin, LOW);  // Turn off Buzzer
    } else if (command == '2') {
      digitalWrite(ledPin, LOW);  // Turn off LED
      digitalWrite(buzzerPin, HIGH);  // Turn on Buzzer
    } else if (command == '0') {
      digitalWrite(ledPin, LOW);  // Turn off LED
      digitalWrite(buzzerPin, LOW);  // Turn off Buzzer
    }
  }
}
