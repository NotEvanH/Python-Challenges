'''
Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent “4444444444444444”, then it should return “4444”.
'''

def hide_numbers(numbers):
    return ("*" * (len(numbers) - 4)) + numbers[-4:]

credit_card_number = "4444444444444444"
print(f'Solution: {hide_numbers(credit_card_number)}')