# Q1)Write a program to print numbers from 1 to 100. Stop the loop if a number divisible by 17 is found.
# i=1
# while i<100:
#     print(i)
#     i=i+1
#     if i%17==0:
#         break
#
# Q2. Read numbers from the user until a negative number is entered. Use break to stop and display the total of all positive numbers.
# print("Enter te numberrs")
# i=1
# pos=0
# while i>0:
#     n=int(input())
#     if n<0:
#         break
#     pos+=1
# print("The count of positive numbers are",pos)

# Q3) Search for the first number between 100 and 200 that is divisible by both 9 and 6. Use break to stop after finding it.
# i=100
# while i<200:
#     print(i)
#     if i%9==0 and i%6==0:
#         break
#     i+=1
#using for loop
# for i in range(100,200):
#     print(i)
#     if i%9==0 and i%6==0:
        # break

# # Q4) Loop through characters in a string. Stop the loop when you find the first vowel.
# str1=str(input("Enter a string:"))
# for i in str1 :
#     print(i)
#     if i.lower() in 'aeiou':
#         print(f"The vowel is :",i)
#         break

# Q5. Write a program to simulate a basic password check. Ask for a password in a loop and use break when the correct one is entered.
# pass1='rohan'
# while (True):
#     a=str(input("enter a password:"))
#     if a==pass1:
#         print("You entered correct password")
#         break

# Q6. Print even numbers between 1 and 50. Stop the loop if the number is greater than 40.
# i=0
# for i in range(i,50):
#     if i%2==0:
#         print(i)
#     i+=1                
#     if i>40:
#         break

# Q7. Write a program to check prime numbers from 10 to 50. Stop the loop if a number is not prime.
# i=1
# for num in range(10,50):
#     if num%i==0:
#         print(f"prime number is {num}")
#     else:
#         break   
#     i+=1 


#using continne

# Q8. Print all numbers from 1 to 50 except those divisible by 5 using continue.
# for i in range(1,51):
#     if i%5==0:
#         continue
#     print(i)
#     i+=1


# Q9. Display all characters in a string except the vowels using continue.
# str1=str(input("Enter a sring:"))
# for char in str1:
#     if char in 'aeiou':
#         continue
#     print(char,end=' ')

# Q10)Write a program that prints numbers from 1 to 20, skipping every third number using continue.
# for i in range(1,21):
#     if i%3==0:
#         continue
#     print(i)
#     i+=1

# Q11. Print all lowercase letters in a string, skipping uppercase letters with continue.
# str1=str(input("Enter a sring:"))
# for  char in str1:
#     if char.isupper():
#         continue
#     print(char,end=' ')

#Q12. From numbers 1 to 100, print only those not divisible by 2 or 3 using continue.
# for i in range(1,101):
#     if i%2==0 or i%3==0:
#         continue
#     print(i)

#Q13) Accept 10 numbers from the user. Skip negative numbers and only add the positive ones.
# pos=0
# for i in range(11):
#     n=int(input("Enter 10 numbers:"))
#     if n<0:
#         continue
#     pos+=1
# print(pos)

# Q14)Loop through a list of fruits and skip the fruit named "banana" using continue.
# fruits=input("Enter a list of fruits with spaces ").split()
# for i in fruits:
#     if i.lower()=="banana":
#         continue
#     print(i)

#using pass
# 15. Write a program that loops from 1 to 10 and uses pass for even numbers.
# i=1
# while i<=10:
#     if i%2==0:
#         pass
#     else:
#         print(i)
#     i+=1

#Q16)Create a function that is defined but not yet implemented using the pass statement.
# def pass1():
#     pass

#17) Write a class with a method stub using pass. Instantiate the class and call the method without errors.

# class demo:
#     def __init__(self):
#         print("You are  in demo class")
#     def  stub(self):
#         pass
# d1=demo()
# d1.stub()

#Q18) Loop through numbers from 1 to 30:
# * If divisible by 3, skip using continue.
# * If number is 25, stop using break.
# * Otherwise, print the number.
# for  i  in range(1,31):
#     if i%3==0:
#         continue
#     elif i==25:
#         break
#     else:
#         print(i)
#     i+=1

# 19. Accept inputs from the user in a loop:
# * If input is a blank string, use pass.
# * If it's "exit", break the loop.
# * Otherwise, print the input in uppercase.

# str1=input("Enter uupper case letters:")
# while True:
#     str1=input("Enter uupper case letters:")
#     if str1==' ':
#         pass
#     elif str1=='exit':
#         break  
#     else:
#         print(str1)

