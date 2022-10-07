import sys

from PyQt5.QtWidgets import (QApplication, QDialog, QGridLayout, QLineEdit,
                             QMainWindow, QPushButton, QSizePolicy, QWidget)


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.setFixedSize(400, 400)
        self.setWindowTitle('Calculadora - Gabriel')

        self.add_button(QPushButton('7'), 1, 0, 1, 1)
        self.add_button(QPushButton('8'), 1, 1, 1, 1)
        self.add_button(QPushButton('9'), 1, 2, 1, 1)
        self.add_button(QPushButton('C'), 1, 3, 1, 1,
                        lambda: self.display.setText(''),
                        'background: #CC0033; font-size: 30px;')
        self.add_button(QPushButton('<-'), 1, 4, 1, 1,
                        func=lambda: self.display.setText(self.display.text()[:-1]))
        self.add_button(QPushButton('4'), 2, 0, 1, 1)
        self.add_button(QPushButton('5'), 2, 1, 1, 1)
        self.add_button(QPushButton('6'), 2, 2, 1, 1)
        self.add_button(QPushButton('+'), 2, 3, 1, 1)
        self.add_button(QPushButton('-'), 2, 4, 1, 1)
        self.add_button(QPushButton('1'), 3, 0, 1, 1)
        self.add_button(QPushButton('2'), 3, 1, 1, 1)
        self.add_button(QPushButton('3'), 3, 2, 1, 1)
        self.add_button(QPushButton('*'), 3, 3, 1, 1)
        self.add_button(QPushButton('/'), 3, 4, 1, 1)
        self.add_button(QPushButton(','), 4, 0, 1, 1)
        self.add_button(QPushButton('0'), 4, 1, 1, 1)
        self.add_button(QPushButton('.'), 4, 2, 1, 1)
        self.add_button(QPushButton('='), 4, 3, 1, 2,
                        self.igual,
                        'background: #43CD80; font-size: 30px;')

        self.display = QLineEdit()
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            '* {background: white; color: #000; font-size: 30px;}')
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.setCentralWidget(self.cw)

    def add_button(self, btn, row, column, rowspan, columnspan, func=None, style=None):
        self.grid.addWidget(btn, row, column, rowspan, columnspan)
        btn.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Expanding
        )
        btn.setStyleSheet('font-size: 30px;')

        if style:
            btn.setStyleSheet(style)

        if not func:
            btn.clicked.connect(lambda:
                                self.display.setText(
                                    self.display.text() + btn.text()
                                )
                                )
        else:
            btn.clicked.connect(func)

    def igual(self):
        try:
            self.display.setText(str(eval(self.display.text())))
        except:
            self.display.setText('Valor Inválido.')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = Calculadora()
    app.show()
    qt.exec_()
