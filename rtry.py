a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a==b and b==c and c==a:
    print("all number are the equal")
elif a==b or b==c or c==a:
    print("any two number are equal")  
else:
    print("not equal")        