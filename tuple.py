'''

string : ordered and immutable  -> " " or ' ' 
list: ordered and mutable - []
tuple: ordered and immutable  - () 

'''

t1 = (1,2,3,4,5)
print(t1)
print(type(t1))

# duplication ? - allow

t1 = (1,2,3,1,2,34,5)
print(t1)

t2=('india','canada','usa','japan')
print(t2)

t3=(2,4.5,'japan',4.678)
print(t3)

t4=(2,4.5,'japan',4.678,[2,3,5])
print(t4)


# t5 =('raj')
t5=(1)
print(t5)
print(type(t5))

t5 =('raj',)
print(t5)
print(type(t5))


print("---------------------------------------------------------------------")
t6=(12,34,12,56,78,23,69)

print(t6[0])
print(t6[3])
print(t6[5])


print(t6[-1])
print(t6[-3])

print(t6[1:6])


str="Python"
print(str[1:4])

str1=[1,2,5,3,6,7]
print(str1[1:4])

print(t6[1:4])

t6=(12,34,12,56,78,23,69)
print(t6[1:7:-3]) # ()
print(t6[2:-3]) #
print(t6[2:-3:-1])
print(t6[-3:4:-1])


# t6 = 12,13,1.4,1,7,"java",56
# print(t6)

t6=(12,34,12,56,78,23,69)
print(len(t6))
print(max(t6))
print(min(t6))
print(sum(t6))

# change the value of tuple

# t6[1]=67
# print(t6)

# str="India"
# str[0]='k'
# print(str)

print("t6: ",id(t6))
t6 = list(t6)
print(t6,type(t6))
t6[2]=20
t6 = tuple(t6)
print(t6)
print("t6: ",id(t6))


t2=('india','canada','usa','japan')
# t2=('india','canada','usa','japan',china)

for i in t2:
    print(i)

i=0
while i<len(t2):
    print(t2[i])
    i+=1


t1=(1,2,3)
t2=(4,5,6)

# t3 = t1*2
t3=t1*4
print(t3)

str="java"
print(str*4)

# t3=t1+t2
# print(t3)

# count() , index()
print(t3.count(1))
print(t3.count(7))

print(t3.index(2))
print(t3.index(2,2,7))
# print(t3.index(9))


t1=(2,4,5,6,7)
t2=('raj','roy','khush')
t3=(5,6,7,8,9,0)

t3 = tuple(zip(t1,t2,t3))
print(t3)


# unpack

t1=('Gujarat','Maharastra','Delhi','Punjab','Kerala','Goa')
a,b,c,d,e,f = t1

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)

# a,b,c,d = t1 - error

# a,b,*c = t1
# print(a)
# print(b)
# print(c)


# a,*b,c = t1
# print(a)
# print(b)
# print(c)

a,b,*c,d,f = t1
print(a)
print(b)
print(c)
print(d)




t1=('Gujarat','Maharastra','Delhi','Punjab','Kerala','Goa')

'''

o/p:

Gujarat
Maharastra
[delhi,Punjab]
Kerala
Goa

a,b,*c,d,e

1. check the delhi is present in tuple or not. if present then print present  at which index otherwise print not Found!!

2. t=(2,4,6,7,8,9,0,1,2,3,4,6,7)
    reverse this tuple.

3. t=((1,2,3),(4,5,6),(2,6,7,4),(1,6,7,8))
    print sum of all tuples.
    t=(6,15,19,22)

4.  t1= (1,2,3,4)
    t2= (2,3,4,5)
    t3= (3,4,1,2)

    o/P: t4=(6 , 9 , 8 , 11)

''' 

t1=('Gujarat','Maharastra','Delhi','Punjab','Kerala','Goa')

# if 'Delhi' in t1:
#     print("Present at index: ",t1.index('Delhi'))
# else:
#     print('Not Found!!')

t2 = tuple(i*2 for i in t1)
print(t2)

t2=(3,4,5,7,8)
t3=tuple(i**2 for i in t2)
print(t3)

t4 = tuple(i for i in t2 if i>5)
print(t4)


# 3.
t=(2,4,6,7,8,9,0,1,2,3,4,6,7)
print(t[::-1])
t2 = tuple(reversed(t))
print(t2)


t=((1,2,3),(4,5,6),(2,6,7,4),(1,6,7,8))

t2 = tuple(sum(i) for i in t)
print(t2)

# 4.
t1= (1,2,3,4)
t2= (2,3,4,5)
t3= (3,4,1,2)

t4 = tuple(zip(t1,t2,t3))
print(t4)
t5 = tuple(sum(i) for i in t4)
print(t5)






