"""
8.  Take rupeess from user and count total number of notes.

n - 1678

500 - 3 (1678/500 = 3.)  -> 1500(178)
200 - 0
100 - 1
50 - 1
10 - 2
5 - 1
1 - 3

"""

n=int(input("Enter rs: "))

n500 = n//500
# n=n%500
n = n - n500 * 500
n200 = n//200
n=n%200
n100=n//100
n=n%100
n50=n//50
n=n%50
n10=n//10
n=n%10
n5=n//5
n=n%5
n1=n



print("500: ",n500)
print("200: ",n200)
print("100: ",n100)
print("50: ",n50)
print("10: ",n10)
print("5: ",n5)
print("1: ",n1)
