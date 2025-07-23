'''
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

 
'''
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
    