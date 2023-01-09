'''
1. Aritmetic Operator ( + - * / %  **  //)
2. Logical Operator (and , or , not)
3. Relational Operator (< > <= >=  == !=)
4. Assignment Operator ( =  += -= *= /= &= |= ^= %=)
5. Bitwise Operator (&  |  ^  ~  << >> )
6. Membership Operator ( in  , not in)
7. Identity Operator (is , is not )


-> ++ , --  -> operators are not there in python

a+=1
a-=1

'''
# a=int(input('Enter a no: '))
# b=int(input("Enter a no:"))

# print('Addition of',a,'and',b,'is',a+b)
# print(f'Addition of {a} and {b} is {a+b}')
# print("Addition of {} and {} is {}".format(a,b,a+b))

# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# # a=4 , b=5
# print(a//b)
# print(a**b) #a^b

"""
a/b = 4/5 = 0.8

floor(0.8) -> 0
ceil(0.8) -> 1


floor(-3.5) -> -4
ceil(-2.5)-> -2

-4 -3 -2 -1 0 1 2 3 4 5 

"""

"""
2. Logical Operator


and  - sign up time Username and password both should be right

F - False
T - True

A   B   A and B

F   F   F
F   T   F
T   F   F
T   T   T


or - Login using Email , Google , Facebook


A   B   A or B

F   F   F
F   T   T
T   F   T
T   T   T

not 

A   not A

T       F
F       T


"""

# a=54
# b=34
# c=23

# print(a>b and b<c) # T and F -> F
# print(a<c and b==d)

# print(a>b or c>a) #T 
# print(c<b or x>y)
# print(c>b or a<b)

# print(not a>b)
# print(not (a>b and b<c))

'''
4. Assignment Operator ( =  += -= *= /= &= |= ^= %=) - shorthand notation

'''

# a=5
# # 5=a - invalid

# b=4
# # b=b+3
# b+=3 # b = b+3
# print(b)

# c=5
# c-=3
# print(c)

# d=6
# d*=4
# print(d)


"""
5. Bitwise Operator (&  |  ^  ~  << >> )

&

A   B   A & B

0   0   0
0   1   0
1   0   0
1   1   1


1024    512    256         128     64   32    16          8    4    2    1



12 -> 1100
15 -> 1111
36 -> 0010 0100
23 -> 0001 0111
112 -> 0111 0000
127 -> 0111 1111


1111 -> 8+4+2+1 = 15
0010 1010 -> 42
0111 1100 -> 124


15 -> 0000 1111
      &&&& &&&&
28 -> 0001 1100

-----------------
      0000 1100 (12)


|

A   B   A | B

0   0   0
0   1   1
1   0   1
1   1   1

15 -> 0000 1111
      |||| ||||
28 -> 0001 1100

-----------------
      0001 1111 (31)


^

A   B   A ^ B

0   0   0
0   1   1
1   0   1
1   1   0

15 -> 0000 1111
      ^^^^ ^^^^
28 -> 0001 1100

-----------------
      0001 0011(19)


13 -> 0000 1101

13<<1  -> 0001 1010 (26)
13<<2  -> 0011 0100 (52)
13<<3  -> 0110 1000 (104)


n<<m -> n*(2^m)


13>>1 -> 0000 0110 (6)
13>>2 -> 0000 0011 (3)
13>>3 -> 0000 0001 (1)
13>>4 -> 0000 0000(0)


n>>m -> n/(2^m)

"""

# print(15&28)
# print(15|28)
# print(15^28)
# print(13<<1)
# print(13<<2)
# print(13<<3)
# print(13>>1)
# print(13>>2)
# print(13>>3)
# print(13>>40)

"""
6. Membership Operator ( in  , not in)

"""

l1 = [1,5,6,8,3,8,5]
l2=[3,4,5,90,45]
l3=[4,1,5,6]

print(id(l1))
print(id(l2))
print(id(l3))

l1=l3
print("---------------")
print(id(l1))
print(id(l2))
print(id(l3))

print(l1 is l2)
print(l1 is l3)




# print(5 in l1)
# print(5 not in l1)


