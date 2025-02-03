'''
Write a function in Python that accepts a list of any length that contains a mix of non-negative integers and strings. The function should return a list with only the integers in the original list in the same order.
'''

def remove_strings(lst):
    return [item for item in lst if isinstance(item, int)]

lst = [1, 2, "s", 8, 6, 10, "hi", "hello"]
print(f'Solution: {remove_strings(lst)}')