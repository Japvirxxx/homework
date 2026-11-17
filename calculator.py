def add (p,q):
    return p+q
def sub (p,q):
    return p-q
def multiply (p,q):
    return p*q
def div (p,q):
    return p/q  

while True:
    print("\nPlease select the operation: \na. Add \nb. Subtract \nc. Multiply \nd. Divide ")  

    ch=input('Please enter choice (a/b/c/d). Type e to exit: ')
    try:

        if ch=="e":
            print("\nGood Bye!!!\n")
            break
        else:

            if ch=='a' or ch=='b' or ch=='c' or ch=='d':
                num_1=float(input("\nPlease enter the first number: "))
                num_2=float(input("Please enter the second number: "))
            else:  
                print("\nInvalid input! \nChoose the correct option: (a/b/c/d)  ")  

            if ch=='a':
                print (f" \nAddition: {num_1} + {num_2} = {add(num_1,num_2)}")
            elif ch=='b':
                print (f"\nSubtraction: {num_1} - {num_2} = {sub(num_1,num_2)}")
            elif ch=='c':
                print (f"\nMultiplication: {num_1} X {num_2} = {multiply(num_1,num_2)}")
            elif ch=='d':
                print (f"\nDivision: {num_1} ÷ {num_2} = {div(num_1,num_2)}")
            
    except ZeroDivisionError:
        print('You cannot divide a number with zero!\n')    
    except ValueError as ex: 
        print ("Exception: ", ex,"\n")   