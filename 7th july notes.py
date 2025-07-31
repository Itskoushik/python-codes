#wap to extract all the key value pairs from the dict only if the keys are strings with minimum 2 vowels init, the 
#values is prime number and sum of individual digits is a perfect number

#count vowels
# def count_vow(s,c=0):
#     for i in s:
#         if i in "aeiouAEIOU":
#             c+=1
#     return c
               
# #sum of digits 
# def su_digi(i,s=0):
#     for j in str(i):
#         s+=int(j)
#     return s

# #check if its prime number
# def is_prime(p):
#     for i in range(2,p):
#         if p%i==0:
#             return False
#     else:
#         return True   
# print(is_prime(int(input("enter the number: ")))    )    

# #perfect number
# def perfn(p,i=1,s=0):
#     while i<p:
#         if p%i==0:
#             s+=i
#         i+=1
#     if s==p:
#         return True
#     else:
#         return False


# def main(d,out={}):
#     for i in d:
#         if type(i)==str and count_vow(i)>2:
#             if type(d[i])==int and is_prime(d[i])==True:
#                 s=su_digi(d[i])
#                 if perfn(s)==True:
#                     out[i]=d[i]
#     print(out)

# main(eval(input("enter dict with values: "))) 
    
#input:143
#output:one four three

# def number(i,s=""):
#     d={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",0:"zero"}
#     for i in str(i):
#         s+=d[int(i)]+" "
#     print(s)
    
# number(int(input("enter the number :")))

# def words(s,i=""):
#     d={"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"zero":0}
#     for j in s.split():
#         i+=str(d[(j)])
#     print(int(i))
    
# words(input("enter the number in words :"))

#consider a str input ,if the len of str is odd check if the chars after middle char concatenated with chars before 
# middle char is palindrome or not without using slicing
# def pali(s,rev=""):
#     for i in s:
#         rev= i+rev
#     if s==rev:
#         return True
#     else:
#         return False
# def rev(s,rev=""):
#     for i in s:
#         rev= i+rev
#     return rev
    
# def main(s):
#     if len(s)%2==1:
#         mi=len(s)//2
#         s=s.split(s[mi])
#         st=rev(s[0])+s[1]
#         print(pali(st))
    
# main(input("enter the string: "))   
    

    