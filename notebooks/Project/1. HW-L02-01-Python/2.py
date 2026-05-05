# Vowel counter
#task is:
# Write a program that receives a string from the user
# and counts the number of vowels (a, e, i, o, u),
# ignoring case sensitivity.


def count_vowels(text:str)->int:
    """ 
        The function count_vowels takes a text and counts the number of vowels 
    """

    VOWELS = ["a", "e", "i", "o", "u"]
    TEXT_LOWER = TEXT.lower() # all charechter to lower
    counter = 0 # counter vowels
    for i in TEXT_LOWER:
        if i in VOWELS:
            counter += 1
    print(f"*** Number of vowels is {counter} ***") 


while True:
    print("--------------RUN--------------")
    print("1. Run (Machine Learning): 1")
    print("1. Run (Your Text): 2")
    print("2. Exit (Enter number): 3")
    Status = int(input("Enter Your Status: "))
    if Status == 1:
        TEXT = "Machine Learning"
        count_vowels(TEXT)
    elif Status == 2:
        TEXT = input("Enter your Text: ")
        count_vowels(TEXT)
    else:
        print("-----------Thank you-----------")
        break