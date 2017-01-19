import sys
from world import Map
from simulation import VacuumSimulation

def main():
    print(sys.version)

    s = VacuumSimulation(test=10)
    print(s.test)  # "10"
    s.register_agent(None)
    s.register_world(None)
    s.run()


if __name__ == "__main__":
    main()
