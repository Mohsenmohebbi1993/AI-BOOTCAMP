#Create a dictionary
# Task is:
# Write a program that takes a string as input,
# counts the frequency of each word in it,
# and stores the result in a dictionary.

def dictionary(TEXT):
    TEXT_LOWER = TEXT.lower()
    LIST_TEXT = TEXT_LOWER.split(" ")
    LIST_TEST_UNIQUE = list(set(LIST_TEXT))
    dictionary = {}

    for word in LIST_TEST_UNIQUE:
        counter = 0
        for word_in_text in LIST_TEXT:
            if word == word_in_text:
                counter +=1
        dictionary[word] = counter

    print(dictionary)


TEXT = "Data science makes data useful"
dictionary(TEXT)

