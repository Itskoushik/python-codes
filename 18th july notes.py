'''
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

'''

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







