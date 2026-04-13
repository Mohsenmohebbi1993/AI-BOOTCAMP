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
    TEXT_LOWER = TEXT.lower()
    counter = 0
    for i in TEXT_LOWER:
        if i in VOWELS:
            counter += 1
    print(f"Number of vowels is {counter}") 
