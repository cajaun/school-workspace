VOWELS = ["a", "e", "i", "o", "u"]
PUNCTUATION = [",", ".", ";", ":", "?" , "!"]

def count_vowels(word):
  
  count = 0
  for letter in word:
        if letter in VOWELS:  
            count += 1
  return count

# print(count_vowels("hello"))




def punctuation(sentence): 
  
  count = 0
  for character in sentence:
    if character in PUNCTUATION:
      count += 1
  return count

# print(punctuation("Hello! I am, Cajaun: This is me."))


def consonants(word):
  
  count = 0
  for letter in word:
    if letter not in VOWELS and  letter.isalpha():
      count += 1
  return count


# print(consonants("Balick"))

def remove_spaces(string):
  new_string = ""
  for char in string:
    if char != " ":
      new_string += char
  return new_string

text="Hello, how are you? I hope you have enjoyed this course!!\
In this course you have learnt how to solve problems; write python \
code; and have fun"

def main():
  print(text)
  st = remove_spaces(text)
  print("st = ", st)
  print("Vowels = ", count_vowels(st))
  print("Consonants = ", consonants(st))
  print("Punctuations = ", punctuation(st))
  
  
print(main())




    
  