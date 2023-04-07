import os
# for folderName, subfolders, filenames in os.walk('/Users/hunteradder626/Library/CloudStorage/OneDrive-Personal/'):
#     print('The current folder is ' + folderName)

#     for subfolder in subfolders:
#         print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

#     for filename in filenames:
#         print('FILE INSIDE ' + folderName + ': '+ filename)

#     print('')

for folderName, subfolders, filenames in os.walk('/Users/hunteradder626/Library/CloudStorage/OneDrive-Personal/'):
    with open("OneDriveContents.txt", 'a') as f:
        f.write('The current folder is ' + folderName)
        f.write('\n' )
        
        for subfolder in subfolders:
            f.write('SUBFOLDER OF ' + folderName + ': ' + subfolder)
            f.write('\n' )

        for filename in filenames:
            f.write('FILE INSIDE ' + folderName + ': '+ filename)
            f.write('\n' )

        f.write('\n'*2)

