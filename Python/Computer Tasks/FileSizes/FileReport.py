import os

listOfBigFiles = []
sizeOfFiles = []
fileAddress = []

for root, dirs, everyFile in os.walk('/Users/hunteradder626/'):
    for eachFile in everyFile:
        try:
            file = os.path.join(root, eachFile)
            size = os.stat(file).st_size
            size  = size / 1024
            size = size / 1024
            if size > 100:
                size = round(size, 0)
                # print(eachFile, size)
                if ',' in eachFile:
                    eachFile = eachFile.replace(',', '')
                if ',' in file:
                    file = file.replace(',', '')
                listOfBigFiles.append(eachFile)
                sizeOfFiles.append(size)
                fileAddress.append(file)
        except:
            # print(f"Can't deal with {eachFile}")
            pass

# print(listOfBigFiles)
# print(sizeOfFiles)
# print(fileAddress)

os.chdir('/Users/hunteradder626/Desktop')

with open('Report.csv', 'w') as f:
    for x, y, z in zip(fileAddress, sizeOfFiles, listOfBigFiles):
        f.write(x + "," + str(y) + ',' + z)
        f.write('\n')

os.system('open report.csv')