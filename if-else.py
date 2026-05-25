#Q1 Write a program that takes an integer input from the user and checks whether the number is odd or
#even.
# m=int(input("enter number :"))
# if m%2==0:
#     print("even number")
# else:
#     print("odd number")    
#-------------------------------------------------------------------------------------#
#Write a program that takes three numbers as input and prints the largest of the three.
# a=int(input("enter 1st number:"))
# b=int(input("enter 2nd number:"))
# c=int(input("enter 3rd number:"))
# if a>b and a>c:
#        print(a)
# if b>c and b>a:
#         print(b)
# else:
#        print(c)       

#-------------------------------------------------------------------------------------#

#Write a program to check if a given year is a leap year. A leap year is divisible by 4 but not by 100
#unless it is also divisible by 400.

# m=int(input("enter year :"))
# if m%4==0 and  m%100!=0 or m%400==0:
#     print("this is leep year ")
# else:
#     print("non leep year")    

#-------------------------------------------------------------------------------------#
#Q4 Write a program that takes a percentage (integer) as input and prints the corresponding grade based
# on the following criteria:
# >= 90: Grade A    >= 70: Grade C  >= 80: Grade B
# >= 60: Grade D    < 60: Grade F

# m=int(input("enter intger persantage"))
# if m>=90:
#     print("a grade ")
# elif m<90 and m>=80:
#     print("b grade ") 
# elif m<80 and m>=70:
#     print("c grade ") 
# elif m<70 and m>=60:
#     print("d grade ")
# else:
#     print("f grade ")             

#-------------------------------------------------------------------------------------#

#Write a program that checks if a given letter is a vowel (a, e, i, o, u) or a consonant.

# char=(input("enter alhpabet :" ))
# if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
#     print("vowel")
# else:
#     print("consonant")

#-------------------------------------------------------------------------------------#
#Write a basic calculator program that takes two numbers and an operator (+, -, *, /) as input and
#performs the specified operation. Print the result based on the operation.

# m=int(input("enter number :"))
# n=int(input("enter number :"))
# y=input("what do")
# if y=='+':
#         print(m+n)
# elif y=='-':        
#    print(m-n)
# elif y=='*':     
#  print(m*n)
# elif y=='/': 
#  print(m/n)

#-------------------------------------------------------------------------------------#
#Write a program that takes a number as input and checks whether it is positive, negative, or zero.
# m=int(input("enter a number :"))
# if m<0:
#     print("nagitive number  ")
# elif m>0:
#     print("positive number") 
# else :
#     print("o")       
#-------------------------------------------------------------------------------------#

#Write a program that checks if a username and password entered by the user match the pre-set values
#username = "admin" and password = "1234". If both match, print "Login Successful", otherwise print
#"Login Failed".
# user = input("enter user name :")
# pasw = input("enter password :")
# if user=='admin' and pasw=='1234':
#     print("login")
# else:
#     print("wrong")    

#-------------------------------------------------------------------------------------#

#Write a program that takes three sides of a triangle as input and checks if those sides form a valid
#triangle. A triangle is valid if the sum of any two sides is greater than the third side.
#Check conditions like a + b > c, b + c > a, and a + c > b.
# m=int(input("enter 1 side :"))
# n=int(input("enter 2 side :"))
# y=int(input("enter 3 side :"))
# if m+n>y and n+y>m and y+m>n:
#     print('triangle')      
# else:
#     print("not vaild")    

#-------------------------------------------------------------------------------------#

#Write a program that calculates the Body Mass Index (BMI) based on user input for weight (in
#kilograms) and height (in meters). Then categorize the BMI into:
#Underweight (BMI < 18.5)
#Normal weight (18.5 <= BMI < 24.9)
#Overweight (25 <= BMI < 29.9)
#Obesity (BMI >= 30)
#Use the formula: BMI = weight / (height ** 2)
 
# w=float(input("enter your weight :"))
# h=float(input("enter your height :"))
# bmi = w / (h**2)
# if bmi < 18.5:
#     print("underweight")
# elif 18.5 <= bmi < 25:
#     print("Normal weight")       #samaj nhi aya
# elif 25 <= bmi < 30:
#     print("Overweight")
# elif bmi>=30:
#     print("obesity")
#-------------------------------------------------------------------------------------#
# #Q11 Write a program that calculates the discount for a product based on its price:
# If price is greater than 1000, discount is 10%
# If price is between 500 and 1000, discount is 5%
# Otherwise, no discount
# Print the final price after applying the discount.
 #--------#
# bill=int(input("enter Your bill :"))
# dicount=0
# if bill>=1000:
#      dicount=bill*10/100
#      print("you are aligable for 10% " ,bill-dicount)
# elif bill>=500:
#     dicount=bill*5/100
#     print("you are eligiable for 5%",bill*5/100) 
# else:
#      print("no dicount ")       
#-------------------------------------------------------------------------------------#
#Write a program that takes the name of a month as input and prints the number of days in that
# month. Consider leap years for February.
# month = input("Enter month name: ")
# year = int(input("Enter year: "))

# if month == "January":
#     print("31 days")

# elif month == "February":
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print("29 days (Leap Year)")
#     else:
#         print("28 days")

# elif month == "March":
#     print("31 days")

# elif month == "April":
#     print("30 days")

# elif month == "May":
#     print("31 days")

# elif month == "June":
#     print("30 days")

# elif month == "July":
#     print("31 days")

# elif month == "August":
#     print("31 days")

# elif month == "September":
#     print("30 days")

# elif month == "October":
#     print("31 days")

# elif month == "November":
#     print("30 days")

# elif month == "December":
#     print("31 days")

# else:
#     print("Invalid month")

#-------------------------------------------------------------------------------------#

#Write a program that simulates a simple ATM. The user should be able to:
#Check balance
#Deposit money
#Withdraw money (ensure the balance doesn't go negative) Use an if-else structure to handle the user's choices.
bal=25000
passw= int(input("enter 4 digit pin : "))
if passw==1234:
     print("1.check your balance ")
     print("2.CARDLESS Deposit  ")
     print("3.Withdraw  ") 
     selct=int(input("enter option  1,2,3 :"))
     if selct==1:
       print("your balance -->",bal)
     if selct==2:
       print("go branch")
     elif selct==3:
      print("collect your cash  -->",bal)
else:
    print("Worng pin")          

#-------------------------------------------------------------------------------------#
# #Write a program that categorizes a given age into different groups:
# Infant (0-1 year)
# Toddler (2-4 years)
# Child (5-12 years)
# Teenager (13-19 years)
# Adult (20-59 years)
# Senior (60 years and above)
# age=int(input("enter your age :"))
# if age <= 1:
#     print("Infant")  
# elif age >=1 and age<= 4:
#     print("Toddler")
# elif age >=4 and age<= 12:
#     print("child")
# elif age >=12 and age<= 19:
#     print("teenager")
# elif age >= 19 and age<=59:
#     print("Adult")    
# elif age >=60:
#     print("senior")
 #-------------------------------------------------------------------------------------#   
#Q15 Write a program that takes an integer (1-7) as input and prints the corresponding day of the week (1
#for Monday, 2 for Tuesday, etc.).
# num=int(input("enter number :"))
# if num==1:
#     print("monday")
# elif num==2:
#     print("tuesday")
# elif num==3:
#     print("Wednessday")
# elif num==4:
#     print("Thursday")
# elif num==5:
#     print("Friday")
# elif num==6:
#     print("Saturday")
# elif num==7:
#     print("sunday ")
# else  :
#     print("pleease vaild nnumber ")        









