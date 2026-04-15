# Mini Recommendation System

#-----------------------
# package import:
import os

#-----------------------
print("----------------start Code----------------")

# Function:

def Checking_json_file(PATH:str):
    """ **Checking_json_file**   
    Chacke json file as `users.json`   
    In this directory, check whether the file `users.json` exists.    
    If it does not exist, create the JSON file using the code in `json_maker.py`.  
    """
    # PATH = r".\notebooks\Project\2. HW_L02_02_python\Mini Recommendation System"

    LIST_FILE = os.listdir(PATH) # list name of file in path

    if not "users.json" in LIST_FILE: # chacke file as `users.json`
        import json_maker # use my mudel, make `users.json` default
        json_maker.make_json_file(PATH) # I create this package
        print("Creat users.json file in this Directory")
    else:
        print("Find users.json in this Directory")

# my PATH
PATH = r".\notebooks\Project\2. HW_L02_02_python\Mini Recommendation System"
# PATH = "." # your PATH
Checking_json_file(PATH)

