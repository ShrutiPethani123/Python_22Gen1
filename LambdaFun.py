def add(n):
    return n+10

print(add(4))

y = lambda n: n+10
print(y(3))

x = lambda a,b : a+b
print(x(2,4))


def fun1(n):
    return lambda a: a**n


# x=fun1(3)  # x = lambda a: a**3
# print(x(2))
print(fun1(4)(2))


