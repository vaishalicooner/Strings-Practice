# Given a string, write a function to check if it is a permutation of a palindrome.


def is_palindrome(string):

    count = set()

    for letter in string.lower():
        if not letter.isalpha():
            continue
        if letter in count:
            count.remove(letter)
        else:
            count.add(letter)

    return len(count) <=1 


# result = is_palindrome("hello")
result = is_palindrome("aab")
print(result)


# def is_palindrome(string):

#     counter = {}

#     for letter in string:
#         counter[letter] +=1

#     odd_count = 0
#     for count in counter.values():
#         odd_count += count%2

#         if odd_count > 1:
#             return False

#     return True

# result = is_palindrome("aab")
# # result = is_palindrome("hello")
# print(result)