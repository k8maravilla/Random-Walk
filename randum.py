import turtle
import statistics
import random

t = turtle.Turtle()

def Pa():
    '''randomly chooses which direction pa goes'''
    return random.choice([(0,1), (1,0), (0, -1), (-1, 0)])

def Mi_Ma():
    '''randomly chooses which direction Mi-Ma goes'''
    return random.choice([(0,1), (1,0), (0, -1), (0, -1), (-1, 0)])

def Reg():
    '''randomly chooses which direction reg goes'''
    return random.choice([(1,0), (-1, 0)])

def my_trials(length, name):
    x = 0
    y = 0

    for _ in range(length):
        x_coord, y_coord = name
        x += x_coord
        y += y_coord
    return (x, y)

def walks(walk_lengths, trials, walkers):
    """determines the large amount of trials that are being passed in to simulate"""
    return [my_trials(walk_lengths, walkers) for _ in range(trials)]

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
    print(my_trials(100, Pa()))

main()
#if __name__ == "__main__":
    #main()
