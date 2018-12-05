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


#----------or-------- without using a datastructure-------

def is_unique(string):
  compare = ""
  
  for letter in string:
    if letter in compare:
      return False
    compare += letter
  return True

# result = is_unique("hello")
result = is_unique("abc")
print(result)
