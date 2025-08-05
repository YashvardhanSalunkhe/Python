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
# num=int(input("Enter number for factorial:"))
# def factorial(num):
#     result=1
#     for i in range(2,num+1):
#         result*=i
#     return result
# print("Factorial of",num,"is",factorial(num))

# Q7)Write a function to check whether a given number is prime or not.
# n1=int(input("Enter a number:"))
# def prime_check(n1):
#     i=1
#     count=0
#     while i<=n1:
#         if n1==1:
#             print("Doesn't matter")
#         if n1%i==0:
#             count+=1
#         i+=1
#     if  count<=2:
#         print(n1,"is prime.")
#     else:
#         print("It is not prime")
# prime_check(n1)
    
# Q8)Write a function that accepts a list of numbers and returns the largest number.
# n1=int(input("Enter how many numbers you  want to  enter:"))
# i=0
# list1=list(map(int,input("Enter the elements of the list with spaces:").split()))
# def greatest(list1):
# #     bigger=max(list1)
# #     print(bigger)
# # greatest(list1) 

# # Q9)Write a function to count the number of vowels in a given string.
# str1=str(input("Enter a string:"))
# def vowel_check(str1):
#     count=0
#     for i  in str1:
#         if i in 'aeiou':
#             count+=1
#     print(count,"vowels  present in the string")
# vowel_check(str1)


# # Q10)Write a function that takes a list of numbers and returns only the even numbers.
# nums=list(map(int,input("enter the numbers with spaces:").split()))
# def even_check(nums):
#     even_list=[]
#     for  i in nums:
#         if  i%2==0:
#             even_list.append(i)
#     print(even_list)
# even_check(nums)

# Q11)Write a function to calculate the sum of digits of a number.
num1=int(input("Enter the number:"))
def sum_digit(num1):
    sum1=0
    for i in num1:
        digit=i%10
        sum1=sum1+digit
        num1=num1//10
    print("sum of the digits:",sum1)
sum_digit(num1)