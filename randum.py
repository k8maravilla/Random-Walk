import turtle
import statistics
import random

t = turtle.Turtle()

def pa():
    '''randomly chooses which direction pa goes'''
    return random.choice([(0,1), (1,0), (0, -1), (-1, 0)])

def mi_ma():
    '''randomly chooses which direction Mi-Ma goes'''
    return random.choice([(0,1), (1,0), (0, -1), (0, -1), (-1, 0)])

def reg():
    '''randomly chooses which direction reg goes'''
    return random.choice([(1,0), (-1, 0)])

def my_trials(length, name):
    """gives endpoint for one trial"""
    my_dict = {
        "Pa": pa,
        "Mi-Ma":mi_ma,
        "Reg":reg
    }
    x = 0
    y = 0

    for _ in range(length):
        x_coord, y_coord = my_dict[name]()
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
        all_walkers = ['Pa', 'Mi-Ma', 'Reg']
    else:
        all_walkers.append(walkers)

    answer_dict = {}

    for walker in all_walkers:
        answer_dict[walker] = {}
        for i in walk_lengths:
            my_walks = walks(i, trials, walker)
            answer_dict[walker][i] = my_walks
    print(answer_dict)
    
    

        
def plot():
    """this function creates a visual of the simulate info"""
    pass
    #simulate()

def main():
    #simulate()
    #print(walks(100, 50, "Pa"))
    simulate([10, 15], 5, "all")


if __name__ == "__main__":
    main()
