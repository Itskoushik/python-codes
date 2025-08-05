'''
def add(a,b,c=0):
    print(a+b+c)
add(1,4,5)

operator overloading:
magic methods/dunder method : any method starting and ending with __ are called as magic methods, it is not necessary 
to call the method explicitly, it will be invoked automatically,because of this it is called as magic method.

operator  name 		operator	    internal operation	
addition		        +	         ob1.__add__(ob2)	
substraction		    -	         ob1.__sub__(ob2)	
multiplication		    *	         ob1.__mul__(ob2)	
true division		    /	         ob1.__truediv__(ob2)	
bitwise not             ~            ob1.__invert__()

operator overloading
it is the phenomenon of making an operator work on user defined class
magic methods have to be explicitly called and pass some implimentation to those magic methods so that 
operators will work on user defined class.

__str__()
when an object is printed it displays the address of that object ,using the __str__() a required value can be printed 
when an object is printed
note:
it has to return only strings


class Weekend:
    def __init__(self,a):
        self.a=a
    def __add__(self,self1): #2 object instances
        return self.a+self1.a #can pass any sort of operation
    def __str__(self):
        return str(self.a) # "bye bye"
ob1=Weekend(10)
ob2=Weekend(20)
print(ob1+ob2)
print(ob2)

encapsulation : its a phenomenon of giving security (wrapping the data) to the members of class.
access specifiers: these are the properties of the class which specifies whether it can be accessed outside the class or not
1.public a.s
2.protected a.s
3.private a.s

public a.s
these are the properties of class which can be accessed inside and outside the class
note: all the previous examples of classes had public a.s

protected a.s
these are the properties of class whichh should provide security to data while accessing outside the class but in 
python protected access specifiers will not provide any security to data.
note: these properties have to be used  only in that particular class even if it is accessible in the derived class
or it is a convension that as a programmer protected a.s should be used only in that class  and avoid using that properties in that 
class

to declare a protected a.s single underscore have to be passed before declaring the property or method
syntax/example:
class python:
    _p=20
ob=python()
print(ob._p)


private access specifiers 
these are the properties of class which can be accessed inside the class 
but cannot be accessed outside the class

__ have to be declared before creating the property or method.
syntax:
class cname:
    __var=value
    def __mname(args):
        s.b
obj=cname(values)
to access the private access specifier outside the class we can make use of name mangling
syntax:
cname/obj._cname__pnames
u can also access the private a.s in other method like display
class Company:
    cname="alphabet"
    ceo="vinayaka"
    __rev=100
    def __init__(self,ename,eid,sal):
        self.ename=ename
        self.eid=eid
        self.__sal=sal
    def display(self):
        print(self.ename,self.eid)
li=Company("likhith",1,1000)
print(li.ceo)
li.dis() 
print(li._Company__sal)


example to perform plus operation between 2 set collection using magic methods

class Sumne:
    def __init__(self,a):
        self.a=a
    def __add__(self1,self2):
        for i in self.a:
            self.a.add(i)
        return self.a
ob1=Sumne({10,20,30})
ob2=Sumne({30,45})

Abstraction:
it is the phenomenon of hiding the implementation or unnecessary things from the user and just give the final functionality work.
to understand abstraction we must know abstract method , abstract class and concrete class.

abstract method:
any method which contains only function declaration but doesnt contain function definition is called as abstract method

abstract class:
if a class contain atleast 1 abstract method it is called as abstract class.



syntax:
from abc import ABC,abstractmethod
class hero(ABC):
    @abstractmethod
    def zero():
        pass
    @abstractmethod
    def zoro(args):
        pass
note: abc is a package name (folder) and ABC is a class , abstract method is a decorator
from abc package ABC class and abstract method have to be imported to create abstract class in python .

concrete class:
if a class doesnt contain any abstract class is called concrete class.


object cannot be created for an abstract class.
to convert abstract class into concrete class 

to inherit the abstract class into a new class by passing implementation for all the abstract methods

from abc import ABC,abstractmethod
class hero(ABC):
    @abstractmethod
    def zero():
        pass
    @abstractmethod
    def zoro(args):
        pass
        
class demon(hero):
    def zero(self):
        print("enter details")
    def zoro(self):
        print("enter your message")
ob=demon()





to access or modify private access specifiers(object members) property decorator have to be used

property decorator:
it is a decorator which is used to access a method like property/function (method like a variable)
we have getters,setters,deleter to perform operation
syntax
class cname:
    def __init__(self):
        pass
    @property #getter
    def mname(self):
        self.__pname
    @mname.setter
    def mname(self,val):
        self.__pname=val
    @mname.deleter
    def mname(self):
        del self.__pname
        
        
example:
class New:
    def __init__(self,a,b):
        self.a=a
        self.__b=b
    @property
    def b(self):
        print(self.__b)
    @b.setter
    def b(self,new):
        self.__b=new
    @b.deleter
    def b(self):
        del self.__b
ob=New(10,20)

write a program which returns true if the integer number is even, if not return false.

def even(n):
    if n%2==0:
        return True
    else:
        return False
    
class Even:
    def __init__(self,n):
        self.n=n
    def even(self):
        if self.n%2==0:
            return True
        else:
            return False
    
ob=Even(12)
print(ob.even())


lambda : it is a keyword which acts like an anonymous function in python to perform simple operations .
var=lambda args: expression 
print(var(value))

write a program to check the number is even or odd 

even= lambda n:n%2==0
print(even(3))


or 



def even(n):
    return n%2==0
    
    
    write a program to find sq of a interger number
    
    
sq= lambda n:n**2
print(sq(value))

def sq(n):
    return n**2
    
wap to get a sq of integer number if it is odd number, if its even number get its cube
sq=lambda sq:sq**3 if sq%2==0 else sq**2
print(sq(2))

wap to print the characters present at even index if the string is palindrome , if not print the reversed string

ch=lambda x:x[::2] if x==x[::-1] else x[::-1]
print(ch("xox"))

write a program to find the greater of two interger numbers 

ch=lambda x,y:x if x>y else y
print(ch(3,4))

wap to check the first character of the string is uppercase, lowercase or digit or special char
ch=lambda x:f"{x[0]} is uppercase" if x[0].isupper() else f"{x[0]} is lowercase" if x[0].islower() else f"{x[0]} is digit" if x[0].isdigit()  else f"{x[0]} is specialcase"

print(ch("@"))  

wap to find sum of minimum 3 interger and max five interger 
ch=lambda x,y,z,a=0,b=0: a+b+x+y+z
print(ch(*(1,2,3,4,5)))


map() function
it is inbuilt function which is used to execute or perform same set of operation
for every value in the collection .
syntax:
var=map(fname,call)
print(datatype(var))

example:
sqr=lambda n:n**2
sqr_range= map(sqr,range(1,11))
print(list(sqr_ramge))

or 

print(list(map(lambda x:x**(1/2),range(1,11))))
print(list(map(lambda x:x**2,range(1,11))))

write a prog to extract all the upper case characters in string collection
wap to store len of every word present in string collection 
print(list(map(len,input("enter the string: ).split())))
wap to store word and its length as key value pair from string collection 

print(dict(map(lambda x:(x,len(x)),input("enter the string: ").split())))


{'hello': 'olleh', 'world': 'dlrow', 'koushik': 'kihsuok'}
print(dict(map(lambda x:(x,x[::-1]),input("enter the string: ").split())))


wap to get following output :
{'HELLO': 'olh', 'WORLD': 'drw', '90': '0'}
print(dict(map(lambda x:(x,x[::-2].lower()),input("enter the string: ").split())))
or
print(dict(map(lambda x:(x.upper(),x[::-2]),input("enter the string: ").split())))


wap to store number and its factorial as key value pairs between the range 1,5
def fact(n):
    p=1
    for i in range(1,n+1):
        p*=i
    return p
    
print(dict(map(lambda x:(x,fact(x)),range(1,6))))


# class Payment:
#     mod=["1.credit card","2.debit card","3.UPI transaction"]
#     def __init__(self):
#         self.credit_limit=float(input("enter the credit limit : "))
#         self.debit_balance=float(input("enter the debit balance : "))
#         self.upi_balance=float(input("enter the upi wallet balance : "))
        
#     def display_pay(self):
#         for i in self.mod:
#             print(i)
#     def process_pay(self):
#         self.display_pay()
#         ch=int(input("enter ur payment mode: "))
#         amt=float(input("enter the amount: "))
#         if ch==1:
#             print(".......please enter the credit card details.... ")
#             name=input("enter the name on card") 
#             digi=int(input("enter the last 4 digits of the credit card: "))
#             cvv=int(input("enter the 3 digit cvv pin : "))
#         if ch==2:
#             print(".......please enter the debit card details.... ")
#             name=input("enter the name on card") 
#             digi=int(input("enter the last 4 digits of the debit card: "))
#             cvv=int(input("enter the 3 digit cvv pin: "))
#         if ch==3:   
#             print(" .......please enter the upi id.... ")
#             upi=input("enter the upi id: ") 
            
# def main():
#     ob=Payment()
#     ob.process_pay()
    
                

# if __name__=="__main__":
#     main() 



wap to extract all the upper case character from string collection
print("".join(list(filter(lambda a:a.isupper(),input("enter the string: ")))))
print(dict(map(lambda x:(x,x[::-1]),filter(lambda a:len(a)%2==0,input("enter the string: ").split()))))



generators()
it is a function which is used to generate sequence of values using yield keyword .
when a yield keyword is present in a user defined function, it becomes a generator function.
def mauve():
    print("talk")
    yield "tsunami"
    print("walk")
    yield "jujjubi"
    print("pass")
    yield "bimar"
print(list(mauve()))  

1.diff between return and yield

return 
it is a keyword which is used to terminate a function execution
it will not execute the next instructions
typecasting is not required to get output
it used in normal udf 
yield
it is a keyword used to pause the function execution,it continues to execute the next set of instructions
typecasting is required to get output
it is used in generator function


wap to extract all the integers from list
print(list(filter(lambda x:type(x)==int,eval(input("enter :")))))
def ext(l):
    for i in l:
        if type(i)==int:
            yield i
print(list(ext([1,2,4,"bimar","badmash","kitab"])))


wap to generate all the lowercase characters in a list
# def low():
#     for i in range(97,123):
#         yield chr(i)
# print("".join(list(low())) 
wap to generate nth fibonacci series 

# def fibo(n,a=0,b=1):
#     for i in range(n):
#         yield a
#         a,b=b,a+b
# print(list(fibo(int(input("enter : ")))))

wap to generate prime numbers between the range 2-100

def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
    
def prime_range():
    for i in range(2,101):
        if prime(i)==True:
            yield i
                
print(list(prime_range()))

decorator: it is a function used to add extra features to the existing functions without modifying it .
a decorator is used on functions  when they have common pre and post task and it is not mandatory to have them both .
it is of two types:
inbuilt and user defined decorators

inbuilt decorators are the decorators which are predefined by the developers 
ex: @classmethod,@staticmethod,@property

udd: these are the decorators which are created on user requirement 
syntax:
def deconame(func):
    def inner(*args,**kwargs):
        pretask
        func(*args,**kwargs)
        posttask
    return inner
    
    
example:
def insta(func):
    def inner(*args,**kwargs):
        print("------login------")
        func(*args,**kwargs)
        print("------logout------")
    return inner


@insta
def darshan():
    print("hello")
    print("bemar pessi")
    print("bemar pessi")
    
@insta   
def siraj():
    print("pressure")
    print("what pressure")
    
darshan()
siraj()
 
 
wap which calculate the total execution time  of program

import time

def execute_time(func):
    def inner(*args,**kwargs):
        t1=time.time()
        func(*args,**kwargs)
        t2=time.time()
        print()
        print("execution time :",t2-t1,sep=" ")
    return inner

@execute_time   
def siraj():
    print("pressure")
    print("what pressure")
    
siraj()


wap to give 5 sec delay before executing any program
import time

def execute_time(func):
    def inner(*args,**kwargs):
        time.sleep(5)
        func(*args,**kwargs)
    return inner

@execute_time   
def siraj():
    print("pressure")
    print("what pressure")
    
siraj() 


wap which returns positive results when arithmetic opearation is performed

'''

import time

def positive(func):
    def inner(*args,**kwargs):
        return abs(func(*args,**kwargs))
    return inner

@positive  
def add(a,b):
    return a+b

@positive
def mul(a,b,c):
    return a*b*c
    
    
print(add(10,20))
print(mul(10,20,-30))
 


