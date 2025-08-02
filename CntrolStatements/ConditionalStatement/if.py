#1. Conditional Statements (Decision-Making) Used to make decisions based on a condition.

#Q1)Check if a number is positive, negative, or zero.

# n=int(input("Enter a number"))
# if n%2==0:
#     print("The given number is even")
# if n%2!=0:
#     print("The given number is odd")
# if n==0:
#     print("The given number is Zero")

#Q2)Check if a person is eligible to vote (age ≥ 18).

# age=int(input("Enter your age "))
# if age>18:
#     print("you are eligible for voting")
# if age<18:
#     print("you are not eligible for voting")

#Q3)Check if a year is a leap year.

# year=int(input("Enter a year"))
# if year%4==0:
#     print("The year is leap year")
#else:
    #print("year is not a leap year")


# #Q4)Find the greatest of two numbers.

# n1=int(input("Enter a first number"))
# n2=int(input("Enter a second number"))
# if n1>n2:
#     print("the greater number is:",n1)
# else:
#     print("the grewter number is:",n2)

#Q5)Find the largest among three numbers.

# n1=int(input("Enter a first number"))
# n2=int(input("Enter a second number"))
# n3=int(input("Enter a Third number"))
# if n1>n2 & n1>n3:
#     print("the greater number is:",n1)
# elif n2>n1 & n2>n3:
#     print("the greater number is:",n2)
# else:
#     print("the greater number is:",n3)

#Q6)Check whether a character is a vowel or consonant.

# str1=str(input("Enter a character "))
# if str1=='a' or str1=='e'or str1=='i' or str1=='o' or str1=='u' or str1=='A' or str1=='E' or str1=='I' or str1=='O' or str1=='U':
#     print("The charcter is vowel")
# else:
#     print("The character is consonant")

#Q7)Check if a number is divisible by both 3 and 5.

# n1=int(input("Enter a  number"))
# if n1%3==0 and n1%5==0:
#     print("The number is Divisible by 3 and 5")
# else:
#     print("The number cannot divisible by 3 and 5")

#Q8)Check if a given number is within the range 1 to 100.

# n1=int(input("Enter a  number"))
# if n1>0 and n1<100:
#     print(f"The {n1} is within the range ")
# else:
#     print(f"The {n1} is not in the range")

#Q9)Use an if-elif-else statement to assign a grade (A/B/C/D/F) based on a test score.
# t_score=int(input("Enter your test score out of 100:"))
# if t_score<100 and t_score>90 :
#     print("Your Grade is A")
# elif t_score<90 and t_score>80 :
#     print("Your Grade is B")
# elif t_score<80 and t_score>70 :
#     print("Your Grade is C")
# elif t_score<70 and t_score>60 :
#     print("Your Grade is D")
# elif t_score<60 :
#     print("Your Grade is E")
# else:
#     print("Invalid input")

# Q10)Create a condition that checks if a triangle is equilateral, isosceles, or scalene given side lengths.
# s1=float(input("Enter a first side:"))
# s2=float(input("Enter a second side:"))
# s3=float(input("Enter a Third side:"))
# if s1==s2==s3:
#     print("The triangle is Equilateral")
# elif s1==s2 or s2==s3 or s3==s1:
#     print("The triangle is  Isoscelen. ")
# else:
#     print("Triangle is Scelen")

# Q11)A store offers a 10% discount if the total bill is over \$100. Write a condition that calculates the final amount.
# billamt=int(input("Enter a bill ammount:"))
# finalamt=0
# if billamt>100:
#    discount=billamt*0.10
#    finalamt=billamt-discount
#    print(f"final amount is {finalamt}")
# else:
#     finalamt=billamt
#     print(f"final amount is {finalamt}")

# Q12) Implement a program that simulates a simple ATM: If balance is sufficient and amount is positive, allow withdrawal.
# balance=5000
# amt=int(input("Enter a amount to wothdraw:"))
# if amt>0 and amt<balance:
#     print("Withdrawal Allowed")
# else:
#     print("Withdrawal not allowed")

# Q13)Write a condition to determine if a given time is AM or PM based on a 24-hour input.
# hour=int(input("Enter a hour (0-24):"))
# if hour<12 and hour>0:
#     print(f"its AM")
# elif hour>12 and hour<24:
#     print(f"its PM")
# else:
#     print("Invalide input")

# Q14) Write a condition that simulates traffic lights: Red (Stop), Yellow (Wait), Green (Go) based on color input.
# import random
# light=['red','yellow','green']
# signal=random.choice(light)
# if signal=='red':
#     print("You selected",signal)
#     print("Stop")
# elif signal=='yellow':
#     print("You selected",signal)
#     print("Wait")
# else:
#     print("You selected",signal)
#     print("Go")
# Q15)Write a program that determines whether a character is uppercase, lowercase, a digit, or a special character.
# char=input("Enter a one character:")
# if len(char)!=1:
#     print("plzz Enert only 1 charcter to check. ")
# else:
#     if char.isupper():
#         print("Its an Uppercase character")
#     elif char.islower():
#         print("Its an Lowercase charater")
#     elif char.isdigit():
#         print("Its a digit")
#     else:
#         print("wrong input")
# Q16) Create a login system that checks for both username and password correctness.
# username='rohan'
# password='rohan123'
# name=str(input("Enter Username:"))
# pass1=str(input("Enter  password"))
# if name==username and pass1==password:
#     print("login Succesfull")
# else:
#     print("Wrong Username and password")

# Q17) calculater 

# a=int(input("Enter your value a:-"))
# b=int(input("Enter value b :-"))
# o=input("choose the operation for given values :-")
# if o=="+":
#     print(a+b)
# elif o=="-" :
#     print(a-b)
# elif o=="*" :
#     print(a*b)
# elif o=="/" :
#     print(a/b)
# elif o=="" :
#     print(a**b)
# else :
#     print("None")

# Q18)Write a program that takes a person's weight and height as input and prints their BMI categor

# h=float(input("Enter your height :-"))
# w=float(input("Enter your weight :-"))
# bmi=w/h**2
# if bmi<18.5 :
#     print(f"Your BMI is{bmi}")
#     print("Underweight")
# elif (bmi>=18.5 and bmi<=24.9) :
#     print(f"Your BMI is{bmi}")
#     print("Normal weight")
# else :
#     print(f"Your BMI is{bmi}")
#     print("O")

# Q19)Write a program to calculate the electricity bill based on the number of units consumed.
# unit1=int(input("Enter the units that are used:"))
# if unit1<=100:
#     bill=unit1*5
#     print(f"total bill is {bill}")
# elif unit1>100:
#    bill=(100*5)+((unit1-100)*8)
#    print(f"Total bill is {bill}")
# else:
#     print("invalid input")

# Q20)Write a program that takes a temperature in Celsius and prints:

# temp=int(input("Enter the temperature:"))
# if temp>35:
#     print("Hot")
# elif temp>25 and  temp<=35:
#     print("Warm")
# elif temp>15 and temp<=25:
#     print("Cool")
# else:
#     print("cold")
