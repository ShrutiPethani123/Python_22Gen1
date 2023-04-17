'''
dictionary:

key:value

'''

d1={

    1:"raj",
    2:"joy",
    3:"khush",
    4:"roy"
}

print(d1)
print(d1[2])
print(type(d1))


d2={

    'a':'apple',
    'b':'banana',
    'k':'kiwi',
    'o':'orange',
    'm':'mango'

}

print(d2['a'])
print(d2['m'])
# print(d2['s']) #error

d3={

    '%':'Modulus',
    "'":'Multiplication',
    '+':'Addition',
    '/':"division"
    
}

print(d3['%'])
print(d3["'"])

print(len(d3))

d4={

    'name':'raj',
    'birthdate':'23march2000',
    'age':23,
    'color': ['red','green','blue','yellow'],
    'mobileNo':65735737357,
    'age':25

}

print(d4['color'])
print(d4['color'][2:])

d5=dict(name='royal',city='ahmedabd')
print(d5)

print(d4.get('name'))

print(d4.get('age1'))
# print(d4['age1'])

print(d4.keys())
print(d4.values())
print(d4.items())


d4['name']='khush'
print(d4)

d4.update({'age':30,'birthdate':'25April2000'})
print(d4)

d4.pop('name')
print(d4)

d4.popitem()
d4.popitem()
print(d4)

# d4.clear()
# print(d4)

# del d4
del d4['age']
print(d4)


