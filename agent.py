
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
        pass

    def perceive(self, cell):
        """
        Perceive the environment.

        :param cell: The cell the agent is currently on.
        :return: Returns if the cell the agent is on is dirty
        """
        return cell.dirty

    def determine_action(self, state):
        """

        :param state:
        :param rule:
        :return: Actuator action
        """

        if state is True:
            return Agent.CLEAN

        return Agent.NOOP

    def step(self, cell):
        """
        Perform the different actions for the agent.
        This is not meant to be overriden.

        :return: void
        """
        perceived_state = self.perceive(cell)
        return self.determine_action(perceived_state)
