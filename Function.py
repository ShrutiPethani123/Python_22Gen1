'''

Function: block of code

type:
1. pre define 
2. user define

'''

def display():
    print("Hello....") 

display()
display()

def add(x,y):
    return x+y



a=int(input("Enter a no: "))
b=int(input('ENter a no: '))
# ans=add(a,b)
# print(ans)
print(add(a,b))


# Make one function for check prime number.


# def isPrime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True

# n=int(input("Enter a no: "))
# if(isPrime(n)):
#     print('Prime....')
# else:
#     print('Not Prime')


# Make one function that take two arguments and return gcd(HCF) of that two  number.
'''
6: 1 2 3 6
12: 1 2 3 4 6 12

gcd: 6

'''


# def hcf(a,b):

#     ans=0
#     if a<b:
#         min=a
#     else:
#         min=b

#     for i in range(1,min+1):
#         if(a%i==0 and b%i==0):
#             ans=i

#     return ans


# a=int(input("Enter a no:"))
# b=int(input("Enter a no:"))
# print(hcf(a,b))


# take range from user and print all perfect number between that range
'''
6: 1 2 3 6

1+2+3 = 6

6 , 28 , 496 , 8128......

'''

def printPerfect(a,b):

    for i in range(a,b+1):
        sum=0
        # for j in range(1,i):
        #     if i%j==0:
        #         sum+=j
        j=1
        while(j<i):
            if i%j==0:
                sum+=j
            j+=1
            
        
        if(i==sum):
            print(i,end=" ")


a=int(input("Enter star:"))
b=int(input("Enter end:"))
printPerfect(a,b)