# Print the numbers
# Task is: 
# Write a program that receives a number greater than 3 from the user
# If the number is odd, it should print all odd numbers from 1 up to that number 
# If the number is even, it should print all even numbers from 2 up to that number
# If the user's input is invalid, an appropriate error message should be displayed


def PrintNumber():
    """ PrintNumber is a function that takes a number as input and performs the following:  
        1. Validates whether the input has the correct data type; if incorrect, it prompts the user to enter the number again.  
        2. If the number is less than 3, it requests the input again.  
        3. Based on the input, it prints the numbers as follows:  
        4. If the number is even, it prints all even numbers from 2 up to that number.  
        5. If the number is odd, it prints all odd numbers from 1 up to that number. """ 
    
    number = input("Enter One number: ") 
    while True:
        if number.isdigit(): # if input is not number
            number = int(number) # change type
            if number > 3: # chacke numbe is greet than 3
                if not number % 2: # in number is Even
                    print("Result is:")
                    for i in range(2, number + 1 ,2):
                        print(i, end=",")

                else: # number is Odd
                    print("Result is:")
                    for i in range(1, number + 1 ,2):
                        print(i, end=",")

                print("") # last print has end=","
                break

            else:
                print("The number must be greater than 3, for EX: 4, 5,...")
        number = input("Enter another Number: ") # number is not valid and input another number



while True:
    print("--------------RUN--------------")
    print("1. Run (Enter number): 1")
    print("2. Exit (Enter number): 2")
    Status = int(input("Enter Your Status: "))
    if Status == 1:
        PrintNumber()
    else:
        print("-----------Thank you-----------")
        break
    

