# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <K.Pelayo>,<11/20/23>,<continuing>
# ------------------------------------------------------------------------------------------ #
import json
from json import JSONDecodeError
from typing import TextIO
# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
# FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = [student_first_name, student_first_name, course_name]  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
json_data: str = ''  # Holds combined string data in a json format.
file = None  # Holds a reference to an opened file.
menu_choice=input(MENU)  # Hold the choice made by the user.
# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
class FILEPROCESSOR:
class IO:
    def read_table_to_file(self):
    global file
    global students
    global student_first_name
    for students in student_data:
        print(f'Student'[student_first_name],[student_last_name],'Is enrolled in', [course_name])

def add_data_to_table():
    global student_first_name
    global student_last_name
    global course_name
    global student_data
    try:
        student_first_name = input("First name here.")
        if not student_first_name.isalpha():
            raise ValueError("the first name must be exclusively alphabets")
        student_last_name=input("Last name here.")
        if not student_last_name.isalpha():
            raise ValueError("the last name must be exclusively alphabets")
        course_name=input("Enter course here.")
        if not course_name.isalpha():
            raise ValueError("The course name must be exclusively alphabets.")
        student_data ={'first name': student_first_name,
                       'last name': student_last_name,
                       'course': course_name}
        students.append(student_data)
    except ValueError as e:
        print(e)
        print('-----techinical information----')
        print(e, e.__doc__, type(e), sep='\n')



def Save_data_to_file(students:[dict[str, str], file=FILE_NAME:
    file: TextIO=None
    try:
        file= open(file, 'w')
        json.dump(student_data,file)
        return True
    except TypeError as e:
        print('Json data was malformed')
        print('-----techinical information----')
        print(e, e.__doc__, type(e), sep='\n')
    except Exception as e:
        print('-----techinical information----')
        print(e, e.__doc__, type(e), sep='\n')
    finally:
        if not file.close:
            file.close()
        return False
IO.menu_choice(menu=MENU)
menu_choice=input(MENU)
def get_menu_input(MENU:str)->str:
    return input(menu_choice)
students = read_table_to_file(file=FILENAME)
while True:
    menu_choice=get_menu_input(menu=MENU)
    if menu_choice=='1':
        add_data_to_table(student_data=students)
    elif menu_choice=='2':
        read_table_to_file(file=FILENAME)
    elif menu_choice=='3':
        Save_data_to_file(student_data=students, FILENAME=file)
    elif menu_choice=='4':
        break
    else:
        print("Non command entered")