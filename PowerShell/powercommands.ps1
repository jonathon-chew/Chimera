#Find all files with a name / file type

function find ($3) {Get-ChildItem -Include "*.$3*" -File -Recurse 
-ErrorAction SilentlyContinue}

#Open all files in folder

function OpenAll() {$1 = ls; for ($i=0; $i -lt $1.length;$i++){start 
$1[$i]}}

#Find file by name / part of name

function grep ($2) {Get-ChildItem -Filter "*$2*" -Recurse -ErrorAction 
SilentlyContinue}

#Replace all things with something else

#Get-ChildItem | Rename-Item -NewName { $_.name -replace " ","-" } 

#Navigate Home quickly

function home(){cd FILEPATH}

#Navigate to the shared drive quickly

function shared(){cd "FILE PATH"}

#Jump up x number of folders

function cdcd ($1) {for($i=0; $i -lt $1; $i++){ cd ..}}
 
#Create Archive Folders

function archive(){$1=Get-ChildItem -Directory; for($i=0;$i -lt $1.length; 
$i++){cd $1[$i]; mkdir Archive; cd ..}}

#Search for a Prince2 term

function prince2([string] $1){$2=$1.replace(" ", "+");start msedge.exe 
"https://www.google.com/search?q=$2+site%3Ahttps%3A%2F%2Fprince2.wiki"}

#Google Search

function google([string] $1){$2=$1.replace(" ", "+");start msedge.exe 
"https://www.google.com/search?q=$2"} 

#Make directory and change into it

function mkcd ($1){mkdir $1; cd $1}

#Open a file by number it appears in directory

#function open(){$1=ls;for($i=0; $i -lt $1.length;$i++){Write-Host $i 
$1[$i] $_.LastWriteTime}; [int] $2 = Read-Host "Which file? "; start 
$1[$2]}

function open(){$1=ls;for($i=0; $i -le $1.length - 1;$i++){Write-Host 
$i")" $1[$i] $1[$i].LastWriteTime}; [int] $2 = Read-Host "Which file? "; 
start $1[$2]}

#open and list directory

function cdls($1){cd $1; ls} 

#Save location to return

function save(){$global:goBack=pwd}

#Return to saved location

function rewind(){cd $global:goBack}
