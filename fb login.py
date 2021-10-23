# name=input("enter the name")
# if name=="anu":
#     print("correct name")
#     print("login process")
#     password=input("enter the password")
#     if password==("12345678"):
#         print("correct password")
#         print("login successfull") 
#     else:
#         print("wrong password") 
# else:
#     print("wrong name")                  

        


name=input("enter the name")
password=input("enter the password") 
if name=="anu" or password=="12345678":
    if name=="anu":   
        if password=="12345678":
            pass
        else:
            print("wrong password")    
    else:
         print("wrong name")          
else:
    print("wrong name and password")

