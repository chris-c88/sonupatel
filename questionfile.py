#In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals. The farmer breeds three species:

#chickens = 2 legs
#cows = 4 legs
#dogs = 4 legs

#The farmer has counted his animals and he gives you a subtotal for each species. You have to implement a script or function that returns the total number of legs of all the animals.

#Example 1
#animals(2, 3, 5) ➞ 36

#Example 2
#input(1, 2, 3) ➞ 22

#Example 3
#How many Chickens? 5
#How many Cows? 2
#How many Dogs? 8
#50 legs

#Create a python script to solve this problem.

print("returns the total number of legs of all the animals")
print("chickens = 2 legs\ncows = 4 legs\npigs = 4 legs")
print("There are 5 chickens, 2 cows and 8 pigs")
chickens=2
cows=4
pigs=4
chic=5
cows1=2
pigs1=8

def animals(chickens,cows,pigs):
    return chic*chickens+cows1*cows+pigs1*pigs
print(animals(chickens,cows,pigs))

