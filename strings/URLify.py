# Write a method to replace all spaces in a string with '%20'.

def replace(string):

    str = ""
    for word in string:
        if word == " ":
            str += "%20"
        else:
            str += word
    return str

result = replace("hello how are you?")
print(result)