'''
1. if else
2. switch  -> not available in python
3. loop


-> simple if
-> if else
-> nested if
-> else if ladder


'''
'''
-> In C Programming
age=?
if(age>=18)
{
    printf("Eligible");
}else{
    printf("Not Eligible");
}

'''

# age = int(input("Enter Your age:  "))

# if (age>=18):
#     print("Eligible for Vote")
# else:
#     print("Not Eligible for Vote")

# print('Thank You')

"""

"""

# n=5

# if n>30:
#     print("hello")
# else:
#    print()
# print("Thank YOU!!")

'''
Take one number from user and check number number is positive or negative.

'''

# n=int(input("Enter a no: "))

# if n>0:
#     if n>10:
#         print(n , "is greater than 10")
#     else:
#         print(n , "is less than 10")
# elif n==0:
#     print("ZERO")
# else:
#     print(n,"is Negative")


# if(n%3==0 and n%11==0):
#     print("Divisible")
# else:
#     print("Not divisible")

'''
1. Take one number from user and check number is odd or even.
2. Take two number from user and find minimum number. 
3. Take three number from user and find maximum number.
4. Take one number from user and check number is divisible by 3 and 11 or not ?

    33 - divisible
    6 - not divisible

5. Take cost price and selling price from user and find profit or loss.

    cp - 200
    sp - 500
    profit - 300


    cp-100
    sp-50
    loss-50

6. Write a program to accept the cost price of bike display the road tax to be paid 
    according to the following criteria:

    cost price (in Rs)       Tax
    >100000                  15%
    >50000and <=100000       10%
    <=50000                   5% 

7. Take one number from user and print week days according to that number.
    1 - Sunday
    2 - Monday
    .
    .
    7 - Satuarday
    
    other input: Invalid 

8.  Take rupeess from user and count total number of notes.

n - 1678

500 - 3
200 - 0
100 - 1
50 - 1
10 - 2
5 - 1
1 - 3


n - 2000

500- 4
200 - 0
100 - 0
50 - 0
10 - 0
5 - 0
1 - 0

9. Take two number from user and perform the operation by user given input.

    1. Addition
    2. Sub
    3. Mul
    4. Div
    5. Modulus
    6. Floor division (//)
    7. power(**)
    8. Find area of rectangle
    9. INR to USD
    10. USD to INR

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





    2**3 -> 8






'''

a = int(input("ENter a no: "))

# if a%2==0: print("Even Number");print("Hello...")
# else: print("Odd Number")

print("Even Number") if a%2==0 else print("Odd Number")



