'''
def fname(arg1,arg2,arg3......argn,k1=v1,k2=v2,.......kn=vn)
   s.b
fname(val1,val2,vsl3...valn)
fname(val1,val2,val3...valn,v1,v2,v3.....vn)
fname(val1,val2,val3,val4...valn,k1=v2,...kn=vn)
      positional argument    keyword argument
      
arguments are the values which are passed to the function when it is called.
they are of 5 types:
1. positional arguments: which are passed to the function in the order they are defined in the function.
2. keyword arguments: which are passed to the function with the name of the parameter.
3. default arguments or non mandatory args: which are passed to the function with the default value if the argument is not passed.
4. variable length arguments: which are passed to the function with a variable number of arguments.
5. mandatory arguments: which are passed to the function and are required to be passed.
default arguments and keyword arguments are passed at the end of the function call.
when a required arguments have to be passed by skipping other arguments it should be mentioned as key value pair  

example of positional arguments:
def add(a, b):
    return a + b
add(2, 3)  # positional arguments

example of keyword arguments:
def add(a, b):
    return a + b
add(a=2, b=3)  # keyword arguments
example of default arguments:
def add(a, b=5):  # b is a default argument
    return a + b
add(2)  # b will take the default value of 5

example of variable length arguments:
def add(*args):  # *args is used to pass a variable number of arguments
    return sum(args)  # sum of all the arguments passed
def add(*args, **kwargs):  # *args is used to pass a variable number of arguments and **kwargs is used to pass keyword arguments

example of mandatory arguments:
def add(a, b):  # a and b are mandatory arguments
    return a + b
# add(2, 3)  # mandatory arguments

def passport(name,dob,adhaar,pan,gender,phone,addr,altphone=None, per_addr=None):
    print("Passport details:")
    print(f"Name: {name}")
    print(f"DOB: {dob}")
    print(f"Adhaar: {adhaar}")
    print(f"PAN: {pan}")
    '''
#wap or create a function which finds the sum of minimum 2 integers and maximum 5 integers:
# def sum_integers(a,b,c=0,d=0,e=0):
#     sum = a + b + c + d + e
#     print(sum)
# sum_integers(1,2,4,5)

def count_vowels(s,si=0,ei=None):
    if ei == None:
        ei = len(s)-1
    vowels = "aeiouAEIOU"
    count = 0
    for i in range(si, ei+1):
        if s[i] in vowels:
            count += 1
    return count
print(count_vowels("pandupura Bharatha",4,8))  

#wap to create a function which does the following : which is string slicing operation