# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math 


def user_info():
    grade_list = []
    # Get the inputs from the user
    n_student = 5
    for _ in range(0, n_student):
        grade_list.append(int(input('Enter a number: ')))
    return grade_list

    # Calculate the mean and standard deviation of the grades
def get_average(grade_list):
    sum = 0 # Do you think 'sum' is a good var name? Run pylint to figure out!
    for grade in grade_list:
        sum = sum + grade
    mean = sum / len(grade_list)
    return mean

def standDev(grade_list, mean):
    sd = 0 # standard deviation
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    sd = math.sqrt(sum_of_sqrs / len(grade_list))
    return sd

    # print out the mean and standard deviation in a nice format.

def calculate(grade_list):
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')

# print_stat()
grade_list = user_info()
mean = get_average(grade_list)
sd = standDev(grade_list, mean)
calculate(grade_list)