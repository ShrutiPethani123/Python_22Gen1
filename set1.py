'''


string : ordered and immutable  -> " " or ' ' 
list: ordered and mutable - []
tuple: ordered and immutable  - () 
set: unordered and mutable -{ }

'''


s1 = {1,2,3,4,5}
print(s1)
print(type(s1))

s2={1,4,1,9,5,2.55,"22gen1",True}
print(s2)


s3={1,1,1,5,5,5,1,2,4,6,77,2,34,5,6}
print(s3)

# length:

print(len(s1))
print(max(s1))
print(min(s1))
print(sum(s1))

for i in s1:
    print(i,end=" ")

print()
# print(s1[2]) invalid

print(7 in s1)
print(4 in s1)

print(s1)
s1.add(45)
s1.add(30)
s1.add(35)
print(s1)
s1.add(4)
print(s1)

s2={11,22,33,44,55,1,2,4,5,6}
s1.update(s2)
print(s1)


l=[100,200,200]
s1.update(l)
print(s1)

# s1.remove(200)
# print(s1)

# s1.discard(100)
# print(s1)


# s1.discard(500)
# s1.remove(500)
# print(s1)

# print(s1.pop())
# print(s1)

# s1.clear()
# print(s1)

# del s1
# print(s1)