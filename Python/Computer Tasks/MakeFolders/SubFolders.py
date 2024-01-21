import os

path = ("/Volumes/MEDWAY/Higher and Degree Apprenticeships/CHDA MAIN FOLDER/Sign-Up Documents/TEST/")

compaines = ["Test Company", "Test Company 2"]

students = ["James James:Michael Michael", "Don't Show:Please Don't show"] 
s = 0

for i in compaines:
    os.chdir(path)
    os.mkdir(i)
    os.chdir(path + "/" + i + "/")
    student = students[s].split(":")
    for e in student:
        os.mkdir(e)
    s = s + 1
