'''
packing: it is phenomenon of grouping individual values into a single varible. it can be done on all the collection datatypes
by default python will do packing in the form of tuple collection.

packing is of 2 types:

1.single packing or tuple packing :

it is phenomemon of grouping individuals into a single variable in the form of tuple collection.
a single star or star operator is used before the variable declaration to store in the form of tuple.

def fname(*args):
    print(args)
fname(val1,val2,val3,val4)  # (val1, val2, val3, val4)

# #wap to extract all the integers from tuple collection using packing and unpacking:
# def ext_int(*args):
#     i = []
#     for j in args:
#         if type(j) == int:
#             i.append(j)
#     return i

# print("Extracted integers:", ext_int(1, 'hello', 3.14, 42, 'world', 7))

2.double packing or dictionary packing: 
it is phenomenon of grouping individuals in a form of dictionary collection.(key-value pairs)
to achieve dictionary packing we use double star or double star operator before the variable declaration.

def fname(**args):
    print(args)
fname(a="dress", b=24,x="googly")

where the keys must follow the rules of identifiers and the values can be of any datatype.

variable length arguments:
whenever it is required to pass any number of positional or keyword arguments to a function , 
we make use of varibale length arguments.

def fname(*args, **kwargs):
    S.B
fname()
fname(val1, val2, val3....valn)  # positional arguments
fname(k1=v1, k2=v2, k3=v3....kn=vn)  # keyword arguments
fname(val1, val2, k1=v1, k2=v2, val3, val4)  # mixed arguments

note:
where *args will take zero to n positional arguments and **kwargs will take zero to n keyword arguments.

when duplicate keys are passed it throws an error.
it will not consider key value pair like a normal dictionary.

unpacking:
it is the phenomemon of dividing the collection into individual values
examples:
a,b,c="rcb" 
a #r
b #c
c #b
def fname(a,b,c,d):
    print(a)
    print(b)
    print(c)
    print(d)
fname(*[22,33,44,55])  # unpacking the list into individual values
no of variables must be equal to length of collection.
'''