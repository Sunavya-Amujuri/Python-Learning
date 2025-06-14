'''Write a program that takes a string input from the user and checks if it is a palindrome or not.
A palindrome is a word, phrase, number, or sequence of characters that reads the same backward as forward.'''

s = input("Give a string: ")

reverse = s[::-1]

if reverse == s:
    print("It is a palindrome.")
else:
    print("It is not a palinrome.")
