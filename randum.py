import turtle
import statistics
import random
import math

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

def distance(end_points):
    """converts walk points to distance length"""
    distance_list = []
    for x, y in end_points:
        total = (x **2 + y ** 2)
        my_distance = math.sqrt(total)
        distance_list.append(my_distance)
    #returns a list of floats
    return distance_list

def find_mean(distances):
    """takes a list of distances, adds them all up, divides that number by the length to give the mean"""
    distance_mean = statistics.mean(distances)
    final_answer = round(distance_mean, 1)
    return final_answer

def find_max(distances):
    """finds the maximum distance in the list of distances"""
    max_distance = max(distances)
    rounded_max = round(max_distance, 1)
    return rounded_max

def find_min(distances):
    """finds the minimum distance in the list of distances"""
    min_distance = min(distances)
    print(round(min_distance, 1))

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
            # returns list of distances
            distance(my_walks)
            #returns the mean of list of distances
            find_mean(distance(my_walks))
            #returns the max
            find_max(distance(my_walks))
            #returns the min
            find_min(distance(my_walks))
            #return the CV
            
            answer_dict[walker][i] = my_walks
            print(my_walks)

    print(answer_dict)

def plot():
    """this function creates a visual of the simulate info"""
    pass
    #simulate()

def main():
    #simulate()
    #print(walks(100, 50, "Pa"))
    simulate([10, 15], 3, "all")



if __name__ == "__main__":
    main()
