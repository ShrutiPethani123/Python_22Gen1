# Nested loop - loop inside loop

# for i in range(1,5):
#     for j in range(1,4):
#         print("A",end=" ")
# print()
'''
i   j

1   1 2 3
2   1 2 3
3   1 2 3
4   1 2 3

12 times


'''

# print("----------------")
# for i in range(1,5):
#     for j in range(1,4):
#         print("A",end=" ")
#     print()

# print("----------------")
# for i in range(1,5):
#     for j in range(1,4):
#         print("i",end=" ")
#     print()

# print("----------------")
# for i in range(1,5):
#     for j in range(1,4):
#         print(j,end=" ")
#     print()


'''
1.

5 5 5 
6 6 6
7 7 7
8 8 8

2.

1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

3.

2 4 6 8
10 12 14 16
18 20 22 24

4.

1 2 3 4
2 4 6 8
3 6 9 12
4 8 12 16


'''


for i in range(1,5):
    k=i
    for j in range(1,5):
        print(k,end=" ")
        k+=i
    print()

print()
for i in range(1,5):
    for j in range(1,5):
        print(i*j,end=" ")
    print()

