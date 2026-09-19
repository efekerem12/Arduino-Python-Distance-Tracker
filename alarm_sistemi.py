import serial
import time
from PyQt5.QtCore import QThread, pyqtSignal

# Arduino'nun bağlı olduğu COM portunu ayarla (Örn: 'COM3' veya Linux/Mac için '/dev/ttyUSB0')
ARDUINO_PORT = 'COM3' 
BAUD_RATE = 9600

class AlarmThread(QThread):
     mesafe_sinyali = pyqtSignal(int)  # Mesafe değerini iletmek için sinyal
     durum_sinyali = pyqtSignal(str)  # Alarm durumunu iletmek için sinyal

     def __init__(self, port="COM3", baud_rate=9600):
          """Sınıfın başlatıcısı. Arduino ya baglanır ve gerekli ayarları yapar."""
          super().__init__()
          self.port = port
          self.baud_rate = baud_rate
          self.calisiyor_mu = True
          self.arduino = None
          

     def run(self):
          """Thread başlatıldığında otomatik çalışan ana döngü metodu."""
          try:
               self.arduino = serial.Serial(self.port, self.baud_rate, timeout=1)
               time.sleep(2)  # Arduino'nun başlatılması için kısa bir bekleme süresi
               self.durum_sinyali.emit("Bağlantı başarılı.")
          except serial.SerialException:
               self.durum_sinyali.emit("Bağlantı başarısız.")
               self.calisiyor_mu = False


          while self.calisiyor_mu:
               if self.arduino and self.arduino.in_waiting > 0:
                    try:
                         line = self.arduino.readline().decode('utf-8').strip()
                         if line.startswith("mesafe:"):
                              mesafe = int(line.split(":")[1])

                              if mesafe > 0 and mesafe < 400: 
                                   self.mesafe_sinyali.emit(mesafe)
                    except ValueError, IndexError:
                         pass
               self.msleep(50)  # CPU kullanımını azaltmak için kısa bir uyku süresi
               
     def durdur(self):
          self.calisiyor_mu = False
          if self.arduino and self.arduino.is_open:
               self.arduino.close()
          self.quit()
          self.wait()
               

 
               
        

 
             
                 
     
    


    