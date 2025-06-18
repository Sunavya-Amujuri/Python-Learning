''' 1) Find the sum of all elements in a given list of numbers.'''

'''m = [10,20,30,40,50]

sum = 0
length = len(m)
for i in range (0,length):
    sum = sum + m[i]
    
print(sum)'''


''' 2) Find the maximum and minimum values in a list of numbers.'''

#short method

'''m = [15,2,6,25,10]

m.sort()
print(m[-1],m[0])

#loop method

maximum = m[0]
minimum = m[0]'''

# Loop through the list to find max and min

m = [15, 2, 6, 25, 10]

# Start by assuming the first value is both the min and max
maximum = m[0]
minimum = m[0]
for num in m:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

print(maximum, minimum)

