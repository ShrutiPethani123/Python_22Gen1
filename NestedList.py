l1=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(l1)

# for i in l1:
#     print(i)

# for i in l1:
#     for j in i:
#         print(j, end=" ")


# # print()
# print(l1[1][1])  

# print([ j for i in l1  for j in i])

# # print all elements that greater than 5

# l2 = [j for i in l1 for j in i if j>5]
# print(l2)


# l3 = [1,2,3,[78,12,34],89,[4,5,5,6]]

# print(l3[0])
# print(l3[4])
# print(l3[3])
# print(l3[3][2])
# l3[3].append(100)
# l3[3].insert(1,500)
# # l3[5].pop(1)
# l3[5].remove(5)
# print(l3)


l4=[
    [1, "ram", 2000],
    [2,'joy',2002],
    [3,'riya',2003],
    # [4,'jina']
]

# for i in l4:
#     print(i)

for i in l4:
    print(i[1])

print([i[1] for i in l4])

for i,j,k in l4:
    print( i , j , k)


a=45

str = f'''
This 
is
multi
line comment{a}

'''
print(str )
print(type(str))


'''
1. Take one nested list and print maximum length of list.

l=[[1,2,3,4,5],[56],[78],[45,23],[45,67,1,8,9,0,1,2,3],[3,4,5]]

o/p: [45,67,1,8,9,0,1,2,3]

'''

l=[[1,2,3,4,5],[56],[78],[45,23],[45,67,1,8,9,0,1,2,3],[3,4,5]]

# l2 = [len(i) for i in l]
# print(l2)
# max1 = max(l2)
# index = l2.index(max1)
# print(l[index])


l3 = l[0]
for i in l:
    if len(i)>len(l3):
        l3=id 

print(l3)
