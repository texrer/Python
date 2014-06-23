#Richard Rogers
#Python Programming CIS 007
#Lab 2
#Question 3
#Write a program that reads an integer between 0 and 1000 and adds 
#all the digits in the integer. For example, if an integer is 932, 
#the sum of all its digits is 14. 
#(Hint: Use the % operator to extract digits, and use the // operator to remove the extracted digit. 
#For instance, 932 % 10 = 2 and 932 // 10 = 93.)

num = eval(input("Enter a number between 0 and 1000:"))
if (num <= 1000):
    print("The sum of the digits is:", (num//1000) + (num//100%10) + (num//10%10) + (num%10))

