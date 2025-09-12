from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


app = QApplication([])

window = QWidget()
window.setWindowTitle('Пустое окно')
window.resize(300, 300)
window.setWindowIcon(QIcon('icon.png'))

# https://www.w3schools.com/colors/colors_names.asp

app.setStyleSheet("""
    QWidget {
        background: LightSteelBlue;
        color: LightSlateGrey;
        font-family: Helvetica;
        font-size: 16px;
    }
""")

window.show()
app.exec_()
