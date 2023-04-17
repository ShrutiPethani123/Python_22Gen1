s1={1,2,3,4}
s2={3,4,5,6,7}


s3 = s1.union(s2)
print(s3)


s3 = s1.intersection(s2)
print(s3)

# s1.intersection_update(s2)
# print(s1)

s3 = s1.difference(s2)
print(s3)

# s1.difference_update(s2)
# print(s1)

s3=s1.symmetric_difference(s2)
print(s3)

# s1.symmetric_difference_update(s2)
# print(s1)


print("--------------------------------------")

s4={1,2,3,5,6}
s5={3,5}
s6={55,9,8,12}

print(s4.issubset(s5))
print(s5.issubset(s4))


print(s4.issuperset(s5))
print(s4.issuperset(s4))

print(s4.isdisjoint(s6))
print(s4.isdisjoint(s5))



