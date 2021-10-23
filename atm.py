card=input("enter the atm card")
if card=="credit" and card=="debite":
    print("insert the card")
    language=input("enter the language")
    if language=="hindi" and language=="english":
        print("translat your language")
        pincode=input("enter the pincode")
        if pincode=="2102003":
            print("insert your pincode")
            withrawal=input("enter the withrawal")
            if withrawal=="current" and withrawal=="saving":
                print("insert your withrawal")
                amount=input("enter your amount")
                if amount=="5000000":
                    print("amount is safishiant")
                else:
                    print("amount is not safishiant")   
            else:
                print("insert not your withrawal")         
        else:
            print("insert not your pincode")
    else:
        print("insert not your language")
else:
    print("insert not your card")

