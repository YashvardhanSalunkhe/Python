# Q1.Write a program to print the following using while loop
# First 10 Even numbers
# n=2
# while n <= 20:
#     print(n)
#     n+=2

#Q2)First 10 Odd numbers
# n=1
# while n <= 20:
#     print(n)
#     n+=2

# # Q3. First 10 Natural numbers (Natural numbers strts form 1)
# n=1
# while n <= 10:
#     print(n)
#     n+=1

# # Q4. First 10 Whole numbers
# n=0
# while n>=0 and n <= 10:
#     print(n)
#     n+=1

# # Q5. Write a program to print first 10 integers and their squares using while loop.
# n=1
# while n>=0 and n <= 10:
#     print(F"Square of {n} is {n**2}")
#     n+=1

# Q6. Write while loop statement to print the following series: 10, 20, 30 … … 300
# n=1
# while n>=0 and n <= 30:
#     print(n*10)
#     n+=1

# Q7. Write a while loop statement to print the following series 105, 98, 91 ………7.
# n=105
# while n>0:
#     print(n)
#     n-=7

# Q8. Write a program to print the first 10 natural number in reverse order using while loop.
# n=10
# while n>0:
#     print(n)
#     n-=1

# Q9. Write a program to print sum of first 10 Natural numbers.
# n=1
# sum=0
# while n <=10:
#     sum+=n
#     n+=1
# print(sum)

# Q10. Write a program to print sum of first 10 Even numbers.
# n1=0
# sum=0
# while n1<=20:
#     sum=sum+n1
#     n1+=2
# print(sum)

# Q11. Write a program to print table of a number entered from the user.
# n=int(input("Enter a number for printing a table  :"))
# i=1
# while i<=10:
#     print(f"{n}X{i} = {n*i}")
#     i+=1

# Q12. Write a program to print all even numbers that falls between two numbers (exclusive both numbers) entered from the user using while loop.
# n1=int(input("Enter a first number"))
# n2=int(input("Enter a second number"))
# i=n1+1
# while i<n2:
#     if i%2==0:
#         print(f'Even numbers between {n1} and {n2} are {i}')
#     i+=1

# Q13. Write a program to check whether a number is prime or not using while loop.
# n1=int(input("Enter a  number")) 
# count=0
# i=1
# while i<=n1:
#     if n1==1:
#         print("Doesn't matter")
#     if n1%i==0:
#         count+=1
#     i+=1
# if count<=2:
#     print("You Entered a Prime number")
# else:
#     print("It is not a prime number")

# Q14. Write a program to find the sum of the digits of a number accepted from the user.
# n=int(input("Enter a number:"))
# i=1
# sum_of_digits=0
# while i<n:
#     digit=n%10 
#     sum_of_digits+=digit
#     n=n//10
# print("Sum of the digit is: ",sum_of_digits)
     
# Q15)Write a program to find the product of the digits of a number accepted from the user.
# n=int(input("Enter a number:"))
# product_of_digits=1
# while n>0:
#     digit=n%10 
#     product_of_digits*=digit
#     n=n//10
# print("Sum of the digit is: ",product_of_digits)

# Q16)Write a program to reverse the number accepted from user using while loop.
# n=int(input("Enter a number:"))
# reverse=0
# while n>0:
#     digit=n%10 
#     reverse=(reverse*10)+digit
#     n=n//10
# print("Sum of the digit is: ",reverse)

# Q17)Write a program to display the number names of the digits of a number entered by 
# user, for example if the number is 231 then output should be Two Three One.
# digit_names = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
# n = int(input("Enter a number: "))
# print("Number names:")
# for digit in str(n):
#     print(digit_names[int(digit)], end=" ")

# Q18) Write a program to print the Fibonacci series till n terms (Accept n from user) using while loop.
# n = int(input("Enter a number: "))
# count=0
# a,b=0,1
# print("Fibonacci series:")
# while count<n:
#     print(a,end=" ")
#     temp=a+b
#     a=b
#     b=temp
#     count+=1

# Q19)Write a program to print the factorial of a number accepted from user.
# n=int(input("Enter a number:"))
# i=1
# fact=1
# while i<=n:
#     fact=fact*i
#     i+=1
# print(f"Factorials of  {n} are {fact }")

# Q20). Write a program to check whether a number is Armstrong or not. (Armstrong number is a number that is equal to the sum of cubes of its digits for example : 153 = 1^3 + 5^3 + 3^3.)
# n=int(input("Enter a Three digit number:"))
# original=n
# sum_digit=0
# while n>0:
#     digit=n%10
#     sum_digit+=digit**3
#     n=n//10
# if  sum_digit==original:
#     print(original,"is armstrong number.")
# else:
#     print(original,"is not a armstrong number.")



#Q22. Write a program to enter the numbers till the user wants and at the end it should display the sum of all the numbers entered.
# n=int(input("Enter a number to print till that number:"))
# i=0
# sum=0
# while i<=n:
#     print(i)
#     sum=sum+i
#     i+=1
# print(f" the sum all numbers is {sum}")

# Q23. Write a program to enter the numbers till the user enter ZERO and at the end it should 
# display the count of positive and negative numbers entered.
# pos=0
# neg=0
# i=1
# while i>=0 :
#     n1=int(input("Enter number"))
#     if n1==0:
#         break
#     if n1>0:
#         pos+=1
#     else:
#         neg+=1
#     i+=1  
# print(f"The count of positive number is {pos}")
# print(f"The count of negative numbers are {neg}")   

# Q29. Write a program to accept 10 numbers from the user and display it’s average
# n=1
# add=0
# print("Enter 10 numbers:")
# while n>0:
#     if n==10:
#         break
#     n1=int(input())
#     add=add+n1
#     n+=1
# avg=add/10
# print(f"The addition of 10 numbers is {add}")
# print(f"The average of 10 numbers is {avg}")