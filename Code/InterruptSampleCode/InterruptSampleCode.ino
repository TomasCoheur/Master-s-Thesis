const int interruptPin = 2;  // Pin connected to trigger the interrupt

// Variable to store the last time the LED was toggled
unsigned long previousMillis = 0;

// Interval at which to toggle the LED (milliseconds)
const long interval = 60000;  // 1000 milliseconds = 1 second

void setup() {
  pinMode(interruptPin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(interruptPin), interruptFunction, CHANGE);
}

void loop() {
  // Get the current time
  unsigned long currentMillis = millis();

  // Check if the specified interval has passed
  if (currentMillis - previousMillis >= interval) {
    // Save the current time for the next iteration
    previousMillis = currentMillis;

    // Toggle the interrupt
    digitalWrite(interruptPin, !digitalRead(interruptPin));
  }
}

void interruptFunction() {
  // Code to execute when the interrupt occurs
}
