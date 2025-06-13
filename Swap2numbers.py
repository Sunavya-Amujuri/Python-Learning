'''swapping of 2 numbers with temporory variables
a = 10
b = 20
temp = a  (a = 10 is fixed here)
a = b
b = temp 
print(f"Value of a: {a}")       
print(f"Value of b: {b}")    (Ans: a = 20, b = 10)'''  


#Swapping of 2 numbers without temporary Variables

a = int(input("Give a: "))
b = int(input("Give b: "))
b = b+a
a = b-a
b = b-a
print(f"Value of a: {a}")       
print(f"Value of b: {b}") 

