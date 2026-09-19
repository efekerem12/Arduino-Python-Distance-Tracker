import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from alarm_sistemi import AlarmThread

class AnaArayuz(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

        self.arduino_thread = AlarmThread(port='COM3')

        self.arduino_thread.mesafe_sinyali.connect(self.mesafe_guncelle)
        self.arduino_thread.durum_sinyali.connect(self.durum_guncelle)

        self.arduino_thread.start() # bu kod AlarmThread sınıfının run() metodunu otomatik olarak başlatır özel bir koddur.

    def init_ui(self):
        """Pencere ve arayüz elemanlarının tasarımı."""
        self.setWindowTitle("Arduino Mesafe Takip Sistemi")
        self.setGeometry(100, 100, 400, 200)

        self.durum_etiketi = QLabel("Bağlanıyor...", self)
        self.mesafe_etiketi = QLabel("Mesafe: -- cm", self)

        self.mesafe_etiketi.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.mesafe_etiketi.setAlignment(Qt.AlignCenter)
        self.durum_etiketi.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.durum_etiketi)
        layout.addWidget(self.mesafe_etiketi)

        merkezi_widget = QWidget()
        merkezi_widget.setLayout(layout)
        self.setCentralWidget(merkezi_widget)

    def mesafe_guncelle(self, gelen_mesafe):
        """Arduino'dan her yeni veri geldiğinde tetiklenen metot."""
        # ARTIK VERİ TAMAMEN ELİNDE, İSTEDİĞİN GİBİ KULLAN

        self.mesafe_etiketi.setText(f"Mesafe: {gelen_mesafe} cm")

        if gelen_mesafe < 20: # mesafeye göre arayüzün rengi değişiyor.
            self.mesafe_etiketi.setStyleSheet("font-size: 24px; font-weight: bold; color: red;")
            

        else:
            self.mesafe_etiketi.setStyleSheet("font-size: 24px; font-weight: bold; color: green;")

    def durum_guncelle(self, durum_mesaji):
        """Arduino bağlantı durumu değiştiğinde tetiklenen metot."""
        self.durum_etiketi.setText(f"Sistem Durumu: {durum_mesaji}")

    def closeEvent(self, event):
        """Pencere kapatıldığında arka plandaki thread'i de güvenle kapatır."""
        self.arduino_thread.durdur()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = AnaArayuz()
    pencere.show()
    sys.exit(app.exec_())