# check if one word is a substring of another.

def is_substring(str1, str2):

    if str1 in str2:
        return True

result = is_substring("hello", "hello how are you?")
# result = is_substring("hello", "how are you?")
print(result)