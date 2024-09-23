import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

#membuat aplikasi 
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Aplikasi PyQt")

# menambahan tombol keluar 
exit_button = QPushButton('Keluar', window)
exit_button.clicked.connect(QApplication.quit)
exit_button.resize(100, 30)
exit_button.move(50,50)

#menampilkan jendela
window.setGeometry(100, 100, 200, 100)
window.show()

#menjalankan aplikasi 
sys.exit(app.exec_())