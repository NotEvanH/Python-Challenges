'''
For this challenge, create a Python function that accepts a string. The function should return a string, with each lowercase character in the original string returned as uppercase characters. If you send the function “goodbye” as a parameter, it should return “GOODBYE”.
'''

def lower_to_upper(string):
    return string.upper()

print(f'Solution: {lower_to_upper("goodbye")}')