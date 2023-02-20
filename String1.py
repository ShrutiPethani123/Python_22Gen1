str = "JavaPython"
print(str)

str='python'
print(str)

print("Length of string: ",len(str))

print(str[0])
print(str[1])

# using index
for i in range(0,len(str)):
    print(str[i],end=" ")

# using element
print()
for i in str:
    print(i , end=" ")
print()

s= "Good Morning"
#   0123456789 10 11
#   -12   ... -2 -1

print(len(s))
print(s[5])
print(s[9])
# print(s[12]) - error

print(s[-1])
print(s[-4])
print(s[-12])
# print(s[-15]) - error

# slicing
'''
[start:end]
[start:]
[:end]
[:]
[start:end:step]

'''

s= "Good Morning"
#   0123456789 10 11 
print(s[2:8])
print(s[6:10])

n = s[5:10]
print(n)

print(s[3:])
print(s[:6])
print(s[:])

print(s[3:10:2])
print(s[1:8:3])
print(s[ : : -1])
print(s[8:4:-1])
print(s[8:4:-2])  # 8 6 
print(s[1:5:-2]) # no output




