'''
Complete the homework by changing the code where noted.

'''

import sys 
sys.path.append('aima-python')
from agents import *

loc_C = (2,0)

class P5:

    def problem_a(self):
        '''
        Call the run() method with the reflex agent and the trivial vac environment 
        and return the environment status
        '''
        # TODO: Write this method!
        return None

    def problem_b(self):
        '''
        Call the run() method with the model based agent and the trivial vac environment
        and return the environment status
        '''
        # TODO: Write this method!
        return None 

    def problem_c(self):
        '''
        Call the run() method with the random agent and the trivial vac environment
        and return the environment status
        '''
        # TODO: Write this method!
        return None 

    def problem_d(self):
        '''
        Compare the performance of the reflex agent, the model based agent, and random agent in the trivial vac environment.
        You will have to pass the agents and the environment to the comparison function, 
        this will require reviewing the documentation because the process is a little different.
        '''
        # TODO: Write this method!
        return None


class LessTrivialVacuumEnvironment(Environment):
    """A simple vacuum environment with 3 locations, A, B and C.
    Each can be dirty or clean.
    Look at TrivialVacuumEnvironment for guidance
    """
    def __init__(self):
        super().__init__()
        self.status = {loc_A: random.choice(['Clean','Dirty']),
                       loc_B: random.choice(['Clean','Dirty']),
                       loc_C: random.choice(['Clean','Dirty'])}

    def thing_classes(self):
        return [Wall, Dirt, RandomVacuumAgent]

    def percept(self, agent):
        """Returns the agent's location, and the location status (Dirty/Clean)."""
        return agent.location, self.status[agent.location]

    def execute_action(self, agent, action):
        """Change agent's location and/or location's status, track performance.
        Score 10 for each dirt cleaned, -1 for each move."""
        # TODO: Write this method!

    def default_location(self, thing):
        """Agents start in either location at random."""
        return random.choice([loc_A, loc_B, loc_C])


def problem6():
    """Write code that will perform 100 runs of a RandomVacuumAgent in a 
    LessTrivialVacuumEnvironment for 20 timesteps and calculate the 
    average performance of those Agents. Return the average performance.
    """
    # TODO: Write this function!

def main():
    ps1p5 = P5()
    print("Problem 5a:", ps1p5.problem_a())
    print("Problem 5b:", ps1p5.problem_b())
    print("Problem 5c:", ps1p5.problem_c())
    print("Problem 5d:", ps1p5.problem_d())
    print("Problem 6:", problem6())

if __name__ == '__main__':
    main()
