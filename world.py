
class World:
    width = 0
    height = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

class Map:

    def __init__(self, width, height):
        """
        :param width:
        :param height:
        """
        self.rows = []

        for h in range(height):
            temp = [Cell(w, h) for w in range(width)]
            self.rows.append(temp)


    def __getitem__(self, idx):
        """
        Get a cell by index.

        can be used like:

            map = Map(10, 10)
            cell = map[0][1]

        :param idx: index of the elemnet you wish to get.
        :return:
        """
        if not isinstance(idx, int):
            raise TypeError("Item cannot be of other type than 'int'")
        elif idx < 0 or idx >= len(self.cells):
            raise IndexError("Index out of range.")

        return self.rows[idx]


class Cell:
    """
    A single cell in the world
    """
    x = 0
    y = 0
    modifiers = {}

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def add_modifier(self, name, value):
        """
        Adds a modifier with name and value to the Cell.
        :param name: The name of the modifier
        :param value: The value of the modifier
        :return: None
        """
        self.modifiers[name] = value

    def contains_modifier(self, name):
        """
        Checks if the cell contains a modifier.
        :param name: The name of the modifier
        :return: A bool if the cell contains the modifier or not
        """
        return name in self.modifiers


class Perceiver:
    """
    An abstract perceiver class from which perceivers can inherit from.
    """

    def perceive(self, environ):
        """
        Perceives the environment

        :param environ: An environment instance that the perceiver is supposed to perceive from.
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