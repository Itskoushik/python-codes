'''
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


'''