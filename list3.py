l = [2,4,1,5,6,1,3,8,2]

# print(sorted(l))
# print(l)

# l.sort()
# print(l)

# list comprehension

for i in l:
    print(i , end=" ")

print()
# print all even numbers form list
l1=[]
for i in l:
    if i%2==0:
        l1.append(i)

print(l1)

l2 = [j for j in l]
print(l2)

l2 = [j**2 for j in l]
print(l2)

l3 = [i for i in l if i%2==0]
print(l3)
print(i)

for i in l:
    j=i+1
    
print(j)

# make one list of all odd numbers between 20 to 30

print([i for i in range(20,31) if i%2!=0])

'''

1. take one list from user and print all numbers that is divisible by 7 and greater than 20
l = [2,56,14,21,89,36,15,20]
o/p: [56,21]


2.  make one list that contain elements that have 'w' in that element.

l = ['apple' ,' kiwi , 'mango' , 'banana' , 'orange']

l2= ['kiwi']

3. Make one list that contain  all capital elements in list

l2 = [ 'APPLE' , 'KIWI' , 'MANGO' , 'BANANA' , 'ORANGE']


4.  Take one list from user and print only lowecase elements in list.
l = ['Apple' ,'KIWI' , 'mango' , 'banaNA' , 'orange']
o/p: ['mango' , 'orange']

5. Take one list from user in numbers and print sum and average of elements.

l =[1,2,3,4,5]
sum: 15
avg: 3


6. take one list from user and return list that contain sum of all digits in element.

l =[125,23,417,2356]
l2=[8,5,12,16]

7. print cumulative sum.

l = [1,2,3,4,5]
l2 = [1,3,6,10,15]


8. Take one list from user and interchange first and last element of list.

l2 = [1,4,5,7,8,9]
o/p: [9,4,5,7,8,1]


9. Take one list and search user given element is present in list or not.

l2 = [2,5,6,23,7,8,9]

ele: 4 --> Not Found
ele: 7 --> present at index  4


10. Input comma separated string convert into list and after that print sum of all element.

string - 1,2,4,5,6

l = [1,2,4,5,6]
sum: 18






'''

l =['apple' ,'kiwi' , 'mango' , 'banana' , 'orange']

l2=[]
for i in l:
    # if 'w' in i:
    #     l2.append(i)

    # if i.count('w')>0:
    #     l2.append(i)

    if i.find('w')!=-1:
        l2.append(i)

print(l2)

# l3= [i for i in l  if 'w' in i or 'W' in i]
l3=[i for i in l if i.count('w')>0]
print(l3)

l4=[i.upper() for i in l]
print(l4)

l1 = [1,2,3,4,5]
l2=["book", 'pen','pencil']

print(l1+l2)
print(l1)
print(l2)

l1.extend(l2)
print(l1)

l1.append(l2)
print(l1)



# 4.

# l = ['Apple' ,'KIWI' , 'mango' , 'banaNA' , 'orange']

# print([i for i in l if i.islower()])

# 5.

# n = int(input("Enter size: "))
# l1=[]
# for i in range(n):
#     l1.append(int(input("Enter a no: ")))

# print(l1)

# sum=0
# for i in l1:
#     sum=sum+i

# avg=sum/n
# print("Sum: ",sum)
# print("Average: ",avg)


# 6. 

# l =[125,23,417,2356]
# l2=[]

# for i in l:
#     sum=0
#     while(i>0):
#         rem=i%10
#         sum=sum+rem
#         i=i//10
#     l2.append(sum)


# print(l2)


# 7.

# l = [1,2,3,4,5]
# l2=[]
# sum=0
# for i in l:
#     sum=sum+i
#     l2.append(sum)

# print(l2)

# 8.

# l2 = [1,2,3,4,5,8,9]

# tmp = l2[0]
# l2[0]=l2[-1]
# l2[-1]=tmp

# print(l2)


# 9.

# l2 = [2,5,6,23,7,8,9]

# n = int(input('Enter a no: '))

# flag=True
# for i in l2:
#     if(i==n):
#         print("Present at index ", l2.index(i))
#         flag=False
#         break
    
# if flag==True:
#     print("Not Found!!")


# a = l2.count(n)

# if a>0:
#     print('Present at index ',l2.index(n))
# else:
#     print("Not Found!!")


# 10.

# str = input("Enter a string")

# l2 = str.split(',')
# print(l2)

# l3 = [int(i) for i in l2]
# print(l3)

# sum=0
# for i in l3:
#     sum+=i

# print(sum)


l=[1,2,3,4,'a','b','c']
print(sum(l))