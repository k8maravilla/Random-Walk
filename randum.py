'''
Project Name: Random Walk
Author: Kaleb Maravilla
Due Date: 04/21/2023
Course: CS1400-002

Put your description here, lessons learned here, and any other information someone using your
program would need to know to make it run.

I learned that nested foor loops can be very helpful. always choose your data structure and stick with it for the whole project.
'''
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
    rounded_min = round(min_distance, 1)
    return rounded_min

def find_coeffiecent_variance(distances):
    """takes a list of distances, finds the standard devation, then divides it by the mean"""
    standard_deviation = statistics.stdev(distances)
    the_mean = find_mean(distances)
    coe_var = standard_deviation / the_mean
    rounded_coe = round(coe_var, 1)
    return rounded_coe

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
            distance_list = distance(my_walks)

            # returns list of distances
            distance(my_walks)

            #returns the mean of list of distances
            mean = find_mean(distance_list)

            #returns the max
            maximum = find_max(distance_list)

            #returns the min
            minimum = find_min(distance_list)

            #return the CV
            coefficent = find_coeffiecent_variance(distance_list)

            answer_dict[walker][i] = my_walks
            print(f"{walker} random walk of {i} steps")
            print(f"Mean = {mean} CV = {coefficent}")
            print(f"Max = {maximum} Min = {minimum}")
    return answer_dict

def plot():
    """this function creates a visual of the simulate info"""
    trtl = turtle.Turtle()

    screen_size = turtle.Screen()

    trtl.speed(3)
    screen_size.setup(300, 400)

    plot_data = simulate([100], 50, 'all') 
    for walker in plot_data:
        if walker == "Pa":
            trtl.shape("circle")
            trtl.color("black")
            trtl.shapesize(.5, .5, .5)
            for index in plot_data[walker].items():
                for x_coord, y_coord in index[1]:
                    scaled_coords = (x_coord * 5, y_coord * 5)
                    trtl.penup()
                    trtl.setposition(scaled_coords)
                    trtl.pendown()
                    trtl.stamp()

        elif walker == "Mi-Ma":
            trtl.shape("square")
            trtl.color("green")
            trtl.shapesize(.5, .5, .5)
            for index in plot_data[walker].items():
                for x_coord, y_coord in index[1]:
                    scaled_coords = (x_coord * 5, y_coord * 5)
                    trtl.penup()
                    trtl.setposition(scaled_coords)
                    trtl.pendown()
                    trtl.stamp()

        elif walker == "Reg":
            trtl.shape("triangle")
            trtl.color("red")
            trtl.shapesize(.5, .5, .5)
            for index in plot_data[walker].items():
                for x_coord, y_coord in index[1]:
                    scaled_coords = (x_coord * 5, y_coord * 5)
                    trtl.penup()
                    trtl.setposition(scaled_coords)
                    trtl.pendown()
                    trtl.stamp()
    save_to_image() 

def main():
    """this is purely just for testing my data"""
    plot()
    turtle.mainloop()
if __name__ == "__main__":
    main()
