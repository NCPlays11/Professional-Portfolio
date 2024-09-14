morse_code_rules = {
    "a": "·−",
    "b": "−···",
    "c": "−·−·",
    "d": "−··",
    "e": "·",
    "f": "··−·",
    "g": "−−·",
    "h": "····",
    "i": "··",
    "j": "·−−−",
    "k": "−·−",
    "l": "·−··",
    "m": "−−",
    "n": "−·",
    "o": "−−−",
    "p": "·−−·",
    "q": "−−·−",
    "r": "·−·",
    "s": "···",
    "t": "−",
    "u": "··−",
    "v": "···−",
    "w": "·−−",
    "x": "−··−",
    "y": "−·−−",
    "z": "−−··",
    "0": "−−−−−",
    "1": "·−−−−",
    "2": "··−−−",
    "3": "···−−",
    "4": "····−",
    "5": "·····",
    "6": "−····",
    "7": "−−···",
    "8": "−−−··",
    "9": "−−−−·",
    " ": "/"
}

text = input("Enter the text you want to convert into morse code: ")
output_list = []

def converter():
    for letter in text:
        letter = letter.lower()
        output_list.append(morse_code_rules[letter])

converter()

morse_code = " ".join(output_list)

print(f'The morse code of "{text}" is "{morse_code}"')