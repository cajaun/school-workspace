ARTICLES = ["a", "an", "the"]

def stringList(string):
  
  return string.split()


def countWords(string):
  
  transformedString = stringList(string)
  
  newList = [len(word) for word in transformedString]
  
  return newList

# print(countWords("This is a test to check the values on an input"))


def articles(string):
  
  transformedString = stringList(string)
  
  newList = [word for word in transformedString if word in ARTICLES]
  
  return newList 


print(articles("This is a test to check the values on an input"))