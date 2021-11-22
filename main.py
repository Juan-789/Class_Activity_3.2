"""
2. Write a program that asks a user for an integer, print "YES" if it's positive and print "NO" otherwise.
"""
unknownNumber = int(input("Type in a number and I will determine wether it's negative or positive. "))
if unknownNumber >= 0:
  print ("It's positive.")
else:
  print("It's negative.")