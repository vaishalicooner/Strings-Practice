#Given two strings, write a method to decide if one is a permutation of the other.

def is_permutation(str1, str2):

    count = {}
    for letter in str1:
        count[letter] = 1

    for letter in str2:
        if not letter in count:
            return False
        count[letter] -= 1

        if count[letter] == 0:
            del count[letter]

    if len(count) == 0:
        return True
    # return len(count) == 0

result = is_permutation("book", "kobo")
print(result)