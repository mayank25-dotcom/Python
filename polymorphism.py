'''
poly = > many  , morphism => forms

'''



# # Parent class
# class Bank:
#     def __init__(self, amount):
#         self.amount = amount

#     def display(self):
#         print("Bank Amount:", self.amount)


# Child class
# class BobBank(Bank):
#     def __init__(self, amount):
#         # calling parent constructor
#         super().__init__(amount)

#     def display(self):
#         print("Bob Bank Amount:", self.amount)  cd m                                                                                                                                                   mm   


# # Objects
# b1 = Bank(5000)
# b2 = BobBank(10000)
          
# b1.display()
# b2.display()
# class rbi:
#     def interst (self):
#         print("rbi interset 6%")
# class hdfc(rbi):
#     def interst (self):
#         print("rbi interset 10%")        
# h1=hdfc()
# h1.interst()
# h2=rbi()
# h2.interst()
# claaa addtwo varibe num1,num2 crate and object 
# class addtwo:
#     num1=1
#     num2=2 
#     def __add__(self,oji):
#          print("heelo fuction of add")
#     def __sub__(self,oji):
#          print("heelo fuction of subrtct")     


# o1=addtwo()
# o2=addtwo()
# print(o1.num1+o1.num2)
# print(o1+o2)
# print(o1-o2)
# crate a class nams as BanAcounct have class variabe as bank_name also crate instance 
# varinnele name as accout number and blance  create a method name as display acount print 
# bank name account number balance   
# class BankAccount :
#     bank_name='bob'
#     def __init__(self,account_number,balance):
#         self.bank_name= self.bank_name
#         self.account_number=account_number
#         self.balance=balance
#     def  display_Account(self):
#         print(f"account number {self.account_number} and {self.balance} {self.bank_name}" ) 
# cos1=BankAccount(122222,9099)
# cos1.display_Account()
# ==============================================================================




#  method over loading and over ringing 
# cand be overload conturct in pyhton           
# ?reson why and why not
# wHAT IS PUBLIC AND PRIVAATE PROTECTED MODIFR
# class bankaccount:
#     bank_name='Hdfc Bank'
#     def __init__(self,accno,balance):
#         self.accno=accno
#         self.__balance=balance
#     def displayBalance(self):
#         return self.__balance
#     def add_balance(self,deposit_amount):
#         self.__balance +=deposit_amount
# class savingaccount(bankaccount):
#     def __init__(self,accno,balance):
#         super().__init__(accno,balance)
#     def add_balance(self, deposit_amount):
#         if (deposit_amount < 25000 and deposit_amount>0):
#              self._bankaccount__balance += deposit_amount
#         else :
#             print("can't deposit")         
#     def balanceinfo(self):
#         return self._bankaccount__balance            
# s1=savingaccount(77)
# print(s1.balanceinfo)
# -----------------------------------------------------------------
# ''Overloading → Same name, different parameters
# Overriding → Same name, child class me change'''

# '''Public → Variable/method that can be accessed from anywhere.

# Protected → Variable/method that should be used only inside class and its child class 
# (but can still be accessed outside) but not good prcatice.  using _varibalename (single underscore )

# Private → Variable/method that cannot be accessed directly outside the class (used for data hiding).
#  using __varibalename (double underscore )
#  private access ex = a1 = A()
#                     print(a1.A_price) 

# Encapsulation is  a feature of OOPs where we bined(combined) methods & variables are together 
# class is a bined variables & methods accessibility 

# In constructor self hoga toh voh local variable hoga 
# wihtout self is local variable
# in class variable is class variable
# --------------------------------------------
# class bankaccount:
#     bank_name='Hdfc Bank'
#     def __init__(self,accno,balance):
#         self.accno=accno
#         self.__balance=balance

#     def get_balance(self):
#         return self.__balance
    
#     def depoist(self,deposit_amount):
#         self.__balance +=deposit_amount

#     def withdraw(self,withdraw_amount):
#         if (withdraw_amount < 25000 and withdraw_amount>0):
#              self.__balance -= withdraw_amount
#         else :
#             print("insufficient balance")
#     def display(self):
#         print(f"account holder :,{self.accno}")    
#         print(f"balance  :,{ self.__balance}")           
# class savingaccount(bankaccount):
#     def __init__(self,accno,balance):
#         super().__init__(accno,balance)
#     def add_balance(self, deposit_amount):
#         if (deposit_amount < 25000 and deposit_amount>0):
#              super().deposit( deposit_amount)
#         else :
#             print("can't deposit")         
#     def balanceinfo(self):
#         print("Balance is:", self.get_balance()) 
# class FDaccount(bankaccount)  :
#     def __init__(self,accno,balance,tenure):
#         super().__init__(accno,balance)
#         self.tenure=tenure       

# s1=bankaccount(1212,25)
# print(s1.get_balance())
# s1.depoist(100)
# print(s1.get_balance())
# s1.withdraw(50)
# print(s1.get_balance())
# s1.display()
# s2=savingaccount(777777,252525)
# s2.add_balance(10000)
# print(s2.get_balance())
# -------------------------------------------------------
class BankAccount:
    bank_name = 'HDFC Bank'

    def __init__(self, accno, balance):
        self.accno = accno
        self.__balance = balance   # private variable

    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def display(self):
        print(f"Account No: {self.accno}")
        print(f"Balance: {self.__balance}")


class SavingAccount(BankAccount):
    def add_balance(self, amount):
        if amount > 0:
            super().deposit(amount)
        else:
            print("Invalid deposit")

    def balance_info(self):
        print("Balance is:", self.get_balance())   # correct way


class FDAccount(BankAccount):
    def __init__(self, accno, balance, tenure):
        super().__init__(accno, balance)
        self.tenure = tenure

    def show_fd(self):
        print(f"FD Tenure: {self.tenure} years")



# s1=savingaccount(7777,100)
# s1.depoist(100)
# s1.balanceinfo()
# s1.add_balance(100)
# s1.display()

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(f"Name : {self.name}")
#         print(f"age{self.age}")
# class Student(Person):
#         def __init__(self,name,age,marks):
#           super().__init__(name,age)
#           self.marks=marks
#         def show_marks(self):
#             print(f"marks:{self.marks}")
#             if self.marks >80:
#                 print("good performance")
# s1=Student('mayank',23,95)
# s1.display()    
# s1.show_marks()      


class Student :
    def __init__(self,name,grade,persentage,team):
        self.name=name
        self.grade=grade
        self.persentage=persentage
        self.team=team
    def student_detail(self):
        print(f"{self.name} is in {self.grade} with {self.persentage}% from team {self.team}")
team1='a'        
team2='b'
student1=Student('mayank',7,97,team1)  
student2=Student('somya',2,95,team2)
student1.student_detail()  
student2.student_detail()  
        
  