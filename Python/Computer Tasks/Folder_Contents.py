import os

path = "/Users/hunteradder626/Documents/Evernote/Recipies"

os.chdir(path)

listofFiles = []
number = 1
for everyItem in os.listdir(path):
    if os.path.isfile(everyItem):
        if everyItem != ".DS_Store":
            if everyItem != "mystyle.css":
                if everyItem != "ContentsPage.html":
                    listofFiles.append(everyItem)

with open ("links.txt", "a") as f:
    for everyFile in listofFiles:
        f.write("<a href=\"")
        f.write(everyFile)
        f.write("\">"+ str(number) + " " + everyFile.replace(".html", "") + "</a>")
        f.write("<br><br>")
        f.write("\n")
        number = number + 1

print("Done")