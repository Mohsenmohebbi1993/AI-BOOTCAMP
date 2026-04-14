# Calculate the average
#task is:
#Write a program that calculates the user's GPA based on the list below.
# First, ask the user for the number of courses,
# then receive the grades for those courses,
# and finally calculate the average of these grades and convert it to a GPA according to the table below.

# A : 20 - 18
# B : 17.99 - 15
# C : 14.99 - 12
# F : 11.99 - 0

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
    

