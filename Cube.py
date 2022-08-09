from Side import Side


class Cube:
    def __init__(self, side1 = Side(), side2 = Side(), side3 = Side(), side4 = Side(), side5 = Side()):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4
        self.side5 = Side(side1.cell3, side2.cell4, side3.cell1, side4.cell2)
