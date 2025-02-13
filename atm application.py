accounts = {
    2401:[100,2423,"user1@gmail.com","user1"],
    2402:[200,2424,"user2@gmail.com","user2"],
    2403:[300,2425,"user3@gmail.com","user3"]

    }
print(accounts)
while True:
    print("choose your option")
    print("1.withdraw")
    print("2.Deposit")
    print("3.Pin Genration")
    print("4. Mini statment")
    print("5. Exit")
    x = int(input("Choose Your option: "))
    print("*******************")
    if x==1:
        print("**************")
        acc = int(input("Enter your account number:"))
        if acc not in accounts:
            print("Invalid Account Number")
        else:
            if accounts[acc][1] is None:
                print("Dear pin is not genrated")
            else:
                pin =int(input("Enter Your Pin: "))
                if accounts[acc][1]==pin:
                    amt = int(input("Enter Amount:"))
                    if accounts[acc][0] >= amt:
                        accounts[acc][0]= accounts[acc][0]-amt
                        print("*************************************")
                        print("Amount Withdraw Sucessfull!")
                        print("*************************************")
                    else:
                        print("*************************************")
                        print("Inssufcient Balance")
                        print("*************************************")
                else:
                    print("*************************************")
                    print("Invalid Pin!")
                    print("***********************")
    elif x==2:
        acc =int(input("Enter Your AccountNumber: "))
        if acc not in  accounts:
            print("Invalid Account Number")
        else:
            amt = int(input("Please Enter amount"))
            accounts[acc][0]+=amt
            print("*************************************")
            print("Deposit sucessfull!")
            print("*************************************")
        
    elif x ==3:
        acc = int(input("Enter Your Account Number:"))
        if acc not in accounts:
            print("Invalid Account Number:")
        else:
            pin = int(input("Enter New Pin"))
            accounts[acc][1] = pin
            print("*************************************")
            print("Pin Genrated Sucessfully !")
            print("*************************************")
    

    elif x== 4:
        acc = int(input("Enter Your Account Number"))
        if acc not in accounts:
            print("*************************************")
            print("Invalid Acount Number")
            print("*************************************")
        else:
            pin = int(input("Enter Your Pin:"))
            if accounts[acc][1] == pin:
                print("*************************************")
                print(f"Name:{accounts[acc][-1]}")
                print(f"Email:{accounts[acc][-2]}")
                print(f"Balance:{accounts[acc][0]}")
                print("*************************************")
            else:
                print("*************************************")
                print("Invalid Pin!")
                print("*************************************")
    else:
        print("*******************")
        print("Thank You")
        print("Visit again")
        break
    
        
