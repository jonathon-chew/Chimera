#!/bin/bash
date +"%d-%m-%y"
/Users/hunteradder626/Library/CloudStorage/OneDrive-Personal/Documents/Scripts/Python/Works/NASA_Photo_of_the_Day/NasaPhotoADay.py
# Old version with a less verbose output 
#brew upgrade && brew update && brew cleanup
echo "-------------" && brew update && echo "-------------" && echo "Update done" 
brew upgrade && echo "-------------" && echo "Upgrade done" && echo "-------------"
brew cleanup && echo "-------------" && echo "Clean Up Done" && echo "-------------"
