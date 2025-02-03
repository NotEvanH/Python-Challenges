'''
Write a function in Python that accepts one numeric parameter. This parameter will be the measure of an angle in radians. The function should convert the radians into degrees and then return that value.

While you might find a Python library to do this for you, you should write the function yourself. One hint you get is that you’ll need to use Pi in order to solve this problem. You can import the value for Pi from Python's math module.
'''

import math

# Solution 1

def radians_into_degrees(radians):
    return math.degrees(radians)

# Solution 2

def radians_into_degrees_two(radians):
    return radians * (180 / math.pi)

radians = 1

print(f'Solution 1: {radians_into_degrees(radians)}')
print(f'Solution 2: {radians_into_degrees_two(radians)}')