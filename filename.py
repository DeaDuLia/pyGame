#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel
from PyQt5.QtGui import QPainter, QColor

import Game


class Window2(QWidget):
    def __init__(self, parent):
        super(Window2, self).__init__()
        self.parent = parent
        self.setFixedSize(300, 100)
        self.setWindowTitle('Настройка цвета')
        self.btn1 = QPushButton("Начать с набором цветов 1", self)
        self.btn2 = QPushButton("Начать с набором цветов 2", self)
        self.btn2.move(0, 50)
        self.btn1.clicked.connect(self.newStart)
        self.btn2.clicked.connect(self.newStart2)

    def newStart(self):
        self.parent.cube = Game.start('#130f0f', '#00cfcb', '#cf00b5', '#cf9300')
        self.parent.repaint()
        self.close()

    def newStart2(self):
        self.parent.cube = Game.start('#0fec00', '#ff6f00', '#aaaaaa', '#fffff')
        self.parent.repaint()
        self.close()


class Window1(QWidget):
    def __init__(self):
        super(Window1, self).__init__()
        self.setWindowTitle('Правила')
        self.lable = QLabel(self)
        self.setFixedSize(500, 150)
        self.lable.setText('1. Цель - собрать на 4-х крайних гранях по 4 одинаковых цвета. \n2. Кликайте на грани и центр кубика, чтобы крутить их\n3. Вы так же можете выбрать другую цветовую гамму\n(Осторожно, игра начинается сначала при применении настроек)')


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.setFixedSize(450, 450)
        self.btn1 = QPushButton("Настройка цвета", self)
        self.btn2 = QPushButton("Правила", self)
        self.btn2.move(150, 0)
        self.lable = QLabel(self)
        self.lable.setText('Вы победили!!!!')
        self.lable.move(155, 190)
        self.lable.setVisible(False)
        self.initUI()
        self.cube = Game.start()
        self.btn1.clicked.connect(self.show_window_2)
        self.btn2.clicked.connect(self.show_window_1)

    def initUI(self):

        self.setGeometry(300, 300, 800, 800)
        self.setWindowTitle('Colours')
        self.show()

    def show_window_2(self):
        self.w2 = Window2(self)
        self.w2.show()
        self.repaint()

    def show_window_1(self):
        self.w1 = Window1()
        self.w1.show()

    def buttonClicked(self):
        pass

    def mousePressEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()
        if y > 230 and y < 333 and x > 228 and x < 332:  # 1
            Game.twist_side(self.cube.side1)
            self.repaint()
        if y > 230 and y < 333 and x > 70 and x < 170:  # 2
            Game.twist_side(self.cube.side2)
            self.repaint()
        if y > 72 and y < 172 and x > 70 and x < 170: # 3
            Game.twist_side(self.cube.side3)
            self.repaint()
        if y > 72 and y < 172 and x > 228 and x < 332:  # 4
            Game.twist_side(self.cube.side4)
            self.repaint()
        if y > 150 and y < 250 and x > 150 and x < 250:  # 5
            Game.twist_mid(self.cube)
            self.repaint()
        if Game.check_sides(self.cube):
            self.lable.setVisible(True)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp, self.cube)
        qp.end()

    def drawRectangles(self, qp, cube):
        col = QColor(0, 0, 0)
        qp.drawEllipse(230, 230, 100, 100)
        qp.drawEllipse(70, 230, 100, 100)
        qp.drawEllipse(70, 70, 100, 100)
        qp.drawEllipse(230, 70, 100, 100)
        qp.drawEllipse(150, 150, 100, 100)
        col.setNamedColor(cube.side1.cell1.color)
        qp.setBrush(col)
        qp.drawRect(300, 300, 40, 40)
        col.setNamedColor(cube.side1.cell2.color)
        qp.setBrush(col)
        qp.drawRect(220, 300, 40, 40)
        col.setNamedColor(cube.side1.cell3.color)
        qp.setBrush(col)
        qp.drawRect(220, 220, 40, 40)
        col.setNamedColor(cube.side1.cell4.color)
        qp.setBrush(col)
        qp.drawRect(300, 220, 40, 40)

        col.setNamedColor(cube.side2.cell1.color)
        qp.setBrush(col)
        qp.drawRect(140, 300, 40, 40)
        col.setNamedColor(cube.side2.cell2.color)
        qp.setBrush(col)
        qp.drawRect(60, 300, 40, 40)
        col.setNamedColor(cube.side2.cell3.color)
        qp.setBrush(col)
        qp.drawRect(60, 220, 40, 40)
        col.setNamedColor(cube.side2.cell4.color)
        qp.setBrush(col)
        qp.drawRect(140, 220, 40, 40)

        col.setNamedColor(cube.side3.cell1.color)
        qp.setBrush(col)
        qp.drawRect(140, 140, 40, 40)
        col.setNamedColor(cube.side3.cell2.color)
        qp.setBrush(col)
        qp.drawRect(60, 140, 40, 40)
        col.setNamedColor(cube.side3.cell3.color)
        qp.setBrush(col)
        qp.drawRect(60, 60, 40, 40)
        col.setNamedColor(cube.side3.cell4.color)
        qp.setBrush(col)
        qp.drawRect(140, 60, 40, 40)

        col.setNamedColor(cube.side4.cell1.color)
        qp.setBrush(col)
        qp.drawRect(300, 140, 40, 40)
        col.setNamedColor(cube.side4.cell2.color)
        qp.setBrush(col)
        qp.drawRect(220, 140, 40, 40)
        col.setNamedColor(cube.side4.cell3.color)
        qp.setBrush(col)
        qp.drawRect(220, 60, 40, 40)
        col.setNamedColor(cube.side4.cell4.color)
        qp.setBrush(col)
        qp.drawRect(300, 60, 40, 40)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())