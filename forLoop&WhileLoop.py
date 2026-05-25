#Write a program to print all natural numbers from 1 to n. – using while loop
# n=1
# while n<=100:
#     print(n)              (while loop)
#     n+=1 
#-------------#
# for i in range (1,101):
#     print(i)              (for loop)

#------------------------------------------------------#
#Write a program to print all natural numbers in reverse (from n to 1). –
#using while loop
# n=int(input("enter number :"))
# while n>=1:
#     print(n)                  (while loop)
#     n-=1
#-------------#
# n=int(input("enter number :"))
# for i in range (n,0,-1):     (for loop)
#     print(i)
#------------------------------------------------------#
#Write a program to print all alphabets from a to z. – using while loop
# i = 97

# while i <= 122:      
#     print(chr(i))      (while loop)
#     i = i + 1   
#-------------#
# for ch in range (ord('a'),ord('z')+1):
#     print(chr(ch))            (for loop)
#------------------------------------------------------#
#Write a program to print all even numbers between 1 to 100. – using
# while loop
# i=1
# n=int(input("enter number :"))
# while i<=n:
#     if  i%2==0:        (while loop)
#         print(i)
        
#     i += 1
#-------------#
# for i in range (2,101,2):
#     print(i)          (for loop)
#------------------------------------------------------#
#Write a program to find the sum of all odd numbers between 1 to n.
# i=1
# n=int(input("enter number :"))
# while i<=n:
#     if i%2!=0:   (while loop)
#       print(i)
#     i+=1    
#-------------#
# for i in range (1,101,2):
#     print(i)
# n=int(input("enter number "))  
# while n>0:
#     print(n)
#     n-=41
# ----------------------------------------------------

# 1 se 10 tak even numbers print karo using while
n=10
i=1
while i<=10:
    if i %2==0:
        print(i)
    i=i+1

# User se number lo, uska factorial nikalna hai (while se)
n=int(input("enter"))
i=1
fact=1
while i<=n:
    fact=fact*i
    i+=1
print(fact)    
# Ek number diya hai:
# 👉 uske digits ka sum nikalna hai
# Example: 123 → 1+2+3 = 6
n=123
smi=0
sumi=0
while i <=n :
    smi=n%10
    sumi=sumi+smi
    n/10
    i+=1
print(sumi)    
# Ek number palindrome hai ya nahi (while use karke)
# Example: 121 → palindrome
n=121
palni=0
palin=0
while i <=n :
    palni=n%10
    palin=palni+palin
    n/10
    i+=1
print(palin)    
# Fibonacci series print karo (first n terms)
# Example: 0 1 1 2 3 5 ...
n=9
favb=0
while i<=n:
    favb=favb+i
    i+=1
print(favb)    
# 👉 Number ke digits reverse print karo
# Example: 123 → 321
n=123
rev=0
num=0
while n>0:
   num =n%10
   rev=rev*10+num
   n=n//10
print(rev)   