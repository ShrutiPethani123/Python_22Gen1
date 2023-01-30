'''
loops -> repetation

for
while
do while -> not available in python

while(condition):
    // block of code
    // inc/dec


'''
# i=1
# while i<=5:
#     print("Royal")
#     # i++; -> invalid
#     i+=1
#     # i=i+1


# k=7
# while k>=5:
#     print("Python")
#     # k-=1 
#     k=k-1
# # 7 6 5




'''
range(end) -> 0 to end-1
range(start , end) -> start to end-1
range(start,end,step)

'''

# for i in range(5):
#     print(i,end=" ")

# for i in range(5,10):
#     print(i,end=" ")

# for j in range(4,10,2):
#     print(j,end=" ")

# for j in range(5,10,-2):
#     print(j,end=" ")

# for j in range(10,-4,-2):
#     print(j,end=" ")

# for j in range(-4,-10,-3):
#     print(j,end=" ")

# for j in range(1,5):
#     print(j,end=" ")

'''
C 

for(;;)
{

}


'''


# list1=[1,2,3,4,5,6]
# list2=['banana' ,'apple','graps','orange']

# for i in list2:
#     print(i , end="   ")

'''

1. print 10 to 20 number using for and while loop.
2. print reverse 50 to 30 number using for and while loop.
3. print all even number between 1 to 20 using both loop.
4. print all odd number between 50 to 90 using both loop.
5. print number of digit.
    n=354346
    digit: 6
6. Find first and last digit of number.
    n=3534

    first:3
    last:4

7. print sum of all digits.

    n-34234
    sum: 16

8. Print multiplication table of user given number using both loop.

    n- 5
    5 * 1 = 5
    5 * 2 = 10
    .
    .
    5 * 10 = 50

9. find factors of number.

    n - 12
    1 2 3 4 6 12

10. Find Factorial of number.

    n- 5
    ans- 120

    n-6
    ans- 720

11. Check number is perfect number or not.

    n - 4
    (1 2 4) sum = 1+2 = 3
    4!=3 -> not perfect

    n- 6
    (1 2 3 6) sum=1+2+3 = 6
    6==6 -> perfect

    n-28
    (1 2 4 7 14 28 )sum= 1+2+4+7+14 = 28

    6,28,496,8128 -> perfect number.

'''
# 5.
# n=int(input("\nEnter a no: "))
# count=0
# while(n>0): #4567 456 45 4 0
#     n=n//10 #456 45 4 0
#     count+=1 #1 2 3 4

# print(count)

# 6.
# n=int(input("\nEnter a no: "))
# last = n%10
# print("last digit is: ",last)

# while n>0: #4532 453 45 4 0
#     rem=n%10 #2 3 5 4
#     n=n//10 #453 45 4 0
# first=rem

# print("First digit is: ",first)

# 8.

# n=int(input('Enter a no:'))

# for i in range(1,11):
    # print(n, "*",i,'=',n*i)
    # print(f"{n} * {i} = {n*i}")
    # print("{} * {} = {} ".format(n,i,n*i))
    # print("{2} * {0} = {1} ".format(i,n*i,n))

# 9

# n=int(input("entr a no:"))

# for i in range(1,n+1):
#     if(n%i==0):
#         print(i,end=" ")
#     i+=1

# 10.

# fact=1
# n=int(input('Enter a no: '))
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

# 11.

n=int(input("entr a no:"))
i=1
sum=0
while i<n:
    if n%i==0:
        sum=sum+i
    i+=1

if sum==n:
    print("perfect")
else:
    print("Non Perfect")
