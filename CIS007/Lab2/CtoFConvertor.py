#Richard Rogers
#Python Programming CIS 007
#Lab 2
#Question 2
#Write a program that reads in an investment amount, the annual interest rate, 
#and the number of years, and displays the future investment value using the following formula:
#futureInvestmentValue = investmentAmount * (1 + monthlyInterestRate)numberOfMonths
#For example, if you enter the amount 1000, an annual interest rate of 4.25%, 
#and the number of years as 1, the future investment value is 1043.33.

invest_amt = eval(input("Enter Investment Amount:"))
annual_int_rate = eval(input("Enter Annual Interest Rate:"))
no_years = eval(input("Enter Number of Years:"))
print("Accumulated value is", invest_amt * (1 + (annual_int_rate//12) ** (no_years * 12)))
