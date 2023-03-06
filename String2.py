'''
s="Java"
s1="Python"
print(s+s1)
print(s.__add__(s1))
print(s1.__add__(s))

s=4
s1=8
print(s+s1)
print(s.__add__(s1))

s=4
s1='cpp'
# print(s+s1) #invalid for differnt data type of s and s1
# print(s.__add__(s1)) #invalid for differnt data type of s and s1

s=4.6
s1=7
print(s+s1)
print(s.__add__(s1))

s=3+4j
# s1=7+6j
s1=5j
print(s+s1)
print(s.__add__(s1))


s="Today is MONDAY"

print("Capitalize: " , s.capitalize())
print("Uppercase", s.upper())
print("Lowercase: ",s.lower())
print("Title: ",s.title())
print("SwapCase: ",s.swapcase())

# String is immutable and ordered.

print(s ,id(s))
# s3 = s.upper()
print(id(s.capitalize()))

'''
# Alignment Methods

s = " Hello Everyone!! Good Evening "
# print(s)
# print(s.center(100))
# print(s.center(100,'$'))
# print(s.center(50,'😕'))
# print(s.ljust(50,'🍔'))
# print(s.rjust(50,'%'))
# print(s.ljust(len(s.rjust(50,'D')),'%'))
# str=(s.rjust(50,'%')).ljust(100,'-')
# print(len(str),str)


# count

s = "Hello Everyone!! Good Evening Hello "
print(s.count('o'))
print(s.count('ll'))
print(s.count('l'))
print(s.count('Hello'))
print(s.count('z'))
print(s.count('Hello',10))
print(s.count('o',10,20))

'''
count(' ' )
count(' ' , start)
count(' ' , start , end)

'''

s = "Hello Everyone!! Good Evening Hello"

print(s.startswith('H'))
print(s.startswith('Hello'))
print(s.startswith('hello'))
print(s.startswith('Hello',4,56))
print(s.startswith('o E',4))
print(s.endswith('H',9))
# print(s.startswith('Hello', ,8)) - invalid








'''
statswith(' ')
statswith(" " , start)
starswith(" ",start,end)


'''

