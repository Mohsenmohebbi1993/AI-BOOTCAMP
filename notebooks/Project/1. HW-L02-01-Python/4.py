# Calculate the average grade
#task is:
#Write a program that calculates avrage grade.
# First, ask the user for the number of courses,
# then receive the grades for those courses,
# and finally calculate the average of these grades and convert it to a GPA according to the table below.

# A : 20 - 18
# B : 17.99 - 15
# C : 14.99 - 12
# F : 11.99 - 0


def Calculate_the_average()->str:
    """ The function **Calculate_the_average**  
        1. first takes the number of courses,    
        2. then receives the grade for each course    
        3. If a grade is **NOT** between 0 and 20, it asks for the grade again"""
    
    print("First, enter the number of courses")
    NUMBER_OF_COURSES = int(input("Enter number of courses: "))
    grade_list = []

    for i in range(NUMBER_OF_COURSES):
        grade = float(input(f"Enter grade of {i+1} course: "))

        while True: # chacke 0 <= grade <= 20
            if 0 <= grade <= 20:
                grade_list.append(grade)
                break

            else: # if The grade is incorrect, give correct grade
                grade = float(input(f"The grade is incorrect, Enter grade of {i+1} course: "))
        
    avrage_grade = sum(grade_list) / len(grade_list)

    # chack avrage_grade
    if 18 <= avrage_grade <= 20:
        print(f"Your avrage garde is A and number of avrage garde {avrage_grade}")
    elif 15 <= avrage_grade < 18:
        print(f"Your avrage garde is B and number of avrage garde {avrage_grade}")
    elif 12 <= avrage_grade < 15:
        print(f"Your avrage garde is C and number of avrage garde {avrage_grade}")
    else:
        print(f"Your avrage garde is F and number of avrage garde {avrage_grade}")



Calculate_the_average()