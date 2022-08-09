from PyQt5.QtWidgets import QWidget


class rules(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 800)
        self.setWindowTitle('Colours')
        self.show()