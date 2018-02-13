#This is a python program to calculate gross pay

Hours = input('Enter number of hours : ') #Working hours

Rate = input('Enter rate charged per hour : ') #Rate charged

#Converting the input into interger

WorkingHours = int(Hours)
RateperHour = int(Rate)

#Multiplying

Pay = WorkingHours * RateperHour

#print Pay

print(Pay)
