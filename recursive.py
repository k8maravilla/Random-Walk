
#lab challenge -----------------------------------
#def recursive_power(base, exp):
#    if exp == 0:
#        return 1
#    else:
#        return base * recursive_power(base, exp -1)
    
#print(recursive_power(5, 3))

#lab challenge 3 --------------------------------

def bunny_ears(integer):
    """counts number of bunny ears"""
    double_integer = integer + integer
    for i in range(double_integer):
        if i == 0:
            return 0
        else:
            i += 2 -1
    return i
print(bunny_ears(0))