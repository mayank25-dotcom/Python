# Write a Python program to nd the second largest element in a list without using built-in functions 
# m=[2,7,8,9,5,7]
# maxi1=m[0]
# maxi2=0
# for  i in m :
#     if i > maxi1:
#         maxi2=maxi1
#         maxi1=i
#     elif  maxi2<i and i != maxi1:
#         maxi2=i
# print(maxi2)  
#  Given a dictionary where keys are student names and values are their marks, write a program to:
#  Find the student with the highest marks
#  Print their name and marks         
# m={'mayank':97, 'mmmm':78,'sssss':26,'jjjjj':65}
# top_student=''
# max_marks= -1
# for i in m :
#     if m[i] > max_marks:
#         max_marks=m[i]
#         top_student= i
# print("Topper:", top_student)
# print("Marks:", max_marks)     
# Write a function to check whether a given string of parentheses is valid.
# m=input("enter")
# if m == '()':
#     print("vaild")
# else:
#     print('non valid')    
# Write a Python program to print a hollow pyramid pattern for n = 5 .
# for row in range (1,6):
#     for colum in range (1,6):
#         if row <= colum:
#            print(" ",end="")
#     for x in range (1,row*2):
#         print("*",end=" ")
#     print()          
# Write a Python program using a lambda function to: 
# Find the square of each element in a list 
# Store the result in a new list
# m=[1,2,3,4,5,6,7]
# n=list(map(lambda x:x**2 ,m))
# print(n)
# data = [("Amit", 78), ("Riya", 92), ("John", 85)]
#  Sort the list based on marks using a lambda function.
# m=[("Amit", 78), ("Riya", 92), ("John", 85)]
# max1=m[0]
# for i in m :
#     if i > max1:

# Write a program using filter() 
# lambda to extract only even numbers from a list.
# m=[2,4,3,7,5,8]
# n=list(filter(lambda x : x%2==0,m))
# print(n)

class Student:
    def __init__(self,name):
        self.name=name
    def details(self):
        print(self.name)  
s1=Student("mayank")
s1.details()          

# class  Animal:
#     def sound(self):
#         print('sound')
# class Dog (Animal):
#     pass
# d1=Dog
# d1.sound()        

# class Person :
#     def intro(self):
#        print("mayank")
# class Student (Person):
#    pass
# s1=Student()
# s1.intro()
# class Animal:
#     def sound(self):
#         print('bhau')
# class dog (Animal) :
#     pass
# d1=dog()
# d1.sound()    
# class Account:
#     def __init__(self,balance):
#         self.__balance=balance
#     def get_balance(self):
#         print(self.__balance)  
#     def set_balance(self):
#         if self.__balance <= 0:
#             print("your balance is 0")
#         else:
#             print("good mantance balance ")    
m=[1,2,2,3,4,4,5]
n=[]
for i in m :
    if i not in n:
        n.append(i)
print(n)  

m=[10,15,20,25,30]
n=[x**2 for x in m if x%2==0    ]
print(n)

m=(1,2,3,4,5)
# print(m(-1,5))

m=(78,85,90,67,88)
# print(m.max())
# print(m.min)
marks=85
student={'name' :'mayank','marks':85}
if marks>= 80:
    student['grade']='A'
else :
  student['grade']='B'  
print(student)

data={'a':1,'b':2,'c':3}
# for i in data :
    # data[i]=data[value]

class car:
    def __init__(self,brand,speed):
        self.brand=brand 
        self.speed=speed
    def display(self):
        print(f"{self.brand} is your car brand and your speed {self.speed}") 
c1=car('marcadies' ,97)
c1.display()
class Bank :
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        if self.__balance < amount:
            print("error") 
        else:
           self.__balance-=amount
b1=Bank(700)
b1.deposit(700)                      
t=(10,20,30,40,50)
print(t[::2])