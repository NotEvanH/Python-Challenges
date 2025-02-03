'''
Write a function in Python that accepts a decimal number and returns the equivalent binary number. To make this simple, the decimal number will always be less than 1,024, so the binary number returned will always be less than ten digits long.
'''

def decimal_to_binary(decimal):
    if decimal >= 1024:
        return "Please use a number less than 1024"
    
    return bin(decimal).replace("0b", "")

print(f'Solution: {decimal_to_binary(1000)}')