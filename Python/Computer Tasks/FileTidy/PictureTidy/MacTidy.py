import os
import os.path
import datetime

userChoice = input("Where is the folder with the pictures? eg. Users/User/Pictures: ")

path = str(userChoice)
fileNames = []
screenshots = []

def get_the_date(seperatedFileName):
    for date in screenshots:
        fileDate = seperatedFileName[1].split("-")
        print(fileDate)
        return fileDate
        
for i in os.listdir(path):
    fileNames.append(i)
    
for names in fileNames:
    if os.path.isfile(path + "/" + names):
        
            remakeFilePath = path + "/" + names
            fileCreation = os.stat(remakeFilePath)
            fileCreation = fileCreation.st_birthtime
            
            fileCreationDateAndTime = datetime.datetime.fromtimestamp(fileCreation)
            fileCreation = str(fileCreationDateAndTime).split(" ")
            
            fileCreation = fileCreation[0]
            fileCreation = fileCreation.split("-")
            print(fileCreation)
            yearDate = fileCreation[0]
            print(yearDate)
            monthDate = fileCreation[1]
            print(monthDate)
            dayDate = fileCreation[2]
            print(dayDate)
            
            monthDict = {1:'1. Jan', 2:'2. Feb', 3:'3. Mar', 4:'4. Apr', 5:'5. May', 6:'6. Jun', 
                7:'7. Jul', 8:'8. Aug', 9:'9. Sep', 10:'10. Oct', 11:'11. Nov', 12:'12. Dec'}
            monthDate = monthDict[int(monthDate)]
            
            yearFolder = path + "/" + yearDate
            monthFolder = yearFolder + "/" + monthDate
            dayFolder = monthFolder  + "/" + dayDate
            
            try:
                if not os.path.exists(yearFolder):
                    os.mkdir(yearFolder)
                if not os.path.exists(monthFolder):
                    os.mkdir(monthFolder)
                if not os.path.exists(dayFolder):
                    os.mkdir(dayFolder)
            except OSError:
                print ("Creation of the directory %s failed" % dayFolder)
            else:
                print ("Successfully created the directory %s " % dayFolder)
                print("Files ready to be moved")
            source = path + "/" + names
            destination = dayFolder + "/" + names 
            os.rename(source, destination)
        