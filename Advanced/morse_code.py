# ChatGPT did the morse code dictionary for me :)
morse_code_dict = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '\'': '.----.', ':': '---...', ';': '-.-.-.', '!': '-.-.--', '-': '-....-', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', '+': '.-.-.', '=': '-...-', ' ': '/'
}

def string_to_morse(input_string):
    input_string = input_string.lower()
    morse_string = []
    
    for letter in input_string:
        if letter in morse_code_dict:
            morse_string.append(morse_code_dict[letter])
        else:
            pass
    
    return ' '.join(morse_string)

input_string = "Hello, World!"
print(f'Solution: {string_to_morse(input_string)}')
