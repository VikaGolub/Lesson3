'''
Codewars: Will you make it?
'''
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if fuel_left * mpg >= distance_to_pump:
        print("You wil get to the pump!")
        return True
    else:
        print("Not this time!")
        return False
