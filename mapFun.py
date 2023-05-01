# map(function , iterator)

def fun(n):
    return len(n)

result = map(fun,('India','USA',"UK"))
print(list(result))



def fun2(a,b):
    return a+str(b)

ans = map(fun2, ('raj','tom'),[45,89,67,46,78,90] )
print(list(ans))


# Take one list from user and make one new list that contain  square of elements using map
# l : [ 2 3 1 4]
# l1: [4,9,1,16]

def fun(a):
    return a*a

# l1 = map(fun,[2,4,5,6])
l1 = map(lambda a:a*a,[2,3,4,5])
print(list(l1))



# Take two list and make one new list that contain sum of two list using map and lambda function.
l=[1,2,3,4]
l1=[2,4,5,6]
# l3:[3,6,8,10]

l2 = list(map(lambda a, b: a+b,l,l1))
print(l2)


# Take one list that have string type elements and make one new list that contain upper string list.
'''
l= ['apple','mango']
l1=['APPLE','MANGO']

'''
l= ['apple','mango']
l2 = list(map(lambda a: a.upper(),l))
print(l2)