'''
Create a function in Python that accepts a single word and returns the number of vowels in that word. In this function, only a, e, i, o, and u will be counted as vowels — not y.
'''

def vowels_in_a_string(string):
    vowels = "aeiou"
    vowel_count = 0
    for letter in string:
        if letter in vowels:
            vowel_count += 1

    return vowel_count

string = "hello, how are you?"
print(f'Solution: {vowels_in_a_string(string)}')