'''
Write a function in Python that accepts a string. The function should return a string and add “.” in between each letter. For example, if you send the function “skills” as a parameter, it should return “s.k.i.l.l.s”.
'''

def add_dots(word):
    return ".".join(word)

print(add_dots("skills"))