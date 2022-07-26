import random
import sys

# Global variables for valid characters
validUpper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
validLower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
validNumber = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
validSpecial = [")", "!", "@", "#", "$", "%", "^", "&", "*", "("]
validChars = [validUpper, validLower, validNumber, validSpecial]

# Meat and cheese
def generatePassword(n):
  ret = ""
  for i in range(0, n):
    rando1 = int(random.random() * 4)
    rando2 = int(random.random() * len(validChars[rando1]))
    ret = ret + validChars[rando1][rando2]
  return ret

# Program entry point
if __name__ == "__main__":
  # Length of password is 8 by default
  length = 8

  if len(sys.argv) > 1:
    length = int(sys.argv[1])
  p = generatePassword(length)

  print(p)