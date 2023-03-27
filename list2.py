'''
l = [1,2,3,4]
print(l)

l2 = l.copy()
print(l2)

l3 = l
print(l3)

l2.append(34)
l3.append(45)

print(l)

print(id(l))
print(id(l2))
print(id(l3))

# is , is not

# print(l2 is l) - False
# print(l3 is l) - True

print(l2 is not l) - True
print(l3 is not l) - False

'''



l2 = [2,4,5,1,6,7,'a','h']

# l2.clear()
# print(l2)

print(l2.pop(2)) # index
print(l2)

print(l2.pop(-2))
print(l2)

# l2.pop(45) - error (index out of range)
# print(l2)

l2.remove(6) #element
print(l2)

# l2.remove(9) - error
print(l2)

l3=['java','c','python','python']
print(l3.index('python'))
# print(l3.rindex('python')) error 



# Take one list from user and make one list that contains square of elements.

l =[2,3,4,5]
l1 = [4,9,16,25]

list=[]
list2=[]
n = int(input("Enter size: "))
for i in range(n):
    list.append(int(input("Enter element")))

print(list)

# for i in list:
#     # n= pow(i,2)
#     # list2.append(n)
#     # list2.append(pow(i,2))
#     list2.append(i**2)

for i in range(n):
    list2.append(list[i]**2)

print(list2)



