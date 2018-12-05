# Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3


def compress(string):

    if len(string) == 0:
        return string

    compressed = []
    current = string[0]
    count = 1

    for letter in string[1:]:
        if current == letter:
            count += 1
        else:
            compressed.append(current + str(count))
            current = letter
            count = 1

    compressed.append(current + str(count))

    result = "".join(compressed)
    return result
    
a = compress("aabcccccaaa")
print(a)