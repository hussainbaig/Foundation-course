"""
Write a program to prompt the user for hours and rate per hour using
input to compute gross pay. Use 35 hours and a rate of 2.75 per hour
to test the program (the pay should be 96.25). You should use input to
read a string and float() to convert the string to a number. Do not
worry about error checking or bad user data.
"""

#Getting no. of hours and rate per hour
x = input('Enter no. of hours: ')
y = input('Enter rate per hour: ')

#converting the input string into number
hours = float (x)
rate_per_hour = float (y)

#calculating gross pay
gross_pay = hours * rate_per_hour
print ("Gross Pay:", gross_pay)
