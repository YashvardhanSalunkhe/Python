# Q1)Write a function to print your name 5 times.
# name=str(input("Enter your name:"))
# def print_name(name):
#     for i in range(1,6):
#         print(name)
# print_name(name)
#
# Q2)Write a function that accepts a number and prints whether it is even or odd.
# n=int(input("Enter a number:"))
# def tester(n):
#     if  n%2==0:
#         print(n,"is  Even")
#     else:
#         print(n,"Is Odd")
# tester(n)

# Q3)Write a function that accepts two numbers and prints their sum.
# n1=int(input("Enter a first number:"))
# n2=int(input("Enter a second number:"))
# def add(n1,n2):
#     print("addition is:",n1+n2)
# add(n1,n2)


# Q4)Write a function to calculate the square of a number.
# n=int(input("Enter a number:"))
# def square(n):
#     print("Square  of number is :",n*n)
# square(n)

# Q5)Write a function that takes a string as input and prints it in reverse order.
# str1=str(input("Enter a string :"))
# def reverse(str1):
#     reversed_s=''
#     for i in str1:
#         reversed_s=i+reversed_s 
#     print(reversed_s)   
# reverse(str1)

# Q6)Write a function to find the factorial of a given number.
num=int(input("Enter number for factorial:"))
def factorial(num):
    result=1
    for i in range(2,num+1):
        result*=i
    return result
print("Factorial of",num,"is",factorial(num))
