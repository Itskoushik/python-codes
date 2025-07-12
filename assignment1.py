#oops concepts in python

#object creation
''''class car:
    def __init__(self,engine,topspeed): #init is a constructor used to initiaze the class method
        self.engine=engine
        self.topspeed=topspeed


    car1=car(100,200)   
    print(car1.topspeed) '''

#encapsulation or securing the data by hiding or protecting the code and showing part of it
#to users by using methods like private or protected access modifiers.

#what are access modifiers : it controls the visibilty and accessibility of class members
'''
class onepiece:
    def __init__(self,balance): #private variable
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def getbal(self):
        return self.balance
    
one=onepiece(500)
one.deposit(1000)
print(one.getbal())
    '''
#inheritance : the process of inheriting the properties of parent by a child is called as inheritance

class onepiece:
    def hello(self,h):
        self.h=h
        
        


