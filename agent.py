
class Perceive:

    def __init__(self, left, right, dirty):
        self.left = left
        self.right = right
        self.dirty = dirty

class Agent:
    CLEAN = 0
    MOVE_L = 1
    MOVE_R = 2
    NOOP = 3

    """
    Simple agent template.

    See more here:  https://i.milje.me/17-01/18aa5e2.png
    """

    def __init__(self):
        self.x = 0
        self.y = 0

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def perceive(self, cell):
        """
        Perceive the environment. For this perceive function it is expected that the environment is 2 cells wide
        and 1 cell high with the first cell at (0,0) and the second cell at (1,0)

        :param cell: The cell the agent is currently on.
        :return: Returns if the cell the agent is on is dirty
        """
        if cell.x is 0 and cell.dirty is True:
            return Perceive(True, False, True)

        elif cell.x is 0 and cell.dirty is False:
            return Perceive(True, False, False)

        elif cell.x is 1 and cell.dirty is True:
            return Perceive(False, True, True)

        elif cell.x is 1 and cell.dirty is False:
            return Perceive(False, True, False)

        return None

    def determine_action(self, state):
        """

        :param state: The state of the perceived cell/world
        :return: Agent action
        """

        if state is None:
            return Agent.NOOP

        if state.dirty:
            return Agent.CLEAN
        if state.right:
            return Agent.MOVE_L
        if state.left:
            return Agent.MOVE_R

        return Agent.NOOP

    def step(self, cell):
        """
        Perform the different actions for the agent.

        :return: Agent action
        """
        perceived_state = self.perceive(cell)
        return self.determine_action(perceived_state)
