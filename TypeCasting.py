"""
Typecasting

int()
float()
str()
bool()
complex()



"""

s="123"
# s="java"
a=int(s)
print(s , type(s))
print(a, type(a))

a=67687
b=float(a)
print(b,type(b))

c=76249816.389
d=str(c)
print(d,type(d))

a=50
a=-39
a=0
a="true"
a="True"
a="False"
a=" "
a=0.0
f=bool(a)
print(f,type(f))
# false -> 0 , 0.0 , ""

a=45
b=complex(a)
print(b , type(b))

a=45
c=5.0
b=complex(a,c)
print(b , type(b))



