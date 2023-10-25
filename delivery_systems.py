print("="*20)

deleviry_boys =   [ "rakul","kajal","esha","navya","kavya" ] 
deleviry_boys_ids = ['0123', '2575', '7275', '2312', '5049']
deleviry_boys_salarys = [10000, 40000, 60000, 30000, 80000]
orders = 0
cash = 0
balance = 0
orderscancled_1 = 1
orderscancled_2 = 5
i = 0

# This statement below helps the program to run continuously.
while True:
    # os.system("cls")
    print("=====================================")
    print(" ----Welcome to Times deleviry----       ")
    print("*************************************")
    print("=<< 1. receiving orders           >>=")
    print("=<< 2. delevered orders           >>=")
    print("=<< 3. hand cash recived          >>=")
    print("=<< 4. online cash recived        >>=")
    print("=<< 5. Exit/Quit                  >>=")
    print("*************************************")
    # The below statement takes the choice number from the user.
    choiceNumber = input("Select your choice  number from the above menu : ")
    if choiceNumber == "1":
        print("Choice  number 1 is selected by the deleviry")
        # The line below will take the no:of delevirys from the user.
        NOC = eval(input("Number of delevirys : "))
 
        i = i + NOC
        # The if condition will restrict the number of new account to 5.
        if i > 5:
            print("\n")
            print("deleviry registration exceed reached or delevirys registration too low")
            i = i - NOC
        else:
            # The while loop will run according to the no:of delevirys.
            while orderscancled_1 <= i:
                # These few lines will take information from customer and then append them to the list.
                name = input("Input Fullname : ")
                deleviry_boys.append(name)
                pin = str(input("Please input a ids of your choice : "))
                deleviry_boys_ids.append(pin)
                balance = 0
                orders = eval(input("Please input a value to order to start an deleviry : "))
                balance = balance + orders
                deleviry_boys_salarys.append(balance)
                print("\nName=", end=" ")
                print(deleviry_boys[orderscancled_2])
                print("ids=", end=" ")
                print(deleviry_boys_ids[orderscancled_2])
                print("Balance=", end=" ")
                print(deleviry_boys_salarys[orderscancled_2], end=" ")
                print("-/Rs")
                orderscancled_1 = orderscancled_1 + 1
                orderscancled_2 = orderscancled_2 + 1
                print("\nYour name is added to delevirys system")
                print("Your ids is added to delevirys system")
                print("Your balance is added to delevirys system")
                print("----New account created successfully !----")
                print("\n")
                print("Your name is avalilable on the delevirys list now : ")
                print(deleviry_boys)
                print("\n")
                print("Note! Please remember the Name and ids")
                print("========================================")
                # This statement below helps the user to go back to the start of the program (main menu).
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif choiceNumber == "2":
        j = 0
        print("Choice number 2 is selected by the deleviry")
        # This while loop will prevent the user using the account if the username or ids is wrong.
        while j < 1:
            k = -1
            name = input("Please input name : ")
            pin = input("Please input ids : ")
            # This while loop will keep the function running when variable k is smaller than length of the
            # deleviry_boys list.
            while k < len(deleviry_boys) - 1:
                k = k + 1
                # These two if conditions find where both the name and pin matches.
                if name == deleviry_boys[k]:
                    if pin == deleviry_boys_ids[k]:
                        j = j + 1
                        # These few statement would show the balance taken from the list.
                        print("Your Current Balance:", end=" ")
                        print(deleviry_boys_salarys[k], end=" ")
                        print("-/Rs\n")
                        balance = (deleviry_boys_salarys[k])
                        # Statement below would take the amount to withdraw from user.
                        withdrawal = eval(input( " Input value to Withdraw : "))
                        # The if condition below would look whether the withdraw is greater than the balance.
                        if withdrawal > balance:
                            # This statement below would take a deposition from the deleviry.
                            deposition = eval(input(
                                "Please Deposit a higher Value because your Balance mentioned above is not enough : "))
                            # These few statements would update the value and show the balance to user.
                            balance = balance + deposition
                            print("Your Current Balance:", end=" ")
                            print(balance, end=" ")
                            print("-/Rs\n") # 1000-500=500
                            balance = balance - withdrawal
                            print("-\n")
                            print("----Withdraw Successfull!----")
                            deleviry_boys_salarys[k] = balance
                            print("Your New Balance: ", balance, end=" ")
                            print("-/Rs\n\n")
                        else:
                            # Else condition mentioned above is to do withdrawal if the balance is greater than the
                            # withdraw amount.
                            balance = balance - withdrawal
                            # These few statement would update the values in the list and show it to the deleviry.
                            print("\n")
                            print("----Withdraw Successfull!----")
                            deleviry_boys_salarys[k] = balance
                            print("Your New Balance: ", balance, end=" ")
                            print("-/Rs\n\n")
            if j < 1:
                # The if condition above would work when the pin or the name is wrong.
                print("Your name and pin does not match!\n")
                break
            # This statement below helps the user to go back to the start of the program (main menu).
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif choiceNumber == "3":
        print("Choice number 3 is selected by the deleviry")
        n = 0
        # The while loop below would work when the pin or the username is wrong.
        while n < 1:
            k = -1
            name = input("Please input name : ")
            pin = input("Please input pin : ")
            # The while loop below will keep the function running to find the correct user.
            while k < len(deleviry_boys) - 1:
                k = k + 1
                # The two if conditions below would find whether both the pin and the name is correct.
                if name == deleviry_boys[k]:
                    if pin == deleviry_boys_ids[k]:
                        n = n + 1
                        # These statements below would show the customer balance and update list values according to
                        # the deposition made.
                        print("Your Current Balance: ", end=" ")
                        print(deleviry_boys_salarys[k], end=" ")
                        print("-/Rs")
                        balance = (deleviry_boys_salarys[k])
                        # This statement below takes the depositionn from the customer.
                        deposition = eval ( input ( " Enter the value you want to deposit : "))
                        balance = balance + deposition # 1000+500=1500
                        deleviry_boys_salarys[k] = balance
                        print("\n")
                        print("----Deposition successful!----")
                        print("Your New Balance: ", balance, end=" ")
                        print("-/Rs\n\n")
            if n < 1:
                print("Your name and pin does not match!\n")
                break
            # This statement below helps the user to go back to the start of the program (main menu).
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif choiceNumber == "4":
        print("Choice number 4 is selected by the deleviry")
        k = 0
        print("deleviry name list and balances mentioned below : ")
        print("\n")
        # The while loop below will keeping running until all the delevirys and balances are shown.
        while k <= len(deleviry_boys) - 1:
            print("->.delevirys =", deleviry_boys[k])
            print("->.Balance =", deleviry_boys_salarys[k], end=" ")
            print("-/Rs")
            print("\n")
            k = k + 1
            # This statement below helps the user to go back to the start of the program (main menu).
        mainMenu = input("Please press enter key to go back to main menu to perform another fuction or exit ...")
    elif choiceNumber == "5":
        # These statements would be just showed to the deleviry.
        print("Choice number 5 is selected by the deleviry")
        print("Thank you for using our banking system!")
        print("\n")
        print("Come again")
        print("Bye bye")
        break
    else:
        # This else function above would work when a wrong function is chosen.
        print("Invalid option selected by the deleviry")
        print("Please Try again!")
        # This statement below helps the user to go back to the start of the program (main menu).
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
