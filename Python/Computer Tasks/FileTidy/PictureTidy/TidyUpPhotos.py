import os
import os.path

path = "/Users/hunteradder626/Pictures"
fileNames = []
screenshots = []

def get_the_date(seperatedFileName):
    for date in screenshots:
        fileDate = seperatedFileName[1].split("-")
        print(fileDate)
        return fileDate
        
for i in os.listdir(path):
    # if i is os.path.isfile:
        fileNames.append(i)
        # print(fileNames)

for eachFile in fileNames: 
    seperatedFileName = eachFile.split() 
    # print(seperatedFileName[0])
    if seperatedFileName[0] == "Screenshot":
        screenshots.append(eachFile)
        get_the_date(seperatedFileName)
        fileDate = get_the_date(seperatedFileName)
        yearFolder = path + "/" + fileDate[0]
        monthDict = {1:'1. Jan', 2:'2. Feb', 3:'3. Mar', 4:'4. Apr', 5:'5. May', 6:'6. Jun', 
            7:'7. Jul', 8:'8. Aug', 9:'9. Sep', 10:'10. Oct', 11:'11. Nov', 12:'12. Dec'}
        month = monthDict[int(fileDate[1])]
        monthFolder = yearFolder + "/" + month
        dayFolder = monthFolder  + "/" + fileDate[2]
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
        source = path + "/" + eachFile
        destination = dayFolder + "/" + eachFile 
        os.rename(source, destination)
        print(f"File {eachFile} moved to {destination}")    


    
# print(screenshots)
        
        

