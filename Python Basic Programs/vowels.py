'''Write a program that takes a string input from the user and counts the number of 
volwels (A,E,I,O,U, and their lowercase equivalents) in the string.'''

s = input("Give name: ")
s2 = s.lower()    #converts all the characters into lowercase
a = s2.count('a')
e = s2.count('e')
i = s2.count('i')
o = s2.count('o')
u = s2.count('u')

print(f"Number of vowels: {a+e+i+o+u}")