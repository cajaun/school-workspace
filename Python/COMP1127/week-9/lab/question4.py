from question3 import unlucky
def soUnlucky(start, end):
  

  return [year for year in range(start, end+ 1) if len(unlucky(year)) == 3]

print(soUnlucky(1000,2018))