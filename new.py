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

n=eval(input('enter'))
st=''
for i in n:
    if type(i)==int:
        rev=0
        j=i
        while j!=0 :
            ld=j%10 #143 
            rev=rev*10+ld #30
            j=j//10 #14
        st+=str(rev)
print(st)
        
            
    