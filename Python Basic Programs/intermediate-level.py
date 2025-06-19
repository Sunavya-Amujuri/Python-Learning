# Write a program to count number of vowels and consonents.

'''n = input("Give a string: ")
n = n.lower()
vowels = "aeiou"

vowel_count = 0
consonant_count = 0

for char in n:                         #The loop iterates over each character in n.
    if char.isalpha():                 #It processes only alphabetic characters.
        if char in vowels:             #It checks whether each character is a vowel or a consonant.
            vowel_count += 1           #It keeps count of vowels and consonants separately.
        else:
            consonant_count += 1

print("Vowels are: ", vowel_count)
print("Consonants are: ", consonant_count)'''


# Write a program to remove Duplicates from a List.

'''l = [1,2,3,3,5,4,2,7,1]    # for unordered list use this
new_l = []

for i in l:
    if i not in new_l:
        new_l.append(i)

print("New list: ", new_l)'''


#ordered list of numbers use this

'''l = [1,2,3,3,5,4,2,7,1]

new_l = list(set(l))
print("Original list: ", new_l)'''



