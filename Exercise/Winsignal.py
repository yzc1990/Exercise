
# 为窗口添加信号

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class Winsignal(QWidget):
    button_clicked_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("为窗口添加信号")
        self.resize(300,200)

        btn = QPushButton("关闭",self)
        btn.clicked.connect(self.btn_clicked)
        self.button_clicked_signal.connect(self.btn_close)

    def btn_clicked(self):
        self.button_clicked_signal.emit()

    def btn_close(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Winsignal()
    example.show()
    sys.exit(app.exec_())