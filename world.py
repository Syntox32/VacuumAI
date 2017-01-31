
from agent import Agent
import random


class World:
    """
    """

    def __init__(self, width: int, height: int):
        """
        :param width:
        :param height:
        """
        self.map = Map()

        # Init map with dimensions
        for w in range(width):
            for h in range(height):
                self.map.add_cell(w, h)

        for cell in self.map.cells:
            if not cell.dirty:
                cell.dirty = random.randint(1, 4) is 4

    def clean_cell_under(self, agent: Agent):
        self.map[agent.x][agent.y].dirty = False

    def get_cell_for(self, agent: Agent):
        return self.map[agent.x][agent.y]

    def clean_cell(self, x, y):
        if self.map[x][y] is not None:
            self.map[x][y].dirty = False

    def dirty_cell(self, x, y):
        if self.map[x][y] is not None:
            self.map[x][y].dirty = True

    def step(self):
        for cell in self.map.cells:
            if not cell.dirty:
                cell.dirty = random.randint(1, 4) is 4


class Map:
    """
    A map of the environment
    """

    def __init__(self):
        self.y_offset = 0
        self.cells = []

    def add_cell(self, x: int, y: int):
        """
        Adds a cell to the map
        """
        c = Cell(x, y)
        self.cells.append(c)

        self.y_offset = min(self.y_offset, y)

    def get_cell(self, x: int, y: int):
        return self[x][y]

    def __getitem__(self, idx):
        """
        Get a cell by index.

        can be used like:

            map = Map()
            map.add_cell(0, 1)
            cell = map[0][1]

        :param idx: index of the elemnet you wish to get.
        :return:
        """
        if not isinstance(idx, int):
            raise TypeError("Item cannot be of other type than 'int'")

        return CellColumn([c for c in self.cells if c.x == idx], self.y_offset)


class CellColumn:

    def __init__(self, cells: [], index_offset: int):
        """
        :param cells: A list of the cells
        :param index_offset: The y position of the first index
        """
        self.column = cells
        self.offset = index_offset

    def __getitem__(self, idx):
        """
        Get a cell by position.

        can be used like:

            cell_row = CellRow(cells)
            cell = cell_row[5]

        :param idx: index of the element you wish to get.
        :return:
        """
        if len(self.column) is 0:
            return None

        if not isinstance(idx, int):
            raise TypeError("Item cannot be of other type than 'int'")

        return next((c for c in self.column if c.y + self.offset == idx), None)


class Cell:
    """
    A single cell in the world
    """
    x = 0
    y = 0
    dirty = False

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Perceiver:
    """
    An abstract perceiver class from which perceivers can inherit from.
    """

    def perceive(self, environ: Map):
        """
        Perceives the environment

        :param environ: A map instance that the perceiver is supposed to perceive from.
        :return: An object describing what the perceiver perceived.
        """
        pass


class Actuator:
    """
    An abstract class from which actuators can inherit from.
    """

    def actuate(self, cell):
        """
        Performs an action on the cell in question

        :param cell: The cell that the action is performed on
        :return: The altered cell
        """
        pass
