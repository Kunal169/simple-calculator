def calculator():
    print("\nWelcome to calculator developed by kunal")
    operations = input('''Please choose the operation you want to perform
    + for addition 
    - for substraction
    * for multiplication
    / for division 
    % for percent
    ** for power

    choose the operation :
    ''')
    num1 = int(input("Enter the number 1 :"))
    num2 = int(input("Enter the number 2 :"))

    if(operations == '+'):
        print(f"{num1} + {num2} is {num1+num2}")
       
    elif (operations == '-'):
        print(f"{num1} - {num2} = {num1-num2}")

    elif (operations == '*'):
        print(f"{num1} * {num2} = {num1 * num2}")

    elif (operations == '/'):
        print(f"{num1} / {num2} = {num1/num2}")

    elif(operations == '%'):
        print(f"{num1} % {num2} = {num1%num2}")

    elif(operations == '**'):
        print(f"{num1} ** {num2} = {num1**num2}")

    else:
        print(" You press Invalid key")
    again()

def again():
    again = input('''
    Do you want to use calculator again
    Please type Y for yes and N for no
    ''')
    a = again.capitalize()

    if(a == 'Y'):
        calculator()
    elif(a == 'N'):
        print("Thanks for using calculator and see you again")
    else:
        again()

calculator()


