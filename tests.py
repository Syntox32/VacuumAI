# AI classes
from unittest import TestCase, main
from world import Map
from world import Cell


class TestMap(TestCase):
    def test_add_cell(self):
        m = Map()
        m.add_cell(0, 0)
        self.assertIsNotNone(m.cells[0])
        pass

    def test_get_cell(self):
        m = Map()
        m.add_cell(0, 1)
        m.add_cell(1, 1)

        self.assertIsNotNone(m.get_cell(0, 1))
        self.assertIsNone(m.get_cell(0, 0))

        self.assertIsNotNone(m.get_cell(1, 1))
        self.assertIsNone(m.get_cell(1, 0))


class TestCell(TestCase):
    def test_add_modifier(self):
        c = Cell(0, 0)
        c.add_modifier("hello", 15)
        self.assertIs(c.modifiers["hello"], 15)

    def test_contains_modifier(self):
        c = Cell(0, 0)
        c.add_modifier("hello", 15)

        self.assertIs(c.contains_modifier("hello"), True)
        self.assertIs(c.contains_modifier("not"), False)

if __name__ == "__main__":
    main()