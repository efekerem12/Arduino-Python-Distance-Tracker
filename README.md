# 📡 Arduino & Python (PyQt5) Distance Tracker (v3.0)

![Project Status](https://img.shields.io/badge/Status-v3.0--GUI-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)
![Python](https://img.shields.io/badge/Python-3.x-yellow)
![Arduino](https://img.shields.io/badge/Arduino-Uno-00979D)

An end-to-end embedded and desktop system that performs real-time distance measurements using an **HC-SR04 Ultrasonic Sensor** on an **Arduino Uno**, sending telemetry data over **PySerial** to a custom **PyQt5** GUI application.

---

## 📸 Demo & Screenshots

> *Arayüzünün ekran görüntüsünü projenin içine `assets/gui-demo.png` adıyla kaydedip aşağıdaki bağlantıyı aktifleştirebilirsin.*

![PyQt5 Dashboard](assets/gui-demo.png)

---

## ✨ Features (Özellikler)

* **Real-time Proximity Monitoring:** Live distance telemetry updated directly from hardware over Serial USB interface at 9600 baud rate.
* **Dynamic Alert Thresholds:** Visual alerts and dynamic color switching (Green -> Red) when proximity drops below **20 cm**.
* **Audio & Visual Hardware Triggers:** Automatic buzzer tone generation and flashing LED sequence during alert states.
* **Modern GUI Dashboard:** Built with PyQt5 and dark-themed styling for high scannability and low footprint.

---

## 🛠️ Tech Stack & Hardware Components

### Hardware
* **Microcontroller:** Arduino Uno R3
* **Sensor:** HC-SR04 Ultrasonic Distance Sensor
* **Actuators:** Buzzer, LED (5mm)
* **Prototyping:** Breadboard & Jumper Wires

### Software & Libraries
* **Embedded Code:** C++ (Arduino Framework)
* **Desktop Application:** Python 3.x
* **GUI Framework:** PyQt5
* **Serial Communication:** PySerial
* **Version Control:** Git, GitKraken, GitHub

---

## 📐 Circuit & Working Logic

1. **HC-SR04** measures the distance continuously via ultrasonic echo reflection timing ($d = \frac{t \times 0.034}{2}$).
2. Distance data formatted as `DISTANCE:<value>` is streamed over USB Serial.
3. **Arduino Logic:** If distance is within $0 < d < 20 \text{ cm}$, buzzer activates and LED flashes.
4. **Python Logic:** PySerial parses the stream, updates the PyQt5 label/progress bar, and switches interface alert modes in real-time.

---

## 🚀 Getting Started (Kurulum)

### 1. Hardware Setup
Flash the Arduino code provided in `alarm.ino` to your Arduino Uno using Arduino IDE.

```cpp
// Pin Wiring Reference
TRIG_PIN -> Pin 9
ECHO_PIN -> Pin 8
BUZZER   -> Pin 11
LED      -> Pin 13
