atm=input("enter the card")
if atm ==("enter"):
    print("please choose banking for withdrowals")
    atm=input("banking")
    if atm ==("select the language"):
        print("english")
        atm=input("please enter your pin") 
        if atm ==("1213"):
            print("select transaction")
            atm=input("cash withdrawal")
            if atm ==("current saving"):
                print("yes")
                atm=input("unable to print recipt")
                if atm==("yes")or("no"):
                    print("yes")
                    atm=input("please enter the amount")
                    if atm==("yes")or("no"):
                        print("your transaction is being processed")
                        atm=input("your transaction successe")
                        if atm==("you can remove your card"):
                            print("yes")
                        else:
                            print("no")    
                    else:
                        print("not processed")    
                else:
                    print("no") 
            else:
                print("no") 
        else:
            print("no option") 
    else:
        print("no option") 
else:
    print("no available")            
        