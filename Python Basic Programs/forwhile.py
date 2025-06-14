''' 1) Take a positive integer N as input and print all the numbers from 1 to N.'''

#n = int(input("Give n value: "))
#for i in range(1,n+1):
 #   print(i)


'''n = int(input("Give n value: "))
i = 1
while i<=n:
    print(i)
    i += 1'''


''' 2) Take a positive integer N as input and calculate the sum of the first N natural numbers.'''

'''n = int(input("Give n value: "))
i = 1
sum = 0

#sum = 0
#i = 1 , sum = sum+i = 0+1 = 1
#i = 2 , sum = sum+i = 1+2 = 3
#i = 3 , sum = sum+i = 3+3 = 6

while i<=n:
    sum += i
    i += 1

print("sum = ", sum)'''


''' 3) Take a positive integer N as input and print all the even numbers from 1 to N.'''

'''n = int(input("Give n value: "))

i = 1
while i <=n:                # for odd if not (i<=2 == 0):
    if i%2 == 0:                         
        print(i)                        
    i += 1'''


''' 4) Take a positive integer n as input and print the multiplication table of N from 1 to 10.'''

'''n = int(input("Give n value: "))
 i = 1

while i<=10:
    print(f"{n} x {i} = {n*i}")
    i += 1'''


'''n = int(input("Give n value: "))
for i in range (1,11):
    print(f"{n} x {i} = {n*i}")'''


''' 5) Take a positive integer n as input and calculate its factorial (N!)'''

n = int(input("Give n value: "))
factorial = 1

while n>0:
    factorial *= n
    n -= 1

print(factorial)



