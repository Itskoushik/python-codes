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





'''

    
        