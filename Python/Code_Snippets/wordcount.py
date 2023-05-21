#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3

file = input("Which file would you like to count the words in? ")

with open (file, 'r') as f:
	contents = f.read()

wordcount = contents.split(" ")

print(len(wordcount))
