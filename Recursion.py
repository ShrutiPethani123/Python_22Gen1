# recursion: function calling itself

def printNum(n):
    # base case
    if(n==1):
        print(n,end=" ")
        return
    print(n,end=" ")
    printNum(n-1)

printNum(10)



# Factorial

'''
5 = 5*4*3*2*1 = 120
5! = 5*4!
4! = 4*3!
3! = 3*2!

'''
print("------------")
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

print(fact(4))


# Take one number from user and print 1 to that number.
# n = 6
# 1 2 3 4 5 6 


def printNum(n):
    # base case
    if(n==1):
        print(n,end=" ")
        return 
    printNum(n-1)
    print(n,end=" ")

printNum(10)


# Print Fibonacci term
# 0 1 1 2 3 5 8 13 ....

print()
# def fib(n):

#     if n<=1:
#         return n
    
#     return fib(n-1) + fib(n-2)

# print(fib(3))
# print(fib(6))

# for i in range(10):
#     print(fib(i), end=" ")


def fib2(n, first , second):

    if n==0:
        return
    print(first , end=" ")
    fib2(n-1,second , first+second)

fib2(6,0,1)