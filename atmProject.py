import time

#Get input from user
print ("Please insert your CARD")

time.sleep(5)

#Declear password 
password = 4210

#Get input password from user
pin = int(input(" Enter your ATM pin : "))

#Declear balance
balance = 5000

#Condition for cheak password
if pin == password:

    while True:

        print(
            """
            1 == balance
            2 == withdraw balance
            3 == deposite balance
            4 == exit
            """
            )
    
    #Exception handinling
        try:
            option = int(input("Please enter your choice : "))
        except:
            print("Please enter a valid option : ")

    #Condition for cheak balance
        if option == 1:
            print(f'Your current balance is {balance}')
            print("----------------------------------------------------------------")

    #Condition for cheak withdraw Amount and display after withdraw amount
        if option == 2:
            withdrawAmount = int(input("plese enter your withdraw amount : "))
            print("---------------------------------------------------------------")

            balance = balance - withdrawAmount
            print("----------------------------------------------------------------")

            print(f'{withdrawAmount} rupees debited from your account')
            print(f'Your current balance is {balance}')
            print("----------------------------------------------------------------")

    #Condition for cheak deposite Amount and display after deposite amount
        if option == 3:

            depositeAmount = int(input("please enter your deposite amount : "))
            print("----------------------------------------------------------------")

            balance = balance + depositeAmount
            print("----------------------------------------------------------------")
            
            print(f'{depositeAmount} is credited to your account')
            print(f'Your current balance is {balance}')
            print("----------------------------------------------------------------")
    #Condition for end loop
        if option == 4:
            break

else:
    print("Wronge pin enter again !")