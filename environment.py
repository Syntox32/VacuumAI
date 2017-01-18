from world import World


class Environment(World):
    '''
    How we're storing the environment for the agents and the simulation world.
    '''

    def __init__(self, width=0, height=0):
        super().__init__(width, height)
