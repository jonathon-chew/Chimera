#! /Library/Frameworks/Python.framework/Versions/3.11/bin/python3

import json

#get all words
with open('words_dictionary.json', 'r') as f:
    content = f.read()

#convert string to json
words = json.loads(content)

#reverse the word
def emordnilap_Check(word):
    if word[::-1] in words:
        return True
    else:
        return False 

#Main script
while True:

    #Take User input
    wordToCheck = input('What word would you like to check? (Type "N" to cancel)\n')
    wordCheck = wordToCheck.lower()
    
    #Exit the script early if there is an issue
    if wordToCheck.upper() == "N": 
        break

    #Conditional statements and responses
    if wordToCheck == wordToCheck[::-1] and wordCheck in content:
        print("I'm a palindrome")
    elif wordCheck != wordCheck[::-1] and emordnilap_Check(wordCheck) == True:
        print("I'm a emornilap", wordToCheck, "<=>", wordToCheck[::-1])
    elif wordCheck in words:
        print("I'm neither a palindrome nor an emornilap")
    elif wordCheck not in words:
        print(f"I can't find {wordToCheck}, please check your spelling")
   
