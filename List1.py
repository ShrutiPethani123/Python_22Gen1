''''

list: []

[1,2,3,4]
['python','android','java']
[2.3,45,'java']

string: ordered and immutable
list: ordered and mutable

'''
l1 = [1,2,3,4,5]
print(l1)
print(type(l1))

# print(l1[0])
# print(l1[1])
# print(l1[2])
# print(l1[3])
# print(l1[4])
'''
# index 0 to len-1

# iterate
# 1.
for i in range(0,len(l1)):
    print(l1[i])

# 2. 

for i in l1:
    print(i)

'''


l2 = [11,23,5.6,'java','python',False]
#     0   1  2    3      4       5
#     -6 -5  -4   -3    -2      -1
# print(l2)

# print(l2[-1])
# print(l2[-3])

# print(l2[1:3])
# l3=l2[2:4]
# print(l3)
# print(l2[-1:-4])
# print(l2[-1:-4:-1])
# print(l2[3:-2])
# print(l2[3:-1])
# print(l2[3:-6:-2])



l2=[43,56,12,78,23,90]
print(l2)
print("Length: ",len(l2))
print("Max: ",max(l2))
print("Min: ",min(l2))
print("sort: ",sorted(l2))
print("sort: ",sorted(l2,reverse=True))

l3 = ['apple','kiwi','Banana','orange','mango','ow']
# print(l3)
# print("Length: ",len(l3))
# print("Max: ",max(l3))
# print("Min: ",min(l3))
# print("sort: ",sorted(l3))
# print("sort: ",sorted(l3,reverse=True))

# add element
# append - add element in last

l3.append('abc')
print(l3)

# insert(index, element)
l3.insert(2,"xyz")
print(l3)

l3.insert(4,56)
print(l3)

# Take one list from user and print that list.
#  size: 
# elements:

# size = int(input("Enter size: ")) #4

# list=[]
# for i in range(size): #0 1 2 3
#     # n= int(input("Enter element: "))
#     # list.append(n)
#     list.append(int(input("Enter element")))

# print(list)

# for i in list:
#     print(i)


# 2. Take one list from user and print sum of all elements.

# l = [2,4,5,6,8]
# sum=25

# sum=0
# for i in list:
#     sum+=i

# print(sum)

# 3. Take one list from user and print all even length elements into list.

# l = ['java','python','c','cpp','html']
# o/p: ['java','python','html']


# n = int(input("Enter size: "))
# list=[]
# for i in range(n):
#     list.append(input("Enter element: "))
# print(list)

# l2=[]

# for i in list:
#     if len(i)%2==0:
#         l2.append(i)

# print(l2)