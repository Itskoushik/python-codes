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



'''




 


