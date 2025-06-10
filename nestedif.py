weather = input("Tell me weather condition: ")
time_of_day = input("Tell me time of the day: ")

if weather == "sunny":
    if time_of_day == "day":
         print("You can play cricket.")
    else:
         print("It's night. Time to sleep.")
elif weather == "rainy":
     print("You play with your Teddy bear toy.")
elif weather == "snowy":
     if time_of_day == "night":
          print("You play with your Boat toy.")
     else:
          print("You play with your Snowman toy.")
else:
    print("You stay inside and read a storybook.")