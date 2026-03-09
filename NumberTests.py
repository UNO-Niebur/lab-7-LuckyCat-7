#NumberTests.py

def isThreeOrFive(n):
  """Returns boolean determination if number is multiple of 3 or 5"""

  if n % 3 == 0 or n % 5 == 0:
    return True
  else:
    return False

def isPrime(p):
  """Returns boolean (True/False) if the value given is prime."""
  if p % 2 != 0:
    return True
  else:
    return False
  

def isEven(n):
  """Returns boolean about given value being even."""

  if n % 2 == 0:
    return True
  else:
    return False

def addNum(numList, num):
  """Adds the given number to the given list. Does not add duplicate values."""

  numList.append(num)


def fibonacciSequence(value):
  """Returns a list of numbers in the fibonacci sequence up to the given value"""

  nums = [1, 2]
  size = 2
  n = nums[size - 1] + nums[size - 2]

  while n < value:
    addNum(nums, n)
    size = len(nums)
    n = nums[size - 1] + nums[size - 2]

  return nums
def sumofsquares(s):
 n = s*(s + 1)*(2*s + 1)//6
 return n 

def squareofsums(s):
  n = s*(s+1)//2
  square = n**2
  return square
 


#Test your new functions in this main
def main():
  print(squareofsums(100))


if __name__ == '__main__':
    main()
