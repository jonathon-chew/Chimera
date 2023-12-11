#Get all file types in a folder, make a new folder for every file type and 
move all the files into the correct folder
$fileTypes=get-childitem -File | % {$_.Extension.tolower()} | unique; 
$newFolders=$fileTypes.Trim("."," ") | mkdir $newFolders; 
foreach($fileType in $fileTypes){$folder=$fileType.trim("."," "); mv 
"*$fileType" "./$folder"}