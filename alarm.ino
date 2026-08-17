const int TRIG_PIN = 4;
const int ECHO_PIN = 5;
const int BUZZER_PIN = 10;
const int SIRENM_PIN = 11;
const int SIRENK_PIN = 12;
const int BUTTON_PIN = 6;

bool alarmAktif = false;

void setup() {
Serial.begin(9600);
pinMode(TRIG_PIN, OUTPUT); 
pinMode(ECHO_PIN, INPUT);
pinMode(BUZZER_PIN, OUTPUT);
pinMode(SIRENM_PIN, OUTPUT);
pinMode(SIRENK_PIN, OUTPUT);
pinMode(SIRENK_PIN, INPUT_PULLUP);

}

void loop() {
digitalWrite(TRIG_PIN, LOW);
delayMicroseconds(2);
digitalWrite(TRIG_PIN, HIGH);
delayMicroseconds(10);
digitalWrite(TRIG_PIN, LOW);

long duration = pulseIn(ECHO_PIN, HIGH);
long distance = duration * 0.034 / 2;

Serial.print("mesafe: ");
Serial.println(distance);



if (distance > 0 && distance < 20) {
    tone(BUZZER_PIN, 1000);
    digitalWrite(SIRENM_PIN, HIGH);
    digitalWrite(SIRENK_PIN, LOW);
    delay(100);
    digitalWrite(SIRENM_PIN, LOW);
    digitalWrite(SIRENK_PIN, HIGH);
    delay(100);
    
}
  
  else {
    noTone(BUZZER_PIN); 
    digitalWrite(SIRENK_PIN, LOW);
    digitalWrite(SIRENK_PIN, LOW);
  }
 
}


   









