import serial
import time

# Arduino'nun bağlı olduğu COM portunu ayarla (Örn: 'COM3' veya Linux/Mac için '/dev/ttyUSB0')
ARDUINO_PORT = 'COM3' 
BAUD_RATE = 9600



    
try:
     arduino = serial.Serial(ARDUINO_PORT, BAUD_RATE, timeout=1)
     time.sleep(2) # Arduino'nun reset atması için bekleme süresi
     print("Arduino ile bağlantı kuruldu!")

except serial.SerialException:
     print(f"Hata: {ARDUINO_PORT} portuna bağlanılamadı. Port numarasını kontrol et!")

while True:
         # Arduino'dan gelen mesafe verisini oku
     if arduino.in_waiting > 0:
        line = arduino.readline().decode('utf-8').strip()
        if line.startswith("mesafe:"):
            mesafe = line.split(":")[1]
            print(f"\rAnlık Oda/Mesafe Durumu: {mesafe} cm", end="") 
             
                 

    


    