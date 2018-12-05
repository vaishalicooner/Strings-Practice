# write code to check if s2 is a rotation of s1.

def is_rotation(str1,str2):

    if (len(str1) == len(str2)) and str1 in str2*2:
        return True

result = is_rotation("sye", "yes")
print(result)