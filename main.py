# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




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