def lbs_to_kg(weight):
    return weight * 0.45

def kg_to_lbs(weight):
    return weight / 0.45

def metres_to_cm(length):
    return length * 100

def cm_to_metres(length):
    return length / 100

def find_max(numbers):
    max = 0
    for number in numbers:
        if number > max:
            max = number
    return max