#Create a dictionary
# Task is:
# Write a program that takes a string as input,
# counts the frequency of each word in it,
# and stores the result in a dictionary.

def dictionary(TEXT:str)->dict:
    """ The dictionary function counts the number of words in a text """

    TEXT_LOWER = TEXT.lower()
    # replace "." to " "
    # replace "  "tow space to " " one space
    #strip first and end space
    TEXT_LOWER = TEXT_LOWER.replace(".", " ").replace("  ", " ").strip()
    LIST_TEXT = TEXT_LOWER.split(" ") # make one list from each word
    LIST_TEST_UNIQUE = list(set(LIST_TEXT)) # Unique word
    dictionary = {} # empty dic

    for word in LIST_TEST_UNIQUE:
        counter = 0
        for word_in_text in LIST_TEXT:
            if word == word_in_text:
                counter +=1
        dictionary[word] = counter

    print(dictionary)


TEXT = "Data science makes data useful"
# TEXT = "I am Mohsen Mohabbi. I have enrolled in the AI bootcamp. I want to complete this course successfully."
dictionary(TEXT)


