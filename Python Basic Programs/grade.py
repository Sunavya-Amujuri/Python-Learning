'''Create a program that takes the marks of a student in different subjects as input.
Calculate the total marks and average, and then display the corresponding grade based on the average.'''

a = int(input("Marks of Math: "))
b = int(input("Marks of Science: "))
c = int(input("Marks of English: "))

total_marks = a+b+c
average = total_marks/3

percentage = (total_marks/300)*100
grade = ""
if percentage > 90:
    grade = 'A'
elif percentage > 80 and percentage<=90:
    grade = 'B'
elif percentage > 70 and percentage<=80:
    grade = 'C'
else:
    grade = "P"

print(f"Total Marks: {total_marks} \n Average marks: {average} \n Grade: {grade}")