'''
Create a function in Python that accepts two parameters. The first will be a list of numbers. The second parameter will be a string that can be one of the following values: asc, desc, and none.

If the second parameter is “asc,” then the function should return a list with the numbers in ascending order. If it's “desc,” then the list should be in descending order, and if it’s “none,” it should return the original list unaltered.
'''

def sort_a_list(list, instruction):
    newList = list

    if instruction == "none":
        return list
    elif instruction == "asc":
        newList.sort()
        return newList
    elif instruction == "desc":
        newList.sort(reverse = True)
        return newList
    else:
        return list
    
list = [2, 9, 1, 3, 5]

print(f'Ascending Order: {sort_a_list(list, "asc")}')
print(f'Descending Order: {sort_a_list(list, "desc")}')
print(f'Normal Order: {sort_a_list(list, "none")}')