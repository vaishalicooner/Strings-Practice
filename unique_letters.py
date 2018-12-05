# Implement an algorithm to determine if a string has all unique characters.

def unique(string):

    letters = {}
    for letter in string:
        if letter in letters:
            return False
        letters[letter] = True

    return True

# result = unique("hello")
result = unique("how")
print(result)