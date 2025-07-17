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




'''
# class Student:
#     def __init__(self, name, marks):  # parameterized constructor
#         self.name = name
#         self.marks = marks 
#         print("adding new student in Database..")
#         print(self)
# ob=Student("ram",1)
# print(ob)

