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
'''
ch=lambda x,y,z,a=0,b=0: a+b+x+y+z
print(ch(*(1,2,3,4,5)))
