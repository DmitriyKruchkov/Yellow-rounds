from PyQt5.QtWidgets import QPushButton, QMainWindow, QApplication
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
import random
import sys


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.button_rounds.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        r = random.randint(40, 300)
        qp.drawEllipse(random.randint(0, 500), random.randint(0, 300), r, r)

    def paint(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
