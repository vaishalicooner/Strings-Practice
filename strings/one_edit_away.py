# Given two strings, write a function to check if they are one edit (or zero edits) away.

def one_edit(w1, w2):

    if abs(len(w1) - len(w2)) > 1:
        return False

    if len(w2) > len(w1):
        w1, w2 = w2, w1

    wrong = 0
    
    i = j = 0

    while j < len(w2):
        if w1[i] != w2[j]:
            wrong += 1
            if wrong > 1:
                return False

            i += 1
            if len(w1) == len(w2):
                j += 1

        else:
            i += 1
            j += 1

    return True


result = one_edit("pale", "pal")
# result = one_edit("hello", "hel")
print(result)