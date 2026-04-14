# Reverse the sentence
# task is:
# give one sentence and reverse


def reverse_the_sentence_1(SENTEMCE:str)-> str:
    """ **Reverse the sentence**  
        give one sentence and reverse
    """
    # clean SENTEMCE
    SENTEMCE = SENTEMCE.replace(".", " ").replace("  ", " ").strip()
    LIST_SENTEMCE = SENTEMCE.split()
    REVERSED_SENTEMCE = LIST_SENTEMCE[::-1]
    print(*REVERSED_SENTEMCE)


# or ---------------------
def reverse_the_sentence_2(SENTEMCE:str)-> str:
    """ **Reverse the sentence**  
        give one sentence and reverse
    """
    # clean SENTEMCE
    SENTEMCE = SENTEMCE.replace(".", " ").replace("  ", " ").strip()
    LIST_SENTEMCE = SENTEMCE.split()
    for i in range(len(LIST_SENTEMCE)-1, -1, -1): # range(10 , 0, -1) does not include 0
        print(LIST_SENTEMCE[i], end=" ")
    print() # last print has end=" ",don't want the next print to stick to it


# or 
def reverse_the_sentence_3(SENTEMCE:str)-> str:
    """ **Reverse the sentence**  
        give one sentence and reverse
    """
    # clean SENTEMCE
    SENTEMCE = SENTEMCE.replace(".", " ").replace("  ", " ").strip()
    LIST_SENTEMCE = SENTEMCE.split()
    for i in range(0, len(LIST_SENTEMCE)):
        # (len(LIST_SENTEMCE) - i - 1) index start 0 to len -1
        print(LIST_SENTEMCE[(len(LIST_SENTEMCE) - i - 1)], end=" ")
    print() # last print has end=" ",don't want the next print to stick to it





SENTEMCE = "Data science is fun"
reverse_the_sentence_1(SENTEMCE)
reverse_the_sentence_2(SENTEMCE)
reverse_the_sentence_3(SENTEMCE)
