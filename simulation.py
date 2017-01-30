from world import World
from agent import Agent

class VacuumSimulation:
    """
    """

    def __init__(self, **kwargs):
        """
        :param test:
        """
        self.width = kwargs.pop("width", 1)
        self.height = kwargs.pop("height", 2)
        self.do_steps = kwargs.pop("do_steps", 10)

        self.world = World(self.width, self.height)
        self.agent = Agent()

        self.cells_cleaned = 0
        self.steps_taken = 0
        self.agent_score = 0

    def reset(self):
        self.cells_cleaned = 0
        self.steps_taken = 0
        self.agent_score = 0

    def spawn_agent(self, x=0, y=0):
        self.agent.set_pos(x, y)

    def run(self):
        """
        :return: A dictionary with the simulation parameters
        """

        for i in range(self.do_steps):
            action = self.agent.step(self.world.get_cell_for(self.agent))
            self.world.step()
            if action == Agent.CLEAN:
                self.world.clean_cell_under(self.agent)
                self.cells_cleaned += 1
            elif action == Agent.MOVE_L:
                self.agent.x -= 1
            elif action == Agent.MOVE_R:
                self.agent.x += 1
            elif action == Agent.NOOP:
                pass
            self.steps_taken += 1

        return {
            "cells_cleaned": self.cells_cleaned,
            "steps_taken": self.steps_taken,
            "do_steps": self.do_steps
        }
