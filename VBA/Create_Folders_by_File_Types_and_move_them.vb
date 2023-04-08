Option Explicit


Sub Auto_Open()

MsgBox "Welcome to ANALYSIS TABS"

End Sub

Sub OrganiseFilesbyFileType()

'Create an instance of the FileSystemObject
Dim fso As Scripting.FileSystemObject
Set fso = New Scripting.FileSystemObject

'Declare a variable for the folder we will loop in
Dim FolderPath As String

'Declare a variable for the files we will loop through
Dim Fle As Scripting.File

'Prompt the user for the folder they want to organise
Dim FoldPathPrompt As FileDialog
Set FoldPathPrompt = Application.FileDialog(msoFileDialogFolderPicker)


With FoldPathPrompt
    .Title = "Select the folder you want to organise files in"
    'If OK is selected, assign the folder path to the FolderPath variable
    If .Show = -1 Then FolderPath = .SelectedItems(1)
End With

'If a folder path has been specified...
If FolderPath <> "" Then

'Declare a variable to store the folder's parent folder's path
    Dim ParentPath As String
    ParentPath = fso.GetParentFolderName(FolderPath)
    
'Declare a variable to store the folder
    Dim TheFolder As Scripting.Folder
    Set TheFolder = fso.GetFolder(FolderPath)
    
'Declare a variable to store the folder's name
    Dim FolderName As String
    FolderName = fso.GetFolder(FolderPath).Name
    
'Declare variable to store the new folder path
    Dim NewFoldPath As String
    NewFoldPath = ParentPath & "\" & FolderName & " - Organised" & "\"
    
'Create a new folder
    fso.CreateFolder NewFoldPath
    
'Loop through each file in the folder that the user has specified
    
    For Each Fle In TheFolder.Files
        'If the subfolder for the file type does not already exist...
        If Not fso.FolderExists(NewFoldPath & Fle.Type) Then
            '... create the subfolder for the file type
            fso.CreateFolder (NewFoldPath & Fle.Type)
        End If
        'Copy the file to the correct subfolder
        Fle.Copy NewFoldPath & Fle.Type & "\" & Fle.Name
    Next Fle
'Delete the original folder
    TheFolder.Delete

End If


End Sub
