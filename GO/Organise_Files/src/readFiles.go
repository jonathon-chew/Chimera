package main

import (
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {

	//Ask the user what they what folder to clean
	var userQuestion string = "Which folder would you like to clean: "
	fmt.Println(userQuestion)

	//take in the user choice
	var userChoice string
	fmt.Scanln(&userChoice)

	//Assign the variable
	var folder string

	//state the place you want to make the new folders by file extention type
	if userChoice[len(userChoice)-1:] != "/" {
		folder = userChoice + "/"
	} else {
		folder = userChoice
	}

	//open the folder
	var f, err = os.Open(folder)

	//if there is an issue with finding the folder tell me
	if err != nil {
		fmt.Println(err)
		return
	}

	//get the files in a list from opening the folder
	files, err := f.Readdir(0)
	if err != nil {
		fmt.Println(err)
		return
	}

	//loop through all the files
	for _, v := range files {
		if !v.IsDir() {
			//create the required variables
			var fileExtention []string
			var fileName string = v.Name()

			//remove hidden Mac files
			var unwanted [2]string
			unwanted[0] = ".localized"
			unwanted[1] = ".DS_Store"

			//remove hidden Mac files from folder creation
			if fileName != unwanted[0] && fileName != unwanted[1] {
				fileExtention = strings.Split(v.Name(), ".")
				fmt.Println(folder+fileExtention[0]+"."+fileExtention[1], fileExtention[1])

				//check if the folder already exists - if it doesn't, make it
				if _, err := os.Stat(folder + fileExtention[1]); os.IsNotExist(err) {
					//make a new folder + make this with the entire folder path
					err := os.Mkdir(folder+fileExtention[len(fileExtention)-1], os.ModePerm)

					//if there is an issue keep going
					if err != nil {
						fmt.Println(err, folder+fileExtention[1])
						continue
					}
				}

				if err != nil {
					fmt.Println("Help!", err)
				}

				//move files to new folder
				err = os.Rename(folder+fileName, folder+fileExtention[len(fileExtention)-1]+"/"+fileName)

				if err != nil {
					log.Fatal(err)
				}
			}
		}
	}
}
