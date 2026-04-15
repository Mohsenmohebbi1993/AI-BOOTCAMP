# Mini Recommendation System

#-----------------------
# package import:
import os
import json
import random
#-----------------------

# Function:
# 1. Json file chacker
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


# 2. # Read json file
def read_json_file(PATH:str):
    """ Function **read_json_file**   
        read json file  
        thas is old user"""
    
    JSON_FILE = "users.json"
    PATH_JSON_FILE = f"{PATH}\\{JSON_FILE}"
    with open(PATH_JSON_FILE, "r", encoding="utf-8") as f: user_data = json.load(f)
    return user_data


# 3. finde all available movies
def all_movies(user_data_from_json:dict):
    """ **all_movies**  
    return all movies availabel"""
    DICT_USER_DATA_VALUES = list(user_data_from_json.values())
    MOVIES = []
    for each_list in DICT_USER_DATA_VALUES:
        for movie in each_list:
            MOVIES.append(movie)
    return list(set(MOVIES))


# 4. Give name and chack is registered
def get_name():
    """ Function **get_username**   
        give:
        1. input first name
        2. input last name
        3. chack is user registered
        4. if is not registered give 3 favarit movies
    """

    # input name and remove space in first and end and capital form
    fist_name = input("Enter your first name: ").strip().capitalize()
    last_name = input("Enter your last name: ").strip().capitalize()
    full_name = f"{fist_name} {last_name}" # make full name
    print(f"Welcome `{full_name}` to Daneshkar") # say wellcome

    if not full_name in list(user_data.keys()): # in is not registered
        print(f"Dear `{full_name}`, you have not been registered before.")
        MOVIES = all_movies(user_data) # list all movies and print
        print("Please enter your 3 favorite movies")
        print("All available movies is: ")
        print(MOVIES)
        # give 3 favarit movies
        movie_1 = input("Please enter the 'First' movie: ").strip().capitalize()
        movie_2 = input("Please enter the 'Second' movie: ").strip().capitalize()
        movie_3 = input("Please enter the 'Third' movie: ").strip().capitalize()
        user_movies = [movie_1, movie_2, movie_3]
        return full_name, user_movies

    else: # if is registered
        print(f"Dear `{full_name}`, you have already been registered.")
        movie_1 = user_data[full_name][0]
        movie_2 = user_data[full_name][1]
        movie_3 = user_data[full_name][2]
        user_movies = [movie_1, movie_2, movie_3]
        return full_name, user_movies


# 5. rankig old user from movies new user
def ranking_old_user(user_data, user_movies):
    OLD_USERS = list(user_data.keys()) # list all old user
    ranking_old_user_dict = {}
    for each_old_user in OLD_USERS:
        grade_old_user = 0
        for each_old_user_movie in user_data[each_old_user]:
            for new_use_movie in user_movies:
                if each_old_user_movie == new_use_movie:
                    grade_old_user +=1
        ranking_old_user_dict[each_old_user] = grade_old_user
    return ranking_old_user_dict


# 6. movie similar and suggestion
def similar_and_suggestion_movie(user_data:dict, full_name:str, user_movies:list)->str:
    """ function **similar_and_suggestion_movie**    
        1. by fuction ranking_old_user give rank user
        2. List of movies similar to the user
        3. suggestion one movie from one suggestion list
        5. If the user is already registered, remove 5 movies
        6. If the user is NOT already registered, remove 3 movies
        7. print list moveis, that user see
        8. print one movie suggestion
    """
    # max similar user
    ranking_old_user_dict = ranking_old_user(user_data, user_movies)
    number_grade_old_user = max(ranking_old_user_dict.values())

    # List of movies similar to the user
    OLD_USERS = list(ranking_old_user_dict.keys())
    user_top_grade =[]
    for each_old_user in OLD_USERS:
        if ranking_old_user_dict[each_old_user] == number_grade_old_user:
            user_top_grade.append(user_data[each_old_user])

    # suggestion movie list (by Duplicate)
    suggestion_movie_list = []
    for i in range(len(user_top_grade)):
        for j in user_top_grade[i]:
            suggestion_movie_list.append(j)

    # suggestion movie list (by NOT Duplicate)
    suggestion_movie_list = list(set(suggestion_movie_list))

    OLD_USER_LIST = list(user_data.keys())
    if not full_name in OLD_USER_LIST: # If the user is already registered, they have watched 5 movies
        # remove movie, that user see
        duplicate_movie = 0 # counter similarr movie
        for i in user_movies: # 3 movies
            if i in suggestion_movie_list:
                suggestion_movie_list.remove(i)
                duplicate_movie += 1
        
        print(f"You have {duplicate_movie} movies in common with the users")

        if duplicate_movie != 0 :
            if len(suggestion_movie_list) != 0 : # if there is an unwatched shared movie
                print(f"you see {user_movies}")
                random_suggestion_movie = random.choices(suggestion_movie_list)
                print(f"Recommended movie for you {random_suggestion_movie}")
            else:
                print("Sorry cant find suggestion movie")
        else:
            print("Sorry cant find suggestion movie")   

    else:
        # remove movie, that user see
        user_movies = user_data[full_name] # 5 movies
        duplicate_movie = 0
        for i in user_movies:
            if i in suggestion_movie_list: # chack 5 movies
                suggestion_movie_list.remove(i)
                duplicate_movie += 1

        print(f"You have {duplicate_movie} movies in common with the users")

        if duplicate_movie != 0: # counter similarr movie
            if len(suggestion_movie_list) != 0 : # if there is an unwatched shared movie
                random_suggestion_movie = random.choices(suggestion_movie_list)
                print(f"you see {user_movies}")
                print(f"Recommended movie for you {random_suggestion_movie}")
            else:
                print("Sorry cant find suggestion movie")
        else:
            print("Sorry cant find suggestion movie")


#--------------------------- run code--------------------------
print("-----------------------start Code-----------------------")
# my PATH
PATH = r".\notebooks\Project\2. HW_L02_02_python\Mini Recommendation System"
# PATH = "." # your PATH

# chack json file (user.json)
Checking_json_file(PATH)

# read json file (user.json)
user_data = read_json_file(PATH)

# Give first and last name and 3 movies
full_name, user_movies = get_name()
print(f"{full_name} your 3 favorite movies are {user_movies[0]}, {user_movies[1]}, {user_movies[2]}")

# suggest one movie
similar_and_suggestion_movie(user_data, full_name, user_movies)
