#Create a dictionary
# Task is:
# Write a program that takes a string as input,
# counts the frequency of each word in it,
# and stores the result in a dictionary.

TEXT = "Data science makes data useful"


TEXT_LOWER = TEXT.lower()
LIST_TEXT = TEXT_LOWER.split(" ")
LIST_TEST_UNIQUE = list(set(LIST_TEXT))
print(LIST_TEST_UNIQUE)




