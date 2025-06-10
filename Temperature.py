#Converting Temparature Units
#(F) Fahrenheit: c*(9/5)+32
#(K) Kelvin: 273+c

c = int(input("Temperature_Celsius: "))
print(f"Temperature in Fahrenheit: ({c*(9/5)+32})",sep="")
print(f"Temperature in Kelvin: {273+c}",sep="")