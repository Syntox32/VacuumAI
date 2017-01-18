
from world import Actuator

class Agent:
    """
    Simple agent template.

    See more here:  https://i.milje.me/17-01/18aa5e2.png
    """

    def __init__(self, env):
        self.env = env


    def perceive(self, env):
        """
        Perceive the environment.

        :param env: Instance of Environment class.
        :return: An object describing the current state of the perceivable environment.
        """
        pass


    def determine_action(self, state, rule):
        """

        :param state:
        :param rule:
        :return: Actuator action
        """
        action = None
        return action


    def rule_match(self, state):
        """

        :param state:
        :return:
        """
        rule = None
        return rule


    def step(self):
        """
        Perform the different actions for the agent.
        This is not meant to be overriden.

        :return: void
        """
        perceived_state = self.perceive(self.env)
        rule = self.rule_match(perceived_state)
        action = self.determine_action(perceived_state, rule)

        self.post_step_callback()


    def post_step_callback(self):
        """
        Callback function meant to be overriden by classes that inherit it.

        :return: void
        """
        pass