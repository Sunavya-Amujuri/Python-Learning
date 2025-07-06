# Write a program to check whether the given string is a palindrome or not.
''' Palindrome = A palindrome is a word, number, phrase, or sentence that reads the same forward and
 backward (ignoring spaces, punctuation, and capitalization).'''

n = input("Give a string: ")
reverse = n[::-1]

if reverse == n:
    print("Yes, It is palindrome.")
else:
    print("No, It is not palindrome.")




