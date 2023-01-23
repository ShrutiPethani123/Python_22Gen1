'''
10. Write a program to input electricity unit charge and calculate the total 
	electricity bill according to the given condition:

	For first 50 units Rs. 0.50/unit
	For next 100 units Rs. 0.75/unit
	For next 100 units Rs. 1.20/unit
	For unit above 250 Rs. 1.50/unit


    unit = 30
    bill = 30*0.50 = 15 

    unit = 120
    bill = 50*0.50 + 70 *0.75 = 25+52.5 = 77.5

    unit = 300

    50 - 0.50 = 25
    100 - 0.75 = 75
    100 - 1.20 = 120
    50 - 1.50 = 75

    bill = 295

'''

unit=int(input("Enter units: "))

if unit<=50:
    bill=unit*0.50
elif unit<=150:
    bill = 50*0.50 + (unit-50)*0.75
elif unit<=250:
    bill = 25 + 75  + (unit-150)*1.20
else:
    bill= 25 +75 + 120 + (unit-250)*1.50


print("Total bill is: ",bill)