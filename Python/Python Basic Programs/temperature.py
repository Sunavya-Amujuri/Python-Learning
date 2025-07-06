''' Build a temperature converter program that allows the user to convert temperatures between 
celsius, kelvin and fahrenheit.'''

#(F) Fahrenheit: c*(9/5)+32
#(K) Kelvin: 273+c


temp,unit = input("Enter Temperature: and Enter unit(K/F/C): ").split()
temp = float(temp)
unit = unit.upper()

if unit == "C":
    f = (temp*9/5)+32
    k = temp+273
    print("Fahrenheit:", f)
    print("Kelvin:", k)
elif unit == "F":
    c = (temp-32)*5/9
    k = c+273
    print("celsius:", c)
    print("kelvin:", k)
elif unit == "K":
    c = temp-273
    f = (c*9/5)+32
    print("celsius:", c)
    print("fahrenheit:", f)
else:
    print("Invalid unit entered.")


