/* 
 Example using the SparkFun HX711 breakout board with a scale
 By: Nathan Seidle
 SparkFun Electronics
 Date: November 19th, 2014
 License: This code is public domain but you buy me a beer if you use this and we meet someday (Beerware license).

 This example demonstrates basic scale output. See the calibration sketch to get the calibration_factor for your
 specific load cell setup.

 This example code uses bogde's excellent library:"https://github.com/bogde/HX711"
 bogde's library is released under a GNU GENERAL PUBLIC LICENSE

 The HX711 does one thing well: read load cells. The breakout board is compatible with any wheat-stone bridge
 based load cell which should allow a user to measure everything from a few grams to tens of tons.
 Arduino pin 2 -> HX711 CLK
 3 -> DAT
 5V -> VCC
 GND -> GND

 The HX711 board can be powered from 2.7V to 5V so the Arduino 5V power should be fine.

*/

#include "HX711.h"
#include "NewPing.h"

#define calibration_factor -9340.0 //This value is obtained using the SparkFun_HX711_Calibration sketch
#define DOUT  3
#define CLK  2
// Hook up HC-SR04 with Trig to Arduino Pin 9, Echo to Arduino pin 10
#define TRIGGER_PIN 9
#define ECHO_PIN 10
// Maximum distance we want to ping for (in centimeters).
#define MAX_DISTANCE 50	
HX711 scale;

// NewPing setup of pins and maximum distance.
NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE);
float duration, distance;

void setup() {
  Serial.begin(9600);
  Serial.println("HX711 scale demo");

  scale.begin(DOUT, CLK);
  scale.set_scale(calibration_factor); //This value is obtained by using the SparkFun_HX711_Calibration sketch
  scale.tare(); //Assuming there is no weight on the scale at start up, reset the scale to 0

  // Serial.println("Readings:");
}

void loop() {
  Serial.print("Weight ");
  Serial.println(scale.get_units(), 1); //scale.get_units() returns a float
  // Serial.print(" lbs"); //You can change this to kg but you'll need to refactor the calibration_factor
  // Serial.println();

  // Send ping, get distance in cm
	distance = sonar.ping_cm();
	
	// Send results to Serial Monitor
	Serial.print("Distance ");
	
	if (distance >= 70 || distance <= 2) 
	{
		// Serial.println("Out of range");
	}
	else 
	{
		Serial.println(distance);
  //		Serial.println(" cm");
	}
	delay(100);
}
