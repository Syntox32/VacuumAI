import sys
from world import Map
from simulation import VacuumSimulation

def main():

    v = VacuumSimulation(width=2, height=1, do_steps=10)
    results = v.run()



if __name__ == "__main__":
    main()
