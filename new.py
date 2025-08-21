# n=int(input("enter:")) #145
# sum=0
# for i in str(n): #"145"
#     fact=1
#     for j in range(1,int(i)+1):
#         fact*=int(j)
#     sum+=fact
# if n==sum:
#     print("strong num")
# else:
#     print("not")   
# wap to reverse a int
# n=int(input("enter:"))
# rev=0
# while n!=0: #123 12 1
#     ld=n%10 #3 2 1
#     rev=rev*10+ld #3 32 321
#     n=n//10 #12 1 0
# print(rev)

# n=int(input("enter"))
# for i in range(1,n+1)::
#     for j in range(1,n+1):
#         if i in range(3,n+1) and j in (1,5) or i==4 or i==2 and j in(2,4) or i==1 and j==3 :
#             print("*",end=" ")
           
#         else:
#             print(end="  ")
#     print()        
            


# n=int(input('enter:'))
# i=1
# while i<=10:
#     print(n,'*', i,'=', n*i)
#     i+=1

# n=eval(input('enter'))
# st=''
# for i in n:
#     if type(i)==int:
#         rev=0
#         j=i
#         while j!=0 :
#             ld=j%10 #143 
#             rev=rev*10+ld #30
#             j=j//10 #14
#         st+=str(rev)
# print(st)

# n=eval(input("enter:"))
# out={}
# for i in n:
#     fact=1
#     if type(i)==int:
#         for j in range(1,i+1):
#             fact*=j
#         out[i]=fact
# print(out)
# l=eval(input("enter:"))
# out={}
# for i in l:
#     if type(i)==str:
#         rev=i[::-1]
#         r=" ".join(list(rev))
#         out[i]=r
#         print(out)
#     elif type(i)==int:
#         arm=0
#         p=len(str(i))
#         for j in str(i):
#             arm+= int(j)**p
#         if i == arm:
#             print(f"{i} is a armstrong num")
#         else:
#             print(f"{i} is not arm")

# ch=input('enter:').split()
# out1={}
# out2=[]
# for i in ch:
#     if len(i)%2==1:
#         r=i[::-1].capitalize()
#         s=0
#         for j in r:
#             s+=ord(j)
#         out1[r]=s
#     else:
#         r=i[::-1]
#         u=""
#         for j in range(len(r)):
#             if j%2==0:
#                 u+=r[j].upper()
#             else:
#                 u+=str(ord(r[j]))
#         out2+=[u]
# print(out2,"even")
# print(out1,"odd")

# n=eval(input('enter:'))
# for i in n:
#     if type(i)==int and i%2==0:
#         p=0
#         for j in range(1,i//2+1):
#             if i%j==0:
#                 p+=j
#         s=0
#         for k in str(p):
#             f=1
#             for x in range(1,int(k)+1):
#                 f*=x
#             s+=f 
#         if s==p:
#             print('strong')
#         elcse:
#             print('not')         
# l=eval(input('enter:'))
# for i in list(set(l)):
#     if type(i)==tuple:
#         if type(i[0])==str:
#            if i[0]==i[0][::-1]:
#                print(i[0],'palindrome')
#         elif type(i[0])==int:
#             if str(i[0]) == str(i[0])[::-1] : 
#                 print(i[0],'palindrome')         
# print (list(set(l))) 




            
# n=int(input("enter:"))
# for i in range(2,n):
#     if n%i==0:
#         print('not prime')
#         break
# else:
#     print("prime num")
    
# def check_prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             print('not prime')
#             break
#     else:
#         print("prime num")
# def prime(x,y):
#     for i in range(x,y+1):
#         print(i,end=" ")
#         check_prime(i)
# prime(1,100)

# def check_strong(n):
#     sum=0
#     for i in str(n):#125
#         fact=1
#         for j in range(1,int(i)+1):
#             fact*=j
#         sum+=fact
#     if sum==n:
#         return "strong"
#     else:
#         return "not strong"
# def strong(x,y):
#         for i in range(x,y+1):
#             if check_strong(i)=="strong":
#                 print(i," ",check_strong(i))
# strong(1,300)

#print all num which are prime  prime ,arm,str

# def check_prime(n):
#     if n>1:
#         for i in range(2,n):
#             if n%i==0:
#                 print(n,"not prime")
#                 break
#         else:
#             return "prime"
    
# def check_arm(x):#156
#     sum=0
#     l=len(str(x))#3
#     for i in str(x):
#         sum+=int(i)**l
#     if sum==x:
#         return 'arm'
        
# def check_strong(z):
#     sum=0
#     for i in str(z):
#         fact=1
#         for j in range(1,int(i)):
#             fact*=j
#         sum+=fact
#         if sum==z:
#             return "strong"
# def num(x,y):
#     for i in range(x,y+1):
#         if check_arm(i)=='arm' and check_prime(i)=='prime':
#             print(i,"armstrong,prime")
#         elif check_arm(i)=='arm':
#             print(i,"armstrong")
#         elif check_prime(i)=='prime':
#             print(i,'prime')
#         elif check_strong(i)=='strong':
#             print(i,'strong')
#         # else:
#         #     print(i,'none of above')
# num(1,200)

# n=int(input("enter:"))
# def feb(n):
#     a,b=0,1
#     for i in range(5):
#         print(a,end=" ")
#         a,b=b,a+b
# feb(5)

# def feb(n,a=0,b=1):
#     if n==0:
#         return a    
#     print(a)
#     return feb(n-1,b,a+b)
# feb(5)
  
s="abcda"
for i in range(len(s)):
    if s[i] in s[i+1:]:
        x=s.replace(s[i],"")
print(x)
    

s=eval(input("enter: "))
for i in s:
    if type(i)==int:
        max2=i
        max1=max(i,max2)
    else:
        s.remove(i)       
s.remove(max1)
print(max(s))







    
        

    
        
        
    



            
            
                    
        

                                                     
                
                    
        
        
    