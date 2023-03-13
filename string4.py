# s = "Today is Monday and day after tommorow is holi"

# print(s.split('d'))
# print(s.partition('day'))
# print(s.rpartition('day'))
# print(s.split('d',2))

# s1 = 'royal'

# print(s1.zfill(7)) # _ _ _ _ _ _ _
# print(s1.zfill(10))
# print(s1.zfill(3))

# dd = input("Enter date: ")
# mm = input("Enter month: ")

# print(f"{dd.zfill(2)}/{mm.zfill(2)}/2022")

# # 03/05/2022


'''

1. Take One string from user and print middle 3 charcter.

s - India
o/p: ndi

s - GOOD
o/p : invalid string

s - JavaPython1
o/p: Pyt



2. Take one string from user and count total number of alphabet , numbers , and special characters.

s - python123java^&$^^

alphabets: 10
numbers: 3
special characters: 5

3. Take one string from user and remove characters by user given index

s - python
ind: 2
o/p: pyhon


4. Take one string from user if it contain minimum 2 uppercase charcater in the first 4 characters  then conver that sting to uppercase

s - PYthon
o/p : PYTHON

s - pyThon
o/p: pyThon

s - RoYAl
o/p: ROYAL


5. Reverse a string

s - Tree
o/p: eerT


6. Take one string from user and print sum of all digits.

s - abcc123gh65
sum: 17


'''

# 1.

# str = input("Enter a string: ")

# if len(str)%2!=0:
#     m=len(str)//2
#     str2=str[m-1:m+2]
#     print(str2)
# else:
#     print("Please Enter valid string!!")



# 2. 

# str = input("Enter a string: ")

# # for i in range(0,len(str)):
# #     print(str[i]+ " ")

# # for i in str:
# #     print(i,end=" ")

# alpha=0
# numbers=0
# symbol=0

# for i in str:

#     if i.isalpha():
#         alpha+=1
#     elif i.isdigit():
#         numbers+=1
#     else:
#         symbol+=1

# print("Alphabets: ",alpha)
# print("Numbers: ",numbers)
# print("Symbol: ",symbol)


# 3.

# str = input("Enter a string: ")

# idx=int(input("Enter index: "))

# # s = str[0:idx]
# # s1 = str[idx+1:]
# # s2 = s+s1
# s2=str[0:idx]+ str[idx+1:]
# # print(s)
# # print(s1)
# print(s2)

# 4.

# str=input("Enter a string: ")

# upper=0
# for i in range(0,4):
#     if str[i].isupper():
#         upper+=1

# if upper>=2:
#     print(str.upper())
# else:
#     print(str)

# 5.

# str=input("Enter a string: ")

# # s = str[::-1]
# # print(s)
# s1=""
# for i in range(len(str)-1,-1,-1):
#     s1+=str[i]

# print(s1)


# 6.

str=input("Enter a string: ")

sum=0
for i in str:
    if i.isdigit():
        sum=sum+int(i)

print(sum)

