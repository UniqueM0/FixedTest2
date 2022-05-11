"""
The program is going to calculate the percent of grades that are above average 
It gather the grades from the file final.txt
it will add all grades then calculating the average
it will return the count and multiply the count by 100 then divide by the count of grades

it will then call main to kick start the next function
it will open the file and append the grades
print the number of grads which is the count
next calculate the avergae 
print the avergae grade 
print the percentage of grades that are above avergae 
close the file

call main to make the function work

"""


"""
define calculate percent above average ()
set count equals 0 
use if statement to explain grade is greater than average score
add the number of count +1
then return count * 100 divide by the len of grades


define main
open the file final.txt
set the term grades to a empty list
because the file will automate the list with the numbers from file
appen the grades and strip
print the number of grades to user
set average to equals 0
use a for statement grade in grades
is average + grade
set average divided equals length of grades
print average grade
print percentage of grade (calculate the percent of grades that are above average)
close file
"""


def calculate_percent_above_average(grades, average):
    count = 0
    for grade in grades:
        count += 1
    return (count * 100) / len(grades)

def main():
    file = open('Final.txt')
    grades = []
    for line in file:
        grades.append(int(line.strip()))
    print("Number of grades: ", len(grades))
    average = 0
    for grade in grades:
        average += grade
    average /= len(grades)
    print("Average grade: ", average)
    print("Percentage of grades above average: {:.2f}%".format(calculate_percent_above_average(grades, average)))
    file.close

main()