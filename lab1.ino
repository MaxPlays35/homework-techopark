int leds = 4;
int count_leds = 0;
bool buttonWasUp[3] = {false, false, false};

void setup() {
  for(int i = 8; i < leds + 4; i++){
    pinMode(i, OUTPUT);
  }
  for(int i = 2; i <= 4; i++){
    pinMode(i, INPUT_PULLUP);
  }
  Serial.begin(9600);

}

void loop() {
  boolean buttonIsUp1 = digitalRead(2);
  if (buttonWasUp[0] && !buttonIsUp1) {
    if (count_leds > 0){
      count_leds -= 1;
     }
  }
  buttonWasUp[0] = buttonIsUp1;
  boolean buttonIsUp2 = digitalRead(3);
  if (buttonWasUp[1] && !buttonIsUp2) {
    count_leds = 0;
  }
  buttonWasUp[1] = buttonIsUp2;
  boolean buttonIsUp3 = digitalRead(4);
  if (buttonWasUp[2] && !buttonIsUp3) {
    if (count_leds < leds){
        count_leds += 1; 
     }
  }
  buttonWasUp[2] = buttonIsUp3;
  for(int i = 8; i < 8 + count_leds; i++){
    digitalWrite(i, HIGH); 
  }
  for(int i = 8 + leds - 1; i >= 8 + count_leds; i--){
    digitalWrite(i, LOW);
  }
  Serial.println(count_leds);
}
