![WhatsApp Image 2025-08-10 at 16 49 23_8f195401](https://github.com/user-attachments/assets/b6bab872-d00e-4252-8f75-2d376e722338)

![Screenshot 2025-08-14 184208](https://github.com/user-attachments/assets/e2c4320e-9f3f-48bc-92dc-72f49e1dd7ae)

# 🌦 Weather Monitoring System
Here's a Weather monitoring system that takes the reading from the surrounding environment and you can fetch the data remotely from the weather station. This Whole Project is an internship project with Anedya IOT Cloud and whole monitoring is done in the Grafana Observability and Monitoring
A **remote weather monitoring system** that collects real-time environmental data using various sensors, sends it to the **Anedya IoT Cloud** via a **Python REST API**, and visualizes it using **Grafana**.  
This system helps monitor temperature, humidity, atmospheric pressure, soil moisture, and UV index from anywhere in the world.

---

## 📌 Features
- 🌡 **Real-time temperature & humidity monitoring** using DHT11/DHT22
- 📉 **Atmospheric pressure measurement** with BMP180
- 🌱 **Soil moisture detection** for agriculture & gardening
- 🌞 **UV index sensing** to monitor harmful UV radiation
- 🖥 **0.96" OLED display** for live readings
- ☁ **Cloud storage & visualization** using Anedya API & Grafana
- 🌍 **Remote access** to sensor data from anywhere

---

## 🛠 Technologies Used
- **Python REST API** – for sending & fetching data from the cloud
- **Anedya IoT Cloud API** – for device data storage and retrieval
- **Grafana** – for real-time data visualization
- **NodeMCU ESP8266** – as the main microcontroller for sensors
- **DHT11/DHT22, BMP180, Soil Moisture, UV Index sensor, OLED** – for data acquisition

---

## 🧩 System Architecture
```mermaid
flowchart LR
    S1[DHT11/DHT22] --> MCU(NodeMCU ESP8266)
    S2[BMP180] --> MCU
    S3[Soil Moisture Sensor] --> MCU
    S4[UV Index Sensor] --> MCU
    MCU -->|Wi-Fi| API[Python REST API]
    API -->|HTTP POST| Cloud[Anedya IoT Cloud]
    Cloud --> Grafana[Grafana Dashboard]
    MCU --> OLED["0.96 inch" OLED Display]

🔧 Hardware Components
1️⃣ DHT11 / DHT22 Sensor
Function: Measures temperature and humidity.
How it works:
Uses a capacitive humidity sensor and a thermistor to detect humidity and temperature.
The capacitive humidity sensor changes its capacitance based on moisture in the air.
The thermistor changes resistance based on temperature.
An internal chip converts these readings into digital signals for the microcontroller.

2️⃣ BMP180 (Barometric Pressure Sensor)
Function: Measures atmospheric pressure and can also estimate altitude.
How it works:
Contains a piezo-resistive pressure sensor that deforms under atmospheric pressure.
This deformation changes the resistance of the sensor material.
The built-in ADC (Analog-to-Digital Converter) converts this into a pressure value, which can be used to calculate altitude.

3️⃣ Soil Moisture Sensor
Function: Detects the water content in soil.
How it works:
Two conductive probes are inserted into the soil.
Water in the soil allows better electrical conductivity.
The sensor measures resistance between the probes — more water = lower resistance.
An onboard circuit outputs this as an analog or digital signal for the microcontroller.

4️⃣ UV Index Sensor
Function: Measures UV radiation levels to determine UV index.
How it works:
Uses a photodiode that reacts to UV light.
The photodiode generates a small electrical current when UV rays strike it.
An internal IC converts this current into a voltage signal.
The microcontroller reads this voltage and calculates the UV index.

5️⃣ 0.96" OLED Display
Function: Displays live weather data.
How it works:
OLED pixels emit their own light when current passes through organic compounds.
No backlight needed — results in high contrast and low power consumption.
Controlled via I²C interface with the NodeMCU.

⚙ Microcontroller – NodeMCU ESP8266
Function: Main controller that reads sensor data, processes it, and sends it to the cloud.
Advantages:
Built-in Wi-Fi for IoT applications
Low power consumption
Compact & affordable
Supports multiple communication protocols (I²C, SPI, UART)

Applications:
IoT devices
Smart home automation
Wireless sensor networks
Remote monitoring systems

📊 Data Flow
Sensors collect weather data.
NodeMCU ESP8266 reads and processes sensor data.
Data is sent via Wi-Fi to the Python REST API.
API sends data to Anedya IoT Cloud.
Grafana fetches and visualizes the data for remote monitoring.
