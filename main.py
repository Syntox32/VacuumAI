import sys
from environment import Environment
from world import Cell


def main():
    print(sys.version)
    environment = Environment(0, 0)
    cell = Cell()
    cell.add_modifier("hello", 2)

if __name__ == "__main__":
    main()
