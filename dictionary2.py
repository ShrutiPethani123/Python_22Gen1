d={
    11:'India',
    12:'USA',
    13:'Canada',
    14:'UK',
    15:'Pakistan'
}

print(d)

# print all the keys

# for i in d:
#     print(i)

# for i in d.keys():
#     print(i)

# for i in d:
#     print(i,d[i])

# for i in d.values():
#     print(i)

# for i in d.items():
#     print(i)

# d[16]='china'
# print(d)

d[12]='USA2'
print(d)

d.update({17:'china'})
print(d)

d[18]='UAE'
d1 = d.copy()
print(d1)

d3=d
print(d3)

d3[13]='russia'
print(d)

d1[12]='usa'
print(d)


