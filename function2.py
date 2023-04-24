# default argument

def printData(name,age,college="bvm", city="Ahm"):
    print(name,age,city,college)

printData('raj',32)
printData('joy',12,'daiict','baroda')


# keyword argument

def data(name,age,college):
    print(name , age, college)

data(age=23,name="tom",college="daiict")


# Arbitary Argument(*args)

def marks(*mark):
    print(mark)

marks(1,2,3)
marks(3,2,4,5,78,9)
marks("a",'c',4,5,2.33)

# Arbitary Keyword Arguments(**args)

def fun1(**name):
    print(name['fname'],name['lname'],name['age'])

fun1(fname="raj",age=20,lname="patel")


# def fun2(name , college,*marks,add="ahm"):
#     print(name , college,marks,add)

# def fun2(name , college, add="ahm",*marks):
#     print(name , college,marks,add)

# fun2('roy','iit',23,45,67,89)
# fun2('roy','iit',(23,45,67,89))


def fun2(name , college,*marks,**result):
    print(name , college,marks,result)


fun2('tom','iit',23,45,67,maths=98,science=90)
fun2('tom','iit',23,45,67,maths=98,science=94) 



def fun3(name , age=45):
    print(age)

fun3(50)
# fun3(age=30,'raj') positional argument follows keyword argument
fun3('raj',age=34)


