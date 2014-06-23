#Richard Rogers
#Python Programming CIS 007
#Lab 2
#Question 4
#Body mass index (BMI) is a measure of health based on weight. 
#It can be calculated by taking your weight in kilograms and dividing it by the square of your height in meters. 
#Write a program that prompts the user to enter a weight in pounds and height in inches and displays the BMI. 
#Note that one pound is 0.45359237 kilograms and one inch is 0.0254 meters. 


weight_lbs = eval(input("Enter weight in pounds:"))
height_inches = eval(input("Enter height in inches:"))
weight_kgs = weight_lbs*0.45359237
height_meters = height_inches*0.0254
print("BMI is:", round(weight_kgs/height_meters**2, 4))
