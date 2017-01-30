import sys
from world import Map
from simulation import VacuumSimulation

def main():
    v = VacuumSimulation(width=2,
                         height=1,
                         do_steps=10)

    # Configuration 1
    v.reset()  # For good measure
    v.spawn_agent(0, 0)
    results = v.run()
    print(results)


if __name__ == "__main__":
    main()
