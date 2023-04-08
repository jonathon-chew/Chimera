#/usr/bin python3

# Make a md file with [] at the start of every line
import os

print("What's the file path? \n")
fileLocation = input()

os.chdir(fileLocation)

print("Is this a ReadMe file? Y/N? ")
readmeCheck = input()    

if readmeCheck == "y" or readmeCheck == "Y":
    fileName = "ReadMe.md"
elif readmeCheck == "n" or readmeCheck == "N":
    print("What's the name of the project? \n")
    fileName = input()
    fileName = fileName + ".md"

with open (fileName, "w") as f:
    f.write

def addLine():
    print("What are the steps? \n")
    steps = input()
    if steps != "":
        steps = "\n[] " + steps
        with open (fileName, "a") as f:
            f.write(steps)
    elif steps == "":
        newLineQuestion = input("Would you like to enter a new line? ")
        if newLineQuestion == "y":
            with open (fileName, "a") as f:
                steps = "\n"
                f.write(steps)

def firstLine():
    print("What is the first step? \n")
    steps = input()
    steps = "[] " + steps
    with open (fileName, "a") as f:
        f.write(steps)

firstLine()

while True:
    print("Would you like to add another line? Y/N")
    choice = str(input())
    if choice == "Y" or choice == "y":
        addLine()
    elif choice == "N" or choice == "n":
        print("Goodbye")
        break    

