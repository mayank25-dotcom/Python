# for row in range(1,5):
#     for colum in range (1,8):
#      if row-1 >=colum:
#         print("*",end="")
#     print()     
# # for row in range(1,5):
# #      for col in range(1,8):
# #         if col <= row-1:
# #             print(" ", end="")
# #         elif col <= row+3:
# #             print("*", end="")
# #         print()

# for row in range (1,7):
#     for  colum in range(1,8):
#         if colum==4 or row==4:
#             if row>=2 :
#                   print("*",end="")
#         else:
#             print(" ",end="") ṇ
#     print()           

         

# for i in range (1,6):
#     for j in range (1,6-i-1):
#          print(j,end="")
#     print()   
# for row in range (1,6):
#     for colum in range (65,71):
#         if row >=colum:
#             print(chr(colum),end="")
#         else :
#             print(" ",end="")
#     print()            
#
# ---------------------------------------------------------
#question 1 
# for row in range (1,5):
#     for colum in range (1,8):
#         if colum >= row and colum  <=row+3:
#          print("*",end="")  
#         else :
#            print(" ",end="") 
#     print()    
# ---------------------------------------------------------
#OUESTION 2 
# m=1
# n=5
# for row in range (1,6):
#     for colum in range (1,6):
#         if row==n or colum==n or row==m or colum==n or row==n or colum==m:
#             print ("*",end="")
#         else:
#             print(" ",end="")
#     print()            
# ---------------------------------------------------------
# #OUESTION 3
# for row in range (1,6):
#     for colum in range (1,row+1):
#           print(chr(64+colum),end="")
#     print()    
#          *

# for i in range(5):
#     # spaces print karne ke liye
#     for j in range(5 - i - 1):
#         print("- ", end=" ")

#     num = 1
#     for j in range(i + 1):
#         print(num, end="   ")
#         num = num * (i - j) // (j + 1)

#     print()    
# for i in range (1,5):
#       for colum in range (1,5):
#         if i <=colum :
#              print(" ",end=" ")
      
#       num = 1
#       for j in range(i + 1):
#         print(num, end="   ")
#         num = num * (i - j) // (j + 1)
#       print()  

# for row in range (1,5):
    



# for row in range (5):
#       for colum in range(1,5):
#          if  row <= colum  :
#             print(" ",end=" ")
  
#       num = 1
#       for j in range(row + 1):
#         print("*", end="   ")
#         num+=1
#       #   num = num * (row - j) // (j + 1)
#       print()    
# for m in range (1,5):
#       for n in range (1,5):
#         if m<=n :
#             print(" ",end=" ")
#       for k in range (1,m*2):
#         print("*",end=" ")
#       print(" ") 
# num=1    
# for row in range (1,5):
#       for colum in range (1,5):
#         if row <=colum :
#             print(" ",end=" ")
       
#       for i  in range (1,row+1):
#         print(num,end="    ")
#         num+=1
#       print()        

# print("------------------------------")
# n = 4
# num = 1

# for i in range(1, n + 1):
    
#     # spaces
#     for j in range(n - i):
#         print(" ", end="  ")
    
#     # numbers
#     for j in range(i):
#         print(num, end="     ")
#         num += 1
    
#     print()
# for row in range  (1,6):
#       for colum in range (1,6):
#          if row==colum:
#             print("*",end=" ")
#          else :
#             print(" ",end=" ") 
#       for i in range (1,10):
#          if row+colum%2==0:
#             print("*",end=" ")
#          else :
#             print(" ",end=" ")           
#       print()      
    
for row in range (1,5):
      for colum in range (1,row+1):
           if row>=colum:

            print("*",end="")
           else :
             print (" ",end="") 
      print()      


for row in range (1,5):
      for colum in range (1,5):
            if row <= colum:
               
               print("*",end="")
            else:
               print(" ",end="")   
      print()       

for i in range(5, 0, -1):
    # spaces
    for j in range(1, 6 - i):
        print(" ", end="")

    # stars
    for k in range(1, 2*i):
        print("*", end="")

    print()











