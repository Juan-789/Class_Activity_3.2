"""
2. Write a program that asks a user for an integer, print "YES" if it's positive and print "NO" otherwise.
"""
unknownNumber = int(input("Type in a number and I will determine wether it's negative, positive, or zero. "))
if unknownNumber > 0:
  print ("It's positive.")
elif unknownNumber == 0:
  print ("It's zero")
else:
  print("It's negative.")
#Compares the numbers to see if they are above or under zero
