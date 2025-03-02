#This project is done in Python in Jetbrains IDE editor.
#) https://docs.python.org/3/library/functions.html#max
#https://www.w3schools.com/python/python_lists_comprehension.asp
#https://www.geeksforgeeks.org/python-list-comprehension/
#https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists/
#https://stackoverflow.com/questions/1904394/read-only-the-first-line-of-a-file
import os
import re

def validity(line):
    parts = line.strip().split(",")#this is to check if the file has proper syntax structure for the reading
    if len(parts) < 2 or len(parts) >= 100:
        print("The file does not have the correct syntax structure.")
        return False
    if not all (part.isdigit() for part in parts):
        print("The file does not have the correct syntax structure.")
        return False
    return True

def file_search(): #First we have to check if the file exists
    #Once it opens, determine its validity. If it is valid, return the file name and the list of numbers

    path = os.getcwd()
    while True:
        file_name = input("Enter the name of the file you are looking for: ")
        if os.path.isfile(path):
            with open(file_name, "r") as file:
                for line in file:
                    if validity(line):
                        return file_name,list(map(int, line.split(",")))
        else:
            print("The file does not exist. Please try again.")
            continue

def average(numbers, file_name): #This function is meant to handle the average, low, average, and other number processing
    hi = max(numbers)
    lo = min(numbers)
    #With the high and low numbers, we can now calculate the average
    med = (hi + lo) / 2
    print(f"Hi is{hi}\n Lo is {lo}\n and Med is {med}")
    numbers_class = []
    for num in numbers_class:
        if num == med:
            numbers_class.append("Med")
        elif num > hi:
            numbers_class.append("Hi")
        else:
            numbers_class.append("Lo")

    #Create a new file called Mymatrix.txt
    new_file = f"HiMedLo{file_name}"
    with open(new_file, "w") as file:
        file.write(",".join(numbers_class))

def matrix():
    file_matrix = "Mymatrix.txt"
    if not os.path.isfile(file_matrix):
        print("The file MyMatrix.txt does not exist.")
        input("Press ENTER to exit.")
        return
    with open(file_matrix, "r") as file:
        lines = file.readlines()
        if len(lines) != 2:
            print("The file does not have exactly two lines.")
            input("Press ENTER to exit.")
            return

        matrix = [list(map(int, line.strip().split(","))) for line in lines]
        if len(matrix[0]) != len(matrix[1]):
            print("The lines do not have the same number of integers.")
            input("Press ENTER to exit.")
            return

    transposed = list(zip(*matrix))
    with open("Transposed.txt", "w") as file:
        for row in transposed:
            file.write(",".join(map(str, row)) + "\n")


def main():
    ent = input(
        "This program will process a file containing a list of non-negative integers, "
        "classify them based on their values, and then generate a new output file. Additionally, "
        "it will read a matrix from another file and create its transposed version."
        ""
    )

    if ent == "":
        print("You pressed ENTER")
        file_name, numbers = file_search()
        average(numbers, file_name)
        matrix()

    else:
        print("You did not press ENTER")


main()