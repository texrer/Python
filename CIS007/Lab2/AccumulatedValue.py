#Richard Rogers
#Python Programming CIS 007
#Lab 2
#Question 2
#Write a program that reads in an investment amount, the annual interest rate, 
#and the number of years, and displays the future investment value using the following formula:
#futureInvestmentValue = investmentAmount * (1 + monthlyInterestRate)numberOfMonths
#For example, if you enter the amount 1000, an annual interest rate of 4.25%, 
#and the number of years as 1, the future investment value is 1043.33.


invest_amt = eval(input("Enter an Investment Amount:"))
annual_int_rate = eval(input("Enter an Interest Rate:"))
num_years = eval(input("Enter Number of Years:"))
monthly_int_rate = (annual_int_rate/12)/100
num_months = num_years * 12
print("Accumulated value is:", round(invest_amt*((1+monthly_int_rate)**num_months),2))
