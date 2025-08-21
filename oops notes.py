'''
oops in python.
in python we can do 3 types of programming that is procedural , functional and object oriented programming
"To map with real world scenarios we started using objects in code"
this is called object oriented programming ,

the main advantage of using oops is a project will be in an organised manner.
resuing the code using inheritance,providing multiple functions using polymorphism , hiding unneccesaary data using abstraction,providing security to the data using 
encapsulation

in oops we use class and object. it is collection of variable and methods,
class: it is a blueprint which consists of properties of real time objects or real time entity
object:it is an instance of class.or it is a varible created for the class

class is of 2 types:

-inbuilt and user defined class:
inbuilt class:
these are the classes which are pre-defined by the developers like int,str,list,tuple,set, etc
user defined class:
it is the classes which are defined based on user requirement .

now as we know we have been doing procedural programming in python 
like for example:-~
a=10
b=10
sum=a+b
print(sum)
diff=a-b
print(diff) #execution is happening line by line as we were also
writing it line by line 

uske baad aaya functions ryt jismai we made sure to maintain the data redundancy (reduce)
and improve code reuseability (increase)

as we have seen we successfully moved from procedural to functional 
programming which is better and as we know we always want the best so we went to oops.
which is object oriented programming.

now lets dive deep into the topic which is object and class.
object:
rough example: what is object ? this laptop is a object?, my keyboard is an object
so basically we can say we can make anything an object but before that we would need to 
define a class in oops.

class is like a blueprint like a plan of 30*40 flat . using this class we can create multiple objects init

now lets jump to actual definition of class:
 
its a blueprint for creating objects

chalo abhi mai ek example deta hu , for example we have a class of students 
and i want to store the names of students in the class register , we can use the concept of class and objects
for example:
class Student: #first char of the class name must be in uppercase
    name="karan" # let us suppose ki saare bacho ka naam karan hai ryt
s1=Student() # the object instance (here we are explicitly telling python kaka that bhaiya s1 is my instance of Student class)
print(s1) # prints that we have created a object of Student class at some mem address
print(s1.name) #prints the name which is karan
s2=Student()
print(s2.name)

this was simple ryt lets look up with another example 
class Car:
    color="black"
    brand="mercedes"
car1=Car() #object created or instance of the class is created
print(car1.color)
print(car1.brand)

#constructor------> while object creation it is invoked.it is a special function which is used to initialize the attributes of the class.
__init__ function:
all classes have a function called __init__(), which is always executed when the object is being initiated .


for example:
class Student:
    name="karan" 
s1=Student() here 
print(s1.name)
s2=Student()
print(s2.name)
# it is very impoertant to understand what is happening here ryt
by default python being very smart is applying the init function by itself and creating a object

if were told to write a contructor by ourselfs then we can also do that
like

class Student:
    name="karan"
    def __init__(self): # gets called by itself or gets invoked my itself
        print(self) #prints the object is created successfully at a mem loc
        its similar to s1=Student() where we are creating the instance of the class ryt
        both points towards same mem loc
        print("adding new student in db...")
s1=Student() #the parenthesis is used to call the constructor
print(s1)
one more important thing abt constructors are that it uses a parameter or argument  called as self parameter
first parameter which is defined in init function is self

self:      


class Student:
    def __init__(self,fullname): # gets called by itself or gets invoked my itself. we can give any name to the parameter self 
    but it is a convention to use self,because it refers to the instance of the class.
        self.name=fullname #here we are assigning the fullname to the name attribute of the class.
        # self is a reference to the current instance of the class.
        # what is attribute?
        attribute is a variable which is defined inside the class and is used to store the data of the object.
        print("adding new student in db...")
s1=Student("karan") #the parenthesis is used to call the constructor
print(s1.name) #karan



also here is one more example
class Student: #here __init__ is a constructor which is used to initialize the attributes of the class
    def __init__(self, name, marks): #here we are defining a constructor which takes two parameters name and marks
        self.name = name
        self.marks = marks 
        print("adding new student in Database..")

s1 = Student("karan", 97)
print(s1.name, s1.marks)  # karan 97

s2 = Student("arjun", 88)
print(s2.name, s2.marks)  # arjun 88

class is collection of variables and methods which are used to define the properties and behaviour of the object.

contructors are of two types:
1. default constructor: which takes no parameters and initializes the attributes of the class with default values.
for example:
class Student:
    def __init__(self):  # default constructor
        pass  # here we are not initializing any attributes of the class
example 2 :
class Student:
    def __init__(self, name="karan", marks=0):  # default constructor with default values
        self.name = name
        self.marks = marks 
        print("adding new student in Database..")
        
2. parameterized constructor: which takes parameters and initializes the attributes of the class with the values passed as arguments.
example:
class Student:
    def __init__(self, name, marks):  # parameterized constructor
        self.name = name
        self.marks = marks 
        print("adding new student in Database..")
        
class and instance attributes:
class attributes are the variables which are defined inside the class and are used to store the data of the object.
whereas instance attributes are the variables which are defined inside the constructor and are used to store the data of the object.

object attributes are the variables or properties that are associated with an object.

now lets look at the example of class and instance attributes
for example:
class Student:
    school_name = "ABC School"  # class attribute
    def __init__(self, name, marks):  # constructor # here self is a reference to the current instance of the class.
        self.name = name  # instance attribute 
        self.marks = marks  # instance attribute
        
    as we know name and marks are different for all the students but school name is same for all the students.
    so we can say that school_name is a class attribute and name and marks are instance attributes.
    
    when class attribute and object attribute have same name then object attribute takes precedence over class attribute.
    
    
    class mein do cheeze store hoti hai:
    1.data (attribute): class ki kya kya properties hai ya fir i can say which is used to store the data of the object or attributes of the class.
    2.methods: which are the functions which are used to define the behaviour of the object.
    or in simple words we can say that methods are the functions which are defined inside the class and are used to perform some operations on the data of the object.
    
    for example:
    class Student:
        def __init__(self, fullname):
            self.name = fullname
        def hello(self):  # method
            print("hello", self.name)  or print(f"hello {self.name}")
            here self is a reference to the current instance of the class.
    s1 = Student("karan")
    s1.hello()  # hello karan
      
lets solve a q on it
class Student:
    def __init__(self, name, marks): #we consider marks is a list of marks
        self.name = name
        self.marks = marks
    def get_avg(self,sum=0):
        for i in self.marks:
            sum += i
        print(f"average marks of {self.name} is {sum/len(self.marks)}")
s1=Student("karan", [90, 80, 70, 60])
s1.get_avg() 

s1.name="ironman" #we can change the attribute value or manipulate them at any instance of time.
s1.get_avg()  # average marks of ironman is 75.0 

static methods:
these are the methods that dont use the self parameter(works at class level)
as we can see we dont need objects so what we do is we try to work at class level
class student:
    @staticmethod #decorator to define a static method
    def hello():
        print("hello from static method")
        
    decorators: it allows us to wrap a function or method in 
    another function or method to modify its behaviour permanently.
    
pillars of oops:
1.abstraction: hiding the implementation details and showing only the essential features of the object.
2.encapsulation: bundling the data and methods that operate on the data within a single unit or class.

class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
    def start(self):
        self.clutch=True
        self.acc=True
        print("car started...")
        
car1=Car()
car1.start()    

this is called abstraction where we are hiding the implementation details or code and just delivering essemtial features of the object to user.   
   
encapsulation:
we try to create a capsule of the data + functions

practice q

class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.accountno=acc
    def debit(self,amount):
        self.balance-=amount
        print("rs.",amount,"was debitted")
        print("total balance",self.get_balance())
    def credit(self,amount):
        self.balance+=amount
        print("rs.",amount,"was creditted")
        print("total balance",self.get_balance())
    def get_balance(self):
        return self.balance

acc1=Account(10000,12345)
# print(acc1.balance)
# print(acc1.accountno)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)

# class Student:
#     def __init__(self, name, marks):  # parameterized constructor
#         self.name = name
#         self.marks = marks 
#         print("adding new student in Database..")
#         print(self)
# ob=Student("ram",1)
# print(ob)


when class is created it internally divides the memory like key value pairs .
all the properties will be stored in that memory layer.
each property will have a reference address.
the key layer will have an address which will be stored with respect to class name .
when an object is created for a class all the properties of class will be derived to object.
the key layer of object dictionary will have an address which will be stored with respect to object name.
syntax:
access:cname/objectname.pname
modify:cname/objectname.pname=value

key space          | value space
hero
x099

class hero:
    a=10
ob=hero()
ob.a=30
hero.a=20

note:
if a property is modified with respect to classname , will effect all the objects.
if it is modified with respect to an object it effects only for that particular object.

class properties:these are the properties or members which are common for each and every object.
object members are the specific members which are different for every object
example:if a python class is considered as class , students are objects
classname- a1
object-students
cmem-chairs,nannu , board
ob.mem- name , dob , area, phone 

#create a class called suiiiiii with minimum 5 class properties,6 object properties, 3 objects,print the properties of all objects


class Rm:
    rm="realmadrid"
    lw="karim benzema"
    rw="zizou"
    fwd="david beckam"
    gk="Navas"
    def __init__(self,pos,name,st="Cristiano Ronaldo",cb="roberto carlos",lb="marcelo",rb="sergio ramos"):
        self.pos=name
        self.st=st
        self.cb=cb
        self.lb=lb
        self.rb=rb
p1=Rm("lw","vini jr")
p2=Rm("rw","rodrigo")
p3=Rm("mf","tony kroos")
print(p1.cb,p1.gk,p1.rb,p1.pos,p1.fwd,sep="\n")


types of method:
1.object method : it is method used to access and modify the object members
2.class method : it is used to access and modify the class members
3.static method

object method example:
class Love:
    def __init__(self,lover1,lover2):
        self.name1=lover1
        self.name2=lover2
    def display(self):  #object access
        print(f"{self.name1} is in love with {self.name2}")
    def affair(self,lover3):    #object modification
        self.name2=lover3
r1=Love("Juliet","romeo")
r2=Love("radha","krishna")
r3=Love("anuska","virat")
r4=Love("sai palavi","ram")
r1.display()
r2.display()
r3.display()
r4.display()
r4.affair("cheeku")
r4.display()
Love.display(r2)


class method example:

class Love:
    lovetyp="relationship"
    nop=2
    tor="5 yrs"
    
    def __init__(self,lover1,lover2):
        self.name1=lover1
        self.name2=lover2
    @classmethod
    def display(cls):  #class access
        print(f"{cls.nop} are in {cls.lovetyp} for {cls.tor}")
    @classmethod
    def new_tor(cls):    #class modification
        ntor=input("enter the new tor: ")
        cls.tor=ntor
Love.display()
r3=Love("anuska","virat")
r3.display()
Love.new_tor()
Love.display()

class Love:
    lovetyp="relationship"
    nop=2
    tor="5 yrs"
    
    def __init__(self,lover1,lover2,status):
        self.name1=lover1
        self.name2=lover2
        self.status=status
    
    def display(self):  #object access
        print(f"{self.name1} is in love with {self.name2} and are {self.status}")
        
    def breakup(self,status="divorse"):    #object modification
        self.name2=status
        print(f"{self.name1} has given divorse to {self.name2}")
        
    def affair(self,lover3):    #object modification
        self.name2=lover3
    @classmethod
    def display_cls(cls):  #class access
        print(f"{cls.nop} are in {cls.lovetyp} for {cls.tor}")
    @classmethod
    def mod_class(cls):    #class modification
        new=input("enter the class method name:  ")
        if new=="tor":
            ntor=input("enter the new time of relationship :  ")
            cls.tor=ntor
        elif new=="nop":
            nnop=int(input("enter the no of people in love :  "))
            cls.nop=nnop
        elif new=="lovetyp":
            nlovetyp=input("enter the current status :  ")
            cls.lovetyp=nlovetyp
        else:
            print("correct class name")
            
            
        
            
Love.display_cls()
r3=Love("anuska","virat","married")
r3.display_cls()
Love.mod_class()
Love.display_cls()



static method
it is method which neither belong to class or object members but it plays a supportive role for both class method and object method
it is not necessary to pass self/self as argument.
static method decorator have to be used before the function declaration 
note:
it is not necessary to call static method outside the class .

it is used to access inside the class
by using 
self.mname(args)


syntax
class x:
    -----
    -----
    -----
    @staticmethod
    def mname(arg1,arg2...argn):
        S.B
        
obj=cname(values)

example: bank

class HDFC:
    def __init__(self,bal,acc):
        self.balance=bal
        self.accountno=acc
    def debit(self,amount):
        if self,balance>=amount:
            self.balance-=amount
        print("rs.",amount,"was debitted")
        print("total balance",self.get_balance())
    @staticmethod
    def add(a,b):
        return a+b
    def credit(self):
        amount=int(input("enter the amount to be credit: "))
        self.balance=self.add(self.balance,amount)
        print("rs.",amount,"was creditted")
        print("total balance",self.get_balance())
    def get_balance(self):
        return self.balance


create a class called library with basic methods and properties,
add or create methods like issue book,and return book , a person can take only 4 books

 
class Lib:
    librarian="ariana grande"
    books={"Mahabharata":10,"Ramayana":5,"harry puuter":7,"One piece":3}
    def __init__(self,stname,phno,book={}):
        self.stname=stname
        self.phno=phno
        self.book=book
        
         
    @classmethod
    def display_book(self):
            print(self.books)
    
    def issue(self):
        print(self.books)
        bk=input("enter the bookname: ")
        if bk in self.books:
            if self.books[bk]>0 and len(self.book)<=5:
                print(f"{bk} is successfully issued!!")
                self.book[bk]=1
                
                self.books[bk]-=1
                print(self.books)
            else:
                print(f"{bk} is out of stock!!!")
        else:
            print(f"{bk} is not available in library!!! ")
        
ob=Lib("kishore",9888567802)
ob.issue()
    
pillars of oops:
1.inheritance:
it is the phenomemon of deriving the properties from one class to another class.
the class from where properties are derived is called as parent class, super class,base class
class to which properties are derived is called as child class, sub class, derived class

example:
parent class
    |
    |
    |
child class

advantages:
it reduces the instructions. 
it reduces the code repeatation 
it improves efficiency of the program
it reduces time and effort consumed by a programmer.

types of inheritance:
1.single level inheritance
2.multi level inheritance
3.multiple inheritance
4.heirachial inheritance
5.hybrid inheritance

single level inheritance
it is phenomenon of deriving properties from 1 parent class to 1 child class,
syntax:
class pc:
    sb
class cc(pc):
    sb
    
diagram:  
parent class
    |
    |
    |
child class

class Thaatha:
    d=7
    def __init__(self,a,b):
        self.a=a
        self.b=b
class Ban(Thaatha):
    y=2
csk=ban(16,5)




constructor chaining : it is the phenomenon of calling the init method of parent class from child class.

syntax:
super().__init__(args)
super(child,self).__init__(args)
pname.__init__(self,args)


class Thaatha:
    d=7
    def __init__(self,a,b):
        self.a=a
        self.b=b
class Ban(Thaatha):
    y=2
    def __init__(self,a,b,p,q,r):
        super().__init__(a,b)
        self.p=p
        self.q=q
        self.r=r
csk=ban(1,2,3,4,5)

method chaining:
it is the phenomenon of calling the method of parent class to child class.
super().mname(args)
super(child,self/cls).mname(args)
pname(mname(self,args))

multilevel inheritance:
it is the phenomenon of deriving properties from 1 class to another by considering more than 1 level.


class a:
    x=8
class b(a):
    y=3
    p=18
    x=99
class c(b):
    t=11
    k=45
ob1=c()
print(ob1.x)


class Resume10:
    def __init__(self,x_per,x_yop):
        self.x_per=x_per
        self.x_yop=x_yop
    def disp1(self):
        print(self.x_per,self.x_yop)  
class Resume12(Resume10):
    def __init__(self,x_per,x_yop,xii_per,xii_yop):
        super().__init__(x_per,x_yop)
        self.xii_per=xii_per
        self.xii_yop=xii_yop
    def disp(self):
        super().disp1()
        print(self.xii_per,self.xii_yop)
        
class Resumeclg(Resume12):
    def __init__(self,x_per,x_yop,xii_per,xii_yop,deg_per,deg_yop):
        super().__init__(xii_per,xii_yop)
        super().__init__(x_per,x_yop)
        self.deg_per=deg_per
        self.deg_yop=deg_yop
    def disp2(self):
        super().disp1()
        super().disp()
        print(self.deg_per,self.deg_yop)

multiple inheritance : it is the phenomenon of deriving properties from multiple parent class to single child class

class p1:
    s.b
class p2:
    s.b
class c1(p1,p2): executes from right to left as per mro (method resolution order)
    s.b
    
class A:
    p=10
class B:
    y=99
    f=66
    p=99
class C(A,B):
    s=12


ob=C()
print(ob.p)


heirchieal inheritance
deriving properties from single parent class to multiple child class.
syntax:

class pc:
    s.b
class c1(pc):
    s.b
class c2(pc):
    s.b
class c3(pc):
    s.b

class A:
    m=19
class B(A):
    p=12
class C(A):
    q=32
ob1=C()  #q,m
ob2=B()  #p,m

hybrid inheritance:it is type of inheritance which can be done by combining more than 1 type of inheritance
it doesnt have a proper syntax.
example: combination of single level and multiple inheritance 
class addition:
    @staticmethod
    def add(a,b):
        return a+b
class substraction(Addition):
    @staticmethod
    def sub(a,b):
    return a-b
class Division:
    @staticmethod
    def div(a,b):
        return a/b
class Calci(substraction,Division):
    @staticmethod
    def mul(a,b):
        return a*b    



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

comprehension:
it is a phenomenon of creating a collection by reducing the instructions
it can be done on list,set,dict and tuple

list comprehension is phenomenon of creating a new list collection by reducing the instructions


syntax 1: 
var=[value for var in collection]


wap to store all the squares between the range 1-10

print([x**2 for x in range(1,11)])

wap to get following output:
[(2, 8), (4, 64), (6, 216)]
print([(i,i**3) for i in range(2,8,2)])

wap to extract all the integers from list
[1, 2, 3, 4]
print([x for x in eval(input("enter the list: "))  if type(x)==int])


wap to extract all the digits present in string collection and output in form of string 
print("".join([i for i in input("enter the string: ") if i.isdigit()]))


wap to count the number of upper case vowels characters present in string 
print(len([i for i in input("enter the string : ") if i in "AEIOU"]))


wap to sq the number if its even else cube of it
var=[tsb if cond else fsb for var in coll]

[1, 4, 27, 16, 125, 36, 343, 64, 729, 100]
print([i**2 if i%2==0 else i**3 for i in range(1,11)])

wap to get folowing output:
[('paarin', 6), ('trip', 4), ('pakka', 'akk')]
print([(i,len(i)) if len(i)%2==0 else (i,i[1:len(i)-1:])for i in input("enter the string: ").split()])


wap to get folowing output

[(1, 5), (1, 10), (1, 15), (2, 5), (2, 10), (2, 15), (3, 5), (3, 10), (3, 15)]

print([(i,j) for i in range(1,4) for j in range(5,16,5)])

set comprehension is phenomenon of creating a new set collection by reducing the instructions.

syntax:
var={value for var in collection}
var={tsb/value for var in coll if cond}
var={tsb if cond else fsb for var in coll}
var={(val1,val2) for var1 in coll for var2 in coll}


wap to store all the integers in rev present in list collection
print({int(str(i)[::-1]) for i in eval(input("enter a set: ")) if type(i)==int})

dictionary comprehension:
dictionary comprehension is phenomenon of creating a new dictionary collection by reducing the instructions.
syntax
var={k:v for var in coll}
var={k:v for var in coll if cond}
var={k:v if cond else v for var in coll}

wap to store word and its length as key value pairs present in a string
{'hello': 5, 'world': 5}
print({i:len(i) for i in input("enter: ").split()})

wap to store the number and its square as key value pairs if it is odd number, 
store its cube if it is a even number between the arnge 1-10
print({i:i**2 if i%2!=0 else i**3 for i in range(1,11)})

wap to store the character and its count keyvalue pair:
st=input("enter : ")
print({i:st.count(i) for i in st })


note:we can use comprehension on tuple but its called as generator comprehension which returns a generator
object when we print it meaning address so we need to typecast it to list,set,dict
print(list((i for i in range(1,11) if i%3!=0)))


file handling:
it is a place or medium where we store collection of data or store data.
inorder to open a file we use open() function

var=open("filename/loc.extension","mode")
mode: what type of operation we need to perform on the file

write mode(w) = it is mode which is to write the data  into the file, if the file is not existing , it creates a new file
if the file is existing it overrides the data

handling text file
write()- it is a fucntion which is used to write the data into the text file
syntax:
var.write("data")


writelines()- when multiple lines of data have to be written this function will be used 
syntax:
var.writelines(collection)
var.writelines(["hello i m cristiano ronaldo","i m the goat"])

example:
f=open("ronaldo.txt","w")
f.writelines(["quotes","your love makes me strong and ur hate make me strongest"])
f.close()

read mode:
it is a mode which is used to read the data , if the file doesnt exist it will give error .
methods on read

read()- it is a function which is used to read the complete data from the file
readline()- it is a function which is used to read single line . next time when we use readline it will read from where the cursor is present 
readlines()- it is a function which is used to return a list of all the lines present in text file separated by comma
we can use indexing on it .

example:
print(a.readlines()[1])

f=open("ronaldo.txt","r")
print(f.readlines()[0])
f.close()

handling csv files.

create a csv file which consists of name,age,gen,veg/non-veg,rst fetch name and age of all female who are veg/non veg
and single store it in new csv file

import csv
with open("ronaldo.csv","w+",newline="") as f:
    data=[["name","age","gender","veg-nonveg","rst"],
          ["ram",22,"m","non-veg","s"],
          ["sita",21,"f","veg","c"],
          ["geta",23,"f","non-veg","c"],
          ["radha",21,"f","veg","s"]]
    write=csv.writer(f)
    write.writerows(data)
    f.seek(0)
    read=csv.reader(f)
    for i in list(read)[1::]:
        data=[]
        if i[2]=="f" and i[3]=="veg" and i[4]=="s":
            with open("cr7.csv","w+",newline="") as t:
                data+=[i[0],i[1]]
                write=csv.writer(t)
                write.writerow(data)
                
convert text to csv 

import csv
with open("iplstat.txt","w+") as f:
    f.writelines(["team1 team2 venue won_by mom\n","rcb csk chep rcb shepard\n","mi csk wan mi sky\n","rcb srh rigen rcb vk"])
    f.seek(0)
    for i in f.readlines():
        o=i.split()
        print(o)
        with open("krishna.csv","a+",newline="") as t:
            write=csv.writer(t)
            write.writerow(o)
    with open("krishna.csv","r",newline="") as t:
        read=csv.reader(t)
        print(list(read))
        
            
    
parsing  techinique:
it is a phenomenon of providing security to the data by transfering from source to destination
it is of 2 types:

json parsing :

it is a type of parsing technique which is used to provide security to the data by converting it to
string format(json) which is called as serialisation.

dumps()- it is a function which is used to convert org data into string format
syntax:
import json
org_data=value
ser_data=json.dumps(org_data)

loads():
it is a function which is used to convert the string data (json) into org format.
syntax:
import json
ser_data=data
org_data=json.loads(ser_data)


example:

import json
a=[1,2,3]
b=json.dumps(a)
with open("data.txt","w") as x:
    x.write(b)
    x.seek(0)
    res=x.read()
    print(res,type(res))
    org_datajson.loads(res)
    print(org_data,type(org_data),"original data")



pickle parsing :
it is type of parsing technique which is used to provide security to the data by converting it to binary format

dumps():
it is function which is used to convert the original data into binary format .
syntax:
import pickle
org_data=[1,2,3] #value
s_data=pickle.dumps(org_data)

loads():
it is function which is used to convert the binary format into original data .

org_data=pickle.loads(s_data)


example:

import pickle
a=[1,2,3]
b=pickle.dumps(a)
with open('data2.txt','wb+') as f:
    x.write(b)
    x.seek(0)
    res=x.read()
    print(res)
    org_data=pickle.loads(res)
    print(org_data,"original data")

connection to sql /backend connectivity/db connection

it is a phenomenon of establishing to a db from python file
using sqlite3 module this can be achieved
connect()- function used to connect to db through py file
cursor()- func which gives authority to a variable to write queries
execute()-to execute
commit()- to save


import sqlite3
a=sqlite3.connect('ashrama.db')
b=a.cursor()
b.execute('create table Vgang (name,phno,addr,gen)')
b.execute('insert into Vgang values("vinayaka","988345671","hubli","m")')
a.commit()- to save
a.close()-to close

fetchone(): it is used to fetch a 1st matched record 

fetchall():it is used to fetch all the matched records present in the table

example:
import sqlite3
a=sqlite3.connect('ashrama.db')
b=a.cursor()
b.execute('select * from Vgang')

    
    
    
    
iteration : it is a process of traversing through the collection by fetching individual values
the function which is used to perform this is called iterator.

for loop is considered as a self iterator because it starts from the intial value,
traverses through the collection by fetching individual values and stops once it reaches end of collection.

iter():
it is a function which is used to point towards initial node address .
syntax:
iter_var=iter(collection)

next():
it is a function which is used to fetch the individual values by traversing through the collection.

note:
when it reaches the end of collection and if we use next() it throws stop iteration error.

node: it is a block of mem which consists of 3 parts .
prev node address, data, next node address 

example:
d=[1,2,3,4,5]
i=iter(d)
next(i) #1

exception handling:
exception:
it is an unauthorised event occured during execution of the program .
the exceptions needed to be handled to avoid the interruptions and continue the flow of execution of program.
exception handling is the phenomenon of making a program execute without any interuptions by handling the exceptions
in phython to handle the exception try and except block will be used .

in try block to program will return and except block solution for the error meassage will be written .
types of exception handling :
1.specific exception handling
2.generic exception handling
3.default exception handling

specific exception handling:
it is a type of exception handling which can be used when the name of exception is known .
syntax:
try:
    program
except ExceptionName:
    solution
    
try:
    program
except ExceptionName:
    solution
except ExceptionName2:
    solution

note: in a single try block multiple except block can be used .


def divide():
    try:
        a=int(input("enter: "))
        b=int(input("enter: "))
        print(a/b)
        print(d)
    except ZeroDivisionError:
        print("zero division handling")
    except NameError:
        print("same variable is present")
divide()
print("welcome patrick")
divide()
print("revise all the topics")
divide()

generic exception handling:
it is a type of exception handling where in we handle all exceptions except keyboardInteruptError.
syntax:
try:
    program
except Exception:
    solution

default exception handling: it is a type of exception handling where in we handle all exceptions including KeyboardInterruptError

try:
    program
except:
    solution


try:
    for i in range(1,1001):
        print(i)
except:
    print('handledd')

custom exception
to throw an error message , raise keyword will be used .
raise ExceptionName ('message')
where exception should be a predefined error name .
message is optional

user defined exception :
in python to throw an error message based on the user requirement 
class cname(Exception):
    pass
raise cname('message')

examples:
class Good(Exception):
    pass
if batch=="SP-A1":
    raise Good('always best from bottom')
else:
    print('ohhh neevu')


assertion Error:
if it is required to throw an error message based on condition "assert" keyword can be used

syntax:
assert condition,"message"
s.b

ex:
a=input("enter:") 
assert a==a[::-1],"not a palindrome"
print("palindrome")   
    
    
    
    
    
note: else block can be written for try and except also be used
it will be executed when there is no error message in the program.
finally: this block will be executed by default with or without any exception 

Regular expression(regex)
when it is required to fetch the necessary data from a huge data then regular expression is used

writing patterns will fetch the required data, because of this it is also called as pattern matching.

[A-Z]- to match 1 UC character
[a-z]- to match 1 LC character
[0-9]- to match 1 digit -\d
[a-zA-Z0-9]-to match 1 alphanumeric character -\w
[A-Z]{m}-to match m number of UC characters
[A-Z]{m,n}-to match m to n number of UC characters

*   	0 or more
+   	1 or more
?	    0 or 1
\b -   set boundaries
\ - remove spcl behaviour of spcl class
{n} 	Exactly n
{n,}	n or more
{n,m}	Between n and m



example:
[6-9][0-9]{9}
[A-Z]{5}\d{4}[A-Z]
[1-5][A-Z]{2}\d{2}[A-Z]{2}\d{3}

\d{2}\:\d{2}\:\d{2} - to match time in hh:mm:ss format
[0-1][0-9]|[2][0-3]\:[0-5][0-9]\:[0-5][0-9] - to match time in 24 hr format
[0-2][0-9]|[3][0-1]?\:[0][1-9]|[1][0-2]\:[0-5][0-9] 


to get the required data re module have to be used.
import re
s="joel patrick call 9872533741 , and alternate number 9723518330"
phn=re.findall(r'\b[6-9][0-9]{9}\b',s)
print(phn)


'''
 


