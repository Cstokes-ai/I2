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

def file_search():
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


def main():
    ent = input(
        "This program scans the current directory for files and lists their names.\n"
        "It then searches for a file matching the pattern AXB.txt, where A and B are letters,\n"
        "and X is a single digit (0-9).\n\n"
        "If exactly one matching file is found, its contents are copied to FOUNDit.txt\n"
        "and displayed on the screen.\n\n"
        "Press ENTER to proceed."
    )

    if ent == "":
        print("You pressed ENTER")


    else:
        print("You did not press ENTER")


main()