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

5.

(j=1)   (j=5)
* * * * * (i=1)
*       *
*       *
*       *
* * * * * (i=5)


6.

*
**
* *
*  *
*   *
****** (i=6)

(j=1) 


7. 
1 2 3 4 5
* * * * * (1)
* *   * * (2)
*   *   * (3)
* *   * * (4)
* * * * * (5)

n=5
primary diagonal -> i=j
secondary Diagonal -> i+j = n + 1
                        i=n+1-j


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

print()
# 5.

for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==5 or j==1 or j==5:
            print("* ",end="")
        else:
            print("  ",end="")
    print()

print()

# 6

for i in range(1,7):
    for j in range(1,i+1):
        if i==6 or j==1 or i==j:
            print("*",end="")
        else:
            print(" ",end="")
    print()


# 7

n=int(input("Enter rows: "))

for i in range(1,n+1):
    for j in range(1,n+1):

        if i==1 or j==1 or i==n or j==n or i==j or i==n-j+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()