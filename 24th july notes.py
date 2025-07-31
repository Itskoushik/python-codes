'''
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





'''

    
        