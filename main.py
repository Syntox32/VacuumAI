import sys
from world import Map
from simulation import VacuumSimulation

NUM_SIMULATION = 1000

def main():
    v = VacuumSimulation(width=2,
                         height=1,
                         do_steps=1000)

    average_score = 0

    #D = Dirty
    #C = Clean
    #* = Agent spawn location

    # Configuration 1: C*,C
    for x in range(NUM_SIMULATION):
        v.reset()  # For good measure
        v.clean_dirt(0, 0)
        v.clean_dirt(1, 0)
        v.spawn_agent(0, 0)
        results = v.run()
        average_score += results["cells_cleaned"]

    average_score /= NUM_SIMULATION
    print("Configuration C*,C:", average_score)

    # Configuration 1: C,C*
    for x in range(NUM_SIMULATION):
        v.reset()  # For good measure
        v.clean_dirt(0, 0)
        v.clean_dirt(1, 0)
        v.spawn_agent(1, 0)
        results = v.run()
        average_score += results["cells_cleaned"]

    average_score /= NUM_SIMULATION
    print("Configuration C,C*:", average_score)

    # Configuration 1: D*,C
    for x in range(NUM_SIMULATION):
        v.reset()  # For good measure
        v.dirty_cell(0, 0)
        v.clean_dirt(1, 0)
        v.spawn_agent(0, 0)
        results = v.run()
        average_score += results["cells_cleaned"]

    average_score /= NUM_SIMULATION
    print("Configuration D*,C:", average_score)

    # Configuration 1: C*,C
    for x in range(NUM_SIMULATION):
        v.reset()  # For good measure
        v.dirty_cell(0, 0)
        v.clean_dirt(1, 0)
        v.spawn_agent(1, 0)
        results = v.run()
        average_score += results["cells_cleaned"]

    average_score /= NUM_SIMULATION
    print("Configuration D,C*:", average_score)

    # Configuration 1: C*,C
    for x in range(NUM_SIMULATION):
        v.reset()  # For good measure
        v.dirty_cell(0, 0)
        v.dirty_cell(1, 0)
        v.spawn_agent(0, 0)
        results = v.run()
        average_score += results["cells_cleaned"]

    average_score /= NUM_SIMULATION
    print("Configuration D*,D:", average_score)

    # Configuration 1: C*,C
    for x in range(NUM_SIMULATION):
        v.reset()  # For good measure
        v.dirty_cell(0, 0)
        v.dirty_cell(1, 0)
        v.spawn_agent(0, 0)
        results = v.run()
        average_score += results["cells_cleaned"]

    average_score /= NUM_SIMULATION
    print("Configuration D,D*:", average_score)

    # Configuration 1: C*,C
    for x in range(NUM_SIMULATION):
        v.reset()  # For good measure
        v.clean_dirt(0, 0)
        v.dirty_cell(1, 0)
        v.spawn_agent(0, 0)
        results = v.run()
        average_score += results["cells_cleaned"]

    average_score /= NUM_SIMULATION
    print("Configuration C*,D:", average_score)

    # Configuration 1: C*,C
    for x in range(NUM_SIMULATION):
        v.reset()  # For good measure
        v.clean_dirt(0, 0)
        v.dirty_cell(1, 0)
        v.spawn_agent(1, 0)
        results = v.run()
        average_score += results["cells_cleaned"]

    average_score /= NUM_SIMULATION
    print("Configuration C,D*:", average_score)

if __name__ == "__main__":
    main()
