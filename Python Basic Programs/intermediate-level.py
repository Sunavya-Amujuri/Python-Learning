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


# python program to check whether the number is armstrong number or not.

'''def is_armstrong(num):
    str_num = str(num)
    num_digits = len(str_num)
    sum_digits = sum(int(digits)**num_digits for digits in str_num)
    return num == sum_digits

number = int(input("Give a number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")'''


# Sort Words Alphabetically in a String.

'''names = ["Laxmi","Narayana","Shiva","Parvathi","Ganesh"]
names.sort()
print(names)'''

#python program to find Second Largest Element in a List.

'''numbers = [5, 10, 15, 20, 25]
first = second = float('-inf')

for num in numbers:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

if second == float('-inf'):
    print("There is no largest number.")
else:
    print("The second largest number is: ", second)'''


# Python program to print All Prime Numbers in a Given Range.

'''def prime_numbers(limit):
    primes = []
    for num in range(2,limit+1):
        is_prime = True
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
    
n = int(input("Give a range: "))
num = prime_numbers(n)
print(f"Prime numbers are : {num}")'''


# python program of a frequency of Characters in a String.

from collections import Counter

'''text = input("Give a string: ")
result = Counter(text)  # ✅ No need to create freq = {} manually
print(result)'''

# or

'''def string_characters(text):
    text = text.lower()
    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

string = input("Enter a string: ")
result = string_characters(string)
print("Character frequency: ", result)'''






