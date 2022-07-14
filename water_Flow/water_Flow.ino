#include <WiFi.h>
#include <HTTPClient.h>
#include <SPI.h>
#include <Wire.h>
 
String sensorId = "1"; // Enter your Write API key from ThingSpeak
const char *ssid = "TECNO SPARK 5 Pro";     // replace with your wifi ssid and wpa2 key
const char *password = "josh@2021";

 const char* serverName = "http://192.168.43.178:8080/sensor/update-sensor";
#define LED_BUILTIN 16
#define SENSOR  2
 
long currentMillis = 0;
long previousMillis = 0;
int interval = 1000;
float calibrationFactor = 4.5;
volatile byte pulseCount;
byte pulse1Sec = 0;
float flowRate;
unsigned long flowMilliLitres;
unsigned int totalMilliLitres;
float flowLitres;
float totalLitres;
char sensorReading[120];
 
void IRAM_ATTR pulseCounter()
{
  pulseCount++;
}
 

 
void setup()
{
  Serial.begin(115200);

  pinMode(SENSOR, INPUT_PULLUP);
 
  pulseCount = 0;
  flowRate = 0.0;
  flowMilliLitres = 0;
  totalMilliLitres = 0;
  previousMillis = 0;
 
  attachInterrupt(digitalPinToInterrupt(SENSOR), pulseCounter, FALLING);
 

  WiFi.begin(ssid, password);
  Serial.println("Connecting");
  while(WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to WiFi network with IP Address: ");
  Serial.println(WiFi.localIP());
 
  Serial.println("Timer set to 5 seconds (timerDelay variable), it will take 5 seconds before publishing the first reading.");
}
 
void loop()
{
  currentMillis = millis();
  if (currentMillis - previousMillis > interval) 
  {
    
    pulse1Sec = pulseCount;
    pulseCount = 0;
 
    // Because this loop may not complete in exactly 1 second intervals we calculate
    // the number of milliseconds that have passed since the last execution and use
    // that to scale the output. We also apply the calibrationFactor to scale the output
    // based on the number of pulses per second per units of measure (litres/minute in
    // this case) coming from the sensor.
    flowRate = ((1000.0 / (millis() - previousMillis)) * pulse1Sec) / calibrationFactor;
    previousMillis = millis();
 
    // Divide the flow rate in litres/minute by 60 to determine how many litres have
    // passed through the sensor in this 1 second interval, then multiply by 1000 to
    // convert to millilitres.
    flowMilliLitres = (flowRate / 60) * 1000;
    flowLitres = (flowRate / 60);
 
    // Add the millilitres passed in this second to the cumulative total
    totalMilliLitres += flowMilliLitres;
    totalLitres += flowLitres;
    
    // Print the flow rate for this second in litres / minute
    Serial.print("Flow rate: ");
    Serial.print(float(flowRate));  // Print the integer part of the variable
    Serial.print("L/min");
    Serial.print("\t");       // Print tab space
 

 
    // Print the cumulative total of litres flowed since starting
    Serial.print("Output Liquid Quantity: ");
    Serial.print(totalMilliLitres);
    Serial.print("mL / ");
    Serial.print(totalLitres);
    Serial.println("L");
 
  }
 
    delay(1000);
  
      //Check WiFi connection status
    if(WiFi.status()== WL_CONNECTED){
      WiFiClient client;
      HTTPClient http;
    
      // Your Domain name with URL path or IP address with path
      http.begin(client,serverName);
      // If you need an HTTP request with a content type: application/json, use the following:
      http.addHeader("Content-Type", "application/json");
      http.addHeader("accept", "application/json");
      if (float(flowRate)> 0 && totalLitres > 0){
      String sensorValues = "{ \"sensorId\": \"" + String(sensorId)  + "\", \"waterFlowRate\" : \"" + String(float(flowRate)) + "\" , \"volume\" : \"" + String(totalLitres) + "\"}";
      sensorValues.toCharArray(sensorReading, (sensorValues.length() + 1));

      int httpResponseCode = http.POST(sensorReading);
      if ( httpResponseCode > 0){
      String response = http.getString();
      Serial.print("HTTP Response code: ");
      Serial.println(httpResponseCode);
      Serial.println(response);
      }
      else {
         Serial.print("Error Occured while sending Data: ");
         Serial.println(httpResponseCode);
        }
      }
      
      // Free resources
     http.end();
    }
    else {
      Serial.println("WiFi Disconnected");
    } 
}
