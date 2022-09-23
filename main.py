#!/usr/bin/env python3
# coding=utf-8

import sys

from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


# Основной класс программы
class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('main.ui', self)  # Загрузка формы из файла

        # Задание заголовка окна
        self.setWindowTitle('Создание простейшей визуальной '
                            'программы на Python')

        # Привязываем к кнопкам наши процедуры-обработчики
        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_exit.clicked.connect(self.close)

    # Процедура решения примера
    def solve(self):
        try:
            a = float(self.lineEdit_a.text())
            b = float(self.lineEdit_b.text())
            x = float(self.lineEdit_x.text())
            if x >= 4:
                answer = (10 * (x + a * a))/(b + a)
            else:
                answer = 5 * (x + a * a + b)

            self.label_answer.setStyleSheet("QLabel{color: green}")
            self.label_answer.setText('Ответ: ' + str(format(answer, '.2f')))
        except:
            self.label_answer.setStyleSheet("QLabel{color: red}")
            self.label_answer.setText(
                'Ошибка!')

    # Процедура очистки данных
    def clear(self):
        self.lineEdit_a.setText('')
        self.lineEdit_b.setText('')
        self.lineEdit_x.setText('')
        self.label_answer.setText('Ответ: ')


# Основная часть программы
app = QApplication(sys.argv)
window = Main()  # базовый класс окна
window.show()  # отобразить окно на экране
sys.exit(app.exec_())  # запуск основного цикла приложения
