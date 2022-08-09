
import random

from Cell import Cell
from Cube import Cube
from Side import Side


def start(color1='#ff0000', color2='#ebc103', color3='#188f00', color4='#0f00ec'):
    colors_list = [color1, color1, color1, color1, color2, color2, color2, color2, color3, color3, color3, color3, color4, color4, color4, color4]
    side1 = Side()
    side2 = Side()
    side3 = Side()
    side4 = Side()
    side5 = Side()
    cube = Cube(side1, side2, side3, side4, side5)
    set_colors_to_cube_sides(cube, colors_list)
    return cube


def set_colors_to_cube_sides(cube = Cube(), colors_list=None):
    if colors_list is None:
        colors_list = ['#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#ff0000', '#0f00ec', '#0f00ec', '#0f00ec', '#0f00ec', '#0f00ec', '#0f00ec', '#0f00ec', '#0f00ec']
    Cell1 = Cell(colors_list.pop(random.randint(0, len(colors_list ) -1)))
    Cell2 = Cell(colors_list.pop(random.randint(0, len(colors_list) - 1)))
    Cell3 = Cell(colors_list.pop(random.randint(0, len(colors_list) - 1)))
    Cell4 = Cell(colors_list.pop(random.randint(0, len(colors_list) - 1)))
    cube.side1 = Side(Cell1, Cell2, Cell3, Cell4)
    cube.side2 = Side(Cell(colors_list.pop(random.randint(0, len(colors_list) - 1))),
                      Cell(colors_list.pop(random.randint(0, len(colors_list) - 1))),
                      Cell(colors_list.pop(random.randint(0, len(colors_list) - 1))),
                      Cell(colors_list.pop(random.randint(0, len(colors_list) - 1))))
    cube.side3 = Side(Cell(colors_list.pop(random.randint(0, len(colors_list) - 1))),
                      Cell(colors_list.pop(random.randint(0, len(colors_list) - 1))),
                      Cell(colors_list.pop(random.randint(0, len(colors_list) - 1))),
                      Cell(colors_list.pop(random.randint(0, len(colors_list) - 1))))
    cube.side4 = Side(Cell(colors_list.pop(random.randint(0, len(colors_list) - 1))),
                      Cell(colors_list.pop(random.randint(0, len(colors_list) - 1))),
                      Cell(colors_list.pop(random.randint(0, len(colors_list) - 1))),
                      Cell(colors_list.pop(random.randint(0, len(colors_list) - 1))))
    cube.side5 = Side(cube.side1.cell4, cube.side2.cell4, cube.side3.cell4, cube.side4.cell4)


def check_sides(cube = Cube()):
    return check_side(cube.side1) and check_side(cube.side2) and check_side(cube.side3) and  check_side(cube.side4)


def check_side(side = Side()):
    return side.cell1.color == side.cell2.color and side.cell1.color == side.cell3.color and side.cell1.color == side.cell1.color == side.cell4.color


def twist_side(side):
    tmp_cell = side.cell1
    side.cell1 = side.cell2
    side.cell2 = side.cell3
    side.cell3 = side.cell4
    side.cell4 = tmp_cell

def twist_mid(cube):
    tmp_cell = cube.side1.cell3
    cube.side1.cell3 = cube.side2.cell4
    cube.side2.cell4 = cube.side3.cell1
    cube.side3.cell1 = cube.side4.cell2
    cube.side4.cell2 = tmp_cell
