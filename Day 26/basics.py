# List Comprehension
import random

names = ["Alex", "Beth", "Naveena", "Rahul", "Vikram"]
# For Filtering the names which are less than 4 character length

short_name = [ name for name in names if len(name) <=4]
print(short_name)

all_uppercase = [name.upper() for name in names if len(name) > 5]
print(all_uppercase)


# Squaring numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [item ** 2 for item in numbers]
print(squared_numbers)

# Converting to integer and filtering even numbers
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(item) for item in list_of_strings]
result = [x for x in numbers if x%2==0]
print(result)



# Read from two files and then output the common values
# with open("file1.txt") as file1:
#     file1_values = file1.readlines()
#     file1_values = [int(item.strip()) for item in file1_values]
#
# with open("file2.txt") as file2:
#     file2_values = file2.readlines()
#     file2_values = [int(item.strip()) for item in file2_values]
#
# result = [item for item in file1_values if item in file2_values]
#
# print(result)



# Dictionary Comprehension
# new_dict = {new_key:new_value for item in list if test}
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}

names = ["Alex", "Beth", "Naveena", "Rahul", "Vikram"]

student_score_dict = {name:random.randint(20, 100) for name in names}

passed_students = {name:score for (name, score) in student_score_dict.items() if score>60}

print(student_score_dict)
print(passed_students)
