'''
Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.

The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.
'''

def get_discount(full_price, discount_percentage):
    return full_price * (discount_percentage / 100)

print(f'Solution: {get_discount(100, 20)}')