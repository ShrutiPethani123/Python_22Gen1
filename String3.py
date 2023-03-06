# s = "Today is Monday"
#    012345678910  14


# print(s.find('d'))
# print(s.find('day'))
# print(s.find('Monday'))
# print(s.find('is'))
# print(s.find('is' , 7))
# print(s.find('is',9,21))

# print(s.index('is'))
# print(s.index('is',20))
# print(s.index('x')) - error


s = "Today is Monday"
#    012345678910  14

# print(s.rfind('day'))
# print(s.rfind('day',3))
# print(s.rfind('day',1,9))
# print(len(s))


# s = "Today is holi"
#    012345678910 11 12
# print(s.find('h'))
# print(s.find('day'))
# print(s.rfind('i'))
# print(s.rfind('i',3))
# print(s.rfind('i',3,7))
# print(s.find('t',7,10))

# print(s.rindex('r'))

# s = "Today is Monday and day after tommorow is holi"
# print(s.split()) - return list
# print(s.split('a'))
# print(s.split('a',4))
# print(s.split('a',2))
# print(s.split('day'))
# print(s.split('day',1))

# l1=s.split()
# print(l1)
# print(" ".join(l1))
# print("-".join(l1))
# print("**".join(l1))

# l= s.split('a',4)
# print(l)
# print(" ".join(l))
# print("a".join(l))

s = "Today is Monday and day after tommorow is holi"
# print(s.partition(" "))
# print(s.partition("a"))
# print(s.partition("and"))
# print(s.partition("is"))
# print(s.rpartition("is"))


s = "&&&&&&&&&&&&*****%%%%%%Today is Monday****** and day after tommorow is holi************"
print(s.lstrip('&'))
print(s.rstrip('*'))
print(s.strip('*'))
# print(s.lstrip('*&').rstrip('**'))
print(s.strip('*%&'))









