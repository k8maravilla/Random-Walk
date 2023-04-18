import turtle
import statistics
import random

t = turtle.Turtle()

def pa_walker():
    '''randomly chooses which direction pa goes'''
    return random.choice([(0,1), (1,0), (0, -1), (-1, 0)])

def mi_ma_walker():
    '''randomly chooses which direction Mi-Ma goes'''
    return random.choice([(0,1), (1,0), (0, -1), (0, -1), (-1, 0)])

def reg_walker():
    '''randomly chooses which direction reg goes'''
    return random.choice([(1,0), (-1, 0)])

def simulate(walk_lengths, trials, walkers):
    """This function should simuate parameters and print a summary"""
    all_walkers = []
    if walkers == "all":
        all_walkers = ['Pa', 'Mi-Ma', 'reg']
    else:
        all_walkers.append(walkers)

        
def plot():
    """this function creates a visual of the simulate info"""
    pass

def main():
    #simulate()
    reg_walker()
main()
if __name__ == "__main__":
    main()
