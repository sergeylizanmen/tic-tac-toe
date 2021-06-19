from PyQt6 import QtWidgets, QtGui
from interface import Ui_MainWindow


class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        """ Флаг для определения хода """
        self.x_move_flag = True

        """ Объект QButtonGroup для всех кнопок ходов """

        self.btn_grp = QtWidgets.QButtonGroup()

        self.btn_grp.setExclusive(True)
        self.btn_grp.addButton(self.pushButton)
        self.btn_grp.addButton(self.pushButton_2)
        self.btn_grp.addButton(self.pushButton_3)
        self.btn_grp.addButton(self.pushButton_4)
        self.btn_grp.addButton(self.pushButton_5)
        self.btn_grp.addButton(self.pushButton_6)
        self.btn_grp.addButton(self.pushButton_7)
        self.btn_grp.addButton(self.pushButton_8)
        self.btn_grp.addButton(self.pushButton_9)

        self.btn_grp.buttonClicked.connect(self.move)

        self.btnReset.clicked.connect(self.reset)

    def x_move(self, button):
        """ Функция для хода Х """
        if not self.check_winner():
            font = QtGui.QFont()
            font.setFamily('Calibri')
            font.setPointSize(36)
            font.setBold(True)
            button.setFont(font)
            button.setStyleSheet("background: rgb(0, 255, 255);\n"
                                 "color: #ff00ff;")
            button.setText('X')
            self.x_move_flag = False

        else:
            self.winner()

    def o_move(self, button):
        """ Функция для хода О """
        if not self.check_winner():
            font = QtGui.QFont()
            font.setFamily('Calibri')
            font.setPointSize(36)
            font.setBold(True)
            button.setFont(font)
            button.setStyleSheet("background: rgb(0, 255, 255);\n"
                                 "color: #0040ff;")
            button.setText('O')
            self.x_move_flag = True
        else:
            self.winner()

    def move(self, button):
        """ Функция для определения хода """
        if button.text() == '':
            if self.x_move_flag:
                self.x_move(button)
            else:
                self.o_move(button)

    def check_winner(self):
        """ Функция определяет есть ли победитель """
        symbols = [button.text() for button in self.btn_grp.buttons()]
        if symbols[0] == symbols[1] == symbols[2] != '' \
                or symbols[3] == symbols[4] == symbols[5] != '' \
                or symbols[6] == symbols[7] == symbols[8] != '' \
                or symbols[0] == symbols[4] == symbols[8] != '' \
                or symbols[2] == symbols[4] == symbols[6] != '' \
                or symbols[1] == symbols[4] == symbols[7] != '' \
                or symbols[0] == symbols[3] == symbols[6] != '' \
                or symbols[2] == symbols[5] == symbols[8] != '':
            return True
        return False

    def winner(self):
        """ Уведомление о победе """
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle('Конец игры')
        if not self.x_move_flag:
            msg.setText('Победил X')
        else:
            msg.setText('Победил O')
        msg.exec()
        self.reset()

    def reset(self):
        """ Очистка поля """
        self.x_move_flag = True
        for button in self.btn_grp.buttons():
            button.setText('')


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = Window()
    application.show()
    app.exec()
