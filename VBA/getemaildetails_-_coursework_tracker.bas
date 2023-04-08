Attribute VB_Name = "getemaildetails"
Sub wholeprogramme()
    Dim Seconds1 As Single
    Dim Seconds2 As Single

    Seconds1 = Timer()
Call getDataFromOutlook
Call getthedate
Call sortthenameout
Call splitemail
Call getsheetstouse
'Call copytheOrigional
'Call CreateSheet
Call sheetstodelete
Call addahyperlink
'Call studentadding
Call autofit
    Seconds2 = Timer()
    MsgBox ("Time taken:" & vbNewLine & Seconds2 - Seconds1 & " seconds")
End Sub

Sub reset()
Range("A1", "BO3000").CLEAR
'Call deletesheets
End Sub

Sub autofit()
Range("A:P").EntireColumn.autofit
Range("C:C").EntireColumn.ColumnWidth = 28
End Sub

Sub getDataFromOutlook()

Dim OutlookApp As Outlook.Application
Dim OutlookNamespace As Namespace
Dim Folder As MAPIFolder
Dim OutlookMail As Variant
Dim objOwner As Outlook.Recipient
Dim i As Integer

Set OutlookApp = New Outlook.Application 'make a new instance of outlook
Set OutlookNamespace = OutlookApp.GetNamespace("MAPI") 'get the inbox
Set objOwner = OutlookNamespace.CreateRecipient("*") 'change the owner of the mailbox
objOwner.Resolve 'make sure it can be done

If objOwner.Resolved Then
    Set Folder = OutlookNamespace.GetSharedDefaultFolder(objOwner, olFolderInbox) 'get the inbox of the new user
End If

Dim objItem As Object
Dim iRows, iCols As Integer
iRows = 2
    
    For Each objItem In Folder.Items 'for every piece of mail in the shared forlder inbox
        If objItem.Class = olMail Then
        
            Dim objMail As Outlook.MailItem
            Set objMail = objItem

            Cells(iRows, 1) = objMail.SenderEmailAddress 'get who sent it and put into column a
            Cells(iRows, 2) = objMail.To 'get who it was sent to and put in column b
            Cells(iRows, 3) = objMail.Subject 'get the subject of the email and put in column c
            Cells(iRows, 4) = objMail.ReceivedTime 'get when we recieved it
            Cells(iRows, 5) = objMail.Body 'get the body of the emali
        End If
        iRows = iRows + 1 'go to next email message
    Next

Set Folder = Nothing 'reset foldedr
Set OutlookNamespace = Nothing 'reset which inbox
Set OutlookApp = Nothing 'reset making a new instance of outlook with this variable

Cells.Select
Range("A1").Activate
With Selection 'change the formating of the cells to wrapped
    .HorizontalAlignment = xlGeneral
    .VerticalAlignment = xlBottom
    .WrapText = True
    .Orientation = 0
    .AddIndent = False
    .IndentLevel = 0
    .ShrinkToFit = False
    .ReadingOrder = xlContext
    .MergeCells = False
End With
With Selection 'change the formating to unwrapped
    .HorizontalAlignment = xlGeneral
    .VerticalAlignment = xlBottom
    .WrapText = False
    .Orientation = 0
    .AddIndent = False
    .IndentLevel = 0
    .ShrinkToFit = False
    .ReadingOrder = xlContext
    .MergeCells = False
End With

Range("A1").Select

End Sub

Sub splitemail()

'split the email into sections to be able to grab the needed parts
Dim last_row As Integer
last_row = Application.WorksheetFunction.CountA(ActiveSheet.Range("C:C"))

'split labs off
For x = 2 To last_row
Range("E" & x).Select
    Selection.TextToColumns DataType:=xlFixedWidth, _
        FieldInfo:=Array(Array(0, 1), Array(4, 1)), TrailingMinusNumbers:=True
Next

'get rid of labs
Range("E:E").Delete

'seperate the course code
For x = 2 To last_row
Range("E" & x).Select
Selection.TextToColumns DataType:=xlFixedWidth, _
        FieldInfo:=Array(Array(0, 1), Array(4, 1)), TrailingMinusNumbers:=True
Next

'break off >
For x = 2 To last_row
Range("F" & x).Select
    Selection.TextToColumns DataType:=xlDelimited, _
        TextQualifier:=xlDoubleQuote, ConsecutiveDelimiter:=False, Tab:=False, _
        Semicolon:=False, Comma:=False, Space:=False, Other:=True, OtherChar _
        :=">", FieldInfo:=Array(Array(1, 1), Array(2, 1), Array(3, 1), Array(4, 1), Array(5, _
        1), Array(6, 1)), TrailingMinusNumbers:=True
Next

'delete everything but title of moduel done
Range("F:I").Delete

'clear blanks in G
Range("G:G").ClearContents

'break off website
For x = 2 To last_row
    If Range("F" & x) <> "" Then
    Range("F" & x).Select
        Selection.TextToColumns DataType:=xlDelimited, _
            TextQualifier:=xlDoubleQuote, ConsecutiveDelimiter:=False, Tab:=False, _
            Semicolon:=False, Comma:=False, Space:=False, Other:=True, OtherChar _
            :="<", FieldInfo:=Array(Array(1, 1), Array(2, 1), Array(3, 1), Array(4, 1), Array(5, _
            1), Array(6, 1)), TrailingMinusNumbers:=True
    End If
Next x

'delete blank rows
For x = 2 To last_row
    If Range("F" & x) = "" Then
        Range("F" & x).EntireRow.Delete
    End If
Next x

'select all
Cells.Select
Range("A1").Activate

'wrap all
With Selection
    .HorizontalAlignment = xlGeneral
    .VerticalAlignment = xlBottom
    .WrapText = True
    .Orientation = 0
    .AddIndent = False
    .IndentLevel = 0
    .ShrinkToFit = False
    .ReadingOrder = xlContext
    .MergeCells = False
End With

'wrap off
With Selection
    .HorizontalAlignment = xlGeneral
    .VerticalAlignment = xlBottom
    .WrapText = False
    .Orientation = 0
    .AddIndent = False
    .IndentLevel = 0
    .ShrinkToFit = False
    .ReadingOrder = xlContext
    .MergeCells = False
End With

'choose column E and change to a number format
Columns("E:E").Select
Selection.NumberFormat = "0"

'get rid of website
Range("E1").Select
Range("G:G").ClearContents

'trim extra spaces
For t = 1 To last_row
    Range("F" & t).Value = WorksheetFunction.Trim(Range("F" & t))
    Range("F" & t).Select
    If Range("F" & t) = "Report a Problem" Then
        Range("F" & t).EntireRow.Delete
    End If
Next t

End Sub

Sub sortthenameout()

'get the names
Range("C:C").Copy
Sheets.Add.Name = ("Names")
Sheets("Names").Select
Range("C:C").PasteSpecial

'get how many names
Dim last_row2 As Integer
last_row2 = Application.WorksheetFunction.CountA(ActiveSheet.Range("C:C"))

'split the names off by spaces
For x = 2 To last_row2 + 1
Range("C" & x).Select
    Selection.TextToColumns DataType:=xlDelimited, _
        TextQualifier:=xlDoubleQuote, ConsecutiveDelimiter:=True, Tab:=False, _
        Semicolon:=False, Comma:=False, Space:=True, Other:=False, OtherChar _
        :="<", FieldInfo:=Array(Array(1, 1), Array(2, 1), Array(3, 9), Array(4, 9), Array(5, _
        9), Array(6, 9), Array(7, 9), Array(8, 9), Array(9, 1), Array(10, 1), Array(11, 1), Array(12 _
        , 1), Array(13, 1), Array(14, 1), Array(15, 1)), TrailingMinusNumbers:=True
Next x

'get the new amount of names
Dim last_row As Integer
last_row = Application.WorksheetFunction.CountA(ActiveSheet.Range("C:C")) + 1

'copy surname
Range("D:D").Copy
Sheets("Data").Select
Range("B:B").PasteSpecial
Sheets("Names").Select

'copy forenames
Range("C:C").Copy
Sheets("Data").Select
Range("C:C").PasteSpecial

'delete the new sheet
Application.DisplayAlerts = False
Sheets("Names").Delete
Application.DisplayAlerts = True

'input headings on to sheet
Range("B1").Value = "Surname"
Range("C1").Value = "First Name"
Range("G1").Value = "Error Handling"
Range("H1").Value = "Does the sheet exist"

End Sub

Sub getthedate()

Range("D:D").Select
Selection.NumberFormat = "dd/mm/yyyy"

End Sub

Sub getsheetstouse()

'work out how many coursecodes there are
Dim coursecodecounter As Integer
coursecodecounter = WorksheetFunction.CountA(ActiveSheet.Range("E:E"))

'get every course code in column E
For x = 2 To coursecodecounter
    If Range("E" & x) = Range("P" & x) Then
        GoTo alreadydone
    ElseIf Range("E" & x) <> Range("P" & x) Then
        Range("P" & x) = Range("E" & x)
    End If
    
alreadydone:
Next x

'remove the duplicates of course codes in the list
Range("P1").Value = "Sheets to use"
ActiveSheet.Range("P:P").RemoveDuplicates Columns:=1, Header:=xlYes

End Sub

Sub CreateSheet()
    
    Dim Courseworktitle As String
    y = 1
    
    'get the number of sheets that need to be made
    Dim last_row2 As Integer
    last_row2 = Application.WorksheetFunction.CountA(ActiveSheet.Range("P:P"))
    
    'make the sheet and go back to the data tab
    For x = 2 To last_row2
    Sheets.Add.Name = Range("P" & x)
    Sheets("Data").Activate
    Next x
    
    Dim last_row As Integer
    last_row = WorksheetFunction.CountA(ActiveSheet.Range("F:F")) + 1
    
    Dim last_column As Integer
    y = 9
    For i = 2 To last_row
    Courseworktitle = Range("E" & i) 'get the coursework title
    Range("F" & i).Copy 'copy the name of the moduel
    Sheets(Courseworktitle).Select 'go to the new sheet
    last_column = WorksheetFunction.CountA(ActiveSheet.Range("1:1")) 'work out how many moduels are there already
        If last_column < 9 Then 'if this is the first time start on column I
            last_column = last_column + 9
            For y = 9 To last_column
                If Cells(1, y) = Courseworktitle Then 'look in column 1 9 across does this equal the name of the moduel copied
                    GoTo done 'if it's the same go to done outside the IF statements and the loop
                Else 'if not the same
                    last_column = last_column + 1 'add one +1 not tested
                    Cells(1, last_column).PasteSpecial 'paste
                    GoTo done 'leave the if statement and leave the loop
                End If
            Next y
        Else
            For y = 1 To last_column 'if last column is bigger than 9 and meaning not starting on 9
                If Cells(1, y) = Courseworktitle Then 'if the coursework name is the same
                    GoTo done 'leave the loop and if statement
                Else 'if not the same
                    last_column = last_column + 1 'go 1 column along
                    Cells(1, last_column).PasteSpecial 'paste this new value
                    GoTo done
                End If
        Next y
    End If

done:
Sheets("Data").Select

Next i

Range("F1").Select

End Sub
Sub deletesheets()
'Call sheetstodelete 'write all the sheets to delete on the document
Dim killme As String

Sheets("Data").Select 'select the right sheet with the list of sheets to delete on

sheetcount = Sheets.Count 'count the number of sheets in the document

For x = 2 To sheetcount
killme = Range("O" & x) 'set the sheet name to be deleted
Application.DisplayAlerts = False 'don't ask me if i'm sure to delete
Sheets(killme).Delete 'delete the sheet
Application.DisplayAlerts = True 'turn alerts back on
Sheets("Data").Activate 'go to the data tab
Next x

Range("O:O").CLEAR 'get rid of the list of sheets to delete

End Sub

Sub cycletabs()
maxSheets = Sheets.Count 'work out how many sheets to go through
For x = 1 To maxSheets
Sheets(x).Select 'go through the sheet by the number of the sheet starting with the first sheet
Application.Wait (Now + TimeValue("00:00:01"))
Next x
End Sub

Sub deleteduplicateassessments()
maxSheets = Sheets.Count - 1 'get the number of sheets minus the data tab
For x = 1 To maxSheets 'for 1 to the number of sheets minus the data tab
Sheets(x).Select 'select the sheet by number of sheet in the document
Range("1:1").Select 'select the row
Selection.EntireRow.RemoveDuplicates 'remove the duplicate moduels
Next x
End Sub

Sub studentadding()

Dim surname As String
Dim forename As String
Dim courseworkcode As String
Dim assessment As String
Dim assessmentdate As String
Dim sht As Worksheet
Dim last_row As Integer
Dim last_row2 As Integer

Set sht = Sheets("Data")
sht.Select

'if surname exists check forename
'if forename exists add moduel date
'if forename doesn't exist add student
'if surname doesn't exist add student
'if surname exists but forename doesn't add student

last_row = WorksheetFunction.CountA(ActiveSheet.Range("B:B"))

'number of sheets
Dim finalSheet
finalSheet = Sheets.Count

'cycle through entries
For n = 2 To last_row
    'cycle through sheet names
    For s = 2 To finalSheet
        Debug.Print (Left(Range("E" & n), 3))
        If Left(Range("E" & n), 3) = Left(Range("O" & s), 3) Then
            Range("H" & n) = "I exist" 'if exists
            Debug.Print ("Hi")
            GoTo break
        Else
            Range("H" & n) = "I don't exist" 'if doesn't exist
        End If
    Next s
break: 'stop looking if found
    
Next n

Dim coursecodenumber As String

'For c = 2 To last_row
'coursecodenumber = Range("E" & c)
'    If Range("H" & c) = "I exist" Then
'        Sheets(coursecodenumber).Select
'        Sheets("Data").Select
'    End If
'
'Next c

For x = 2 To last_row
    If Range("H" & x) = "I exist" Then
    
    sht.Select
    surname = Range("B" & x) 'set the surname
    forename = Range("C" & x) 'set the first name
    assessmentdate = Range("D" & x) 'set the date that they did the assessment
    courseworkcode = Left(Range("E" & x), 3) 'set the coursework code
    assessment = Range("F" & x) 'what was the moduel that you did
    Sheets(courseworkcode).Select 'select the new sheet that needs the data entering
    
    last_row2 = WorksheetFunction.CountA(ActiveSheet.Range("C:C")) '+ 10
    
            For y = 4 To last_row2
            'check that last row wil run properly
        '        If last_row2 < 10 Then
        '        last_row2 = WorksheetFunction.CountA(ActiveSheet.Range("C:C")) + 10
        '        End If
                'check surname
                If Cells(y, 3) = surname Then 'check surname
                    If Cells(y, 4) = forename Then 'check forename
                        'check for the assessment title
                        For i = 9 To 100
                            If Cells(3, i) = assessment Then 'if right assessment
                                'check if value already added
                                If Cells(y, i) = assessmentdate Then 'if already added
                                    GoTo assessmentdoesntexist
                                Else 'if not already added then add this to the database
                                    Cells(y, i) = assessmentdate
                                    GoTo entered
                                End If
                            End If
                        Next i
                    ElseIf Cells(y, 4) <> forename And y < last_row2 Then 'if the forename isn't the same
                        GoTo forenameNotRight
                    End If
                ElseIf Cells(y, 3) <> surname And y < last_row2 Then 'if the surname doesn't match
                    GoTo surnameNotRight
                ElseIf Cells(y, 3) <> surname And y = last_row2 Then 'add the student then add the date into the database
                    last_row2 = last_row2 + 1 'add a row to the bottom
                    Cells(last_row2, 3) = surname 'add the surname
                    Cells(last_row2, 4) = forename 'add the forename
                        For i = 9 To 100
                            If Cells(3, i) = assessment Then 'if right assessment
                                'check if value already added
                                If Cells(y, i) = assessmentdate Then 'if already added
                                    GoTo done
                                Else 'if not already added
                                    Cells(y + 1, i) = assessmentdate
                                    GoTo entered
                                End If
                            End If
                        Next i
                End If
forenameNotRight:
        '        Range("D" & y) = Range("D" & y)
surnameNotRight:
        '        Range("C" & y) = Range("C" & y)
        '        Application.Wait (Now + TimeValue("00:00:01"))
        Debug.Print (y & " " & last_row2)
            Next y
assessmentdoesntexist:
        '    If sht.Cells(x, 7).Value = "" Then
            sht.Cells(x, 7) = "I can't enter this, please check the assessment exists and manually enter if it does"
        'End If
done:
        If sht.Cells(x, 7).Value = "" Then
            sht.Cells(x, 7) = "This has already been entered" 'what to put in error handling if this already exists
        End If
entered:
        sht.Select
        If sht.Cells(x, 7).Value = "" Then
            sht.Cells(x, 7).Value = "Happy days I have been entered" 'what to put in the error handling if it works
        End If
    
    Else
GoTo notthiscourse
    End If
notthiscourse:
Next x

sht.Select 'go back to the sheet with the data to enter and see any data errors

For x = 2 To last_row
    If Range("H" & x) = "I don't exist" Then
        Range("G" & x) = "This entry isn't for this course" 'if it couldn't do it, put this specific error
    End If
Next x
End Sub
Sub removestudents()

Dim numberofsheets As Integer
numberofsheets = Sheets.Count - 1

For x = 1 To numberofsheets
Sheets(x).Select
Range("A4", "BO3000").CLEAR 'clear all the data in the sheets, leaving the sheets
Next x

Sheets("Data").Select

End Sub

Sub copytheOrigional()
Dim sheetname As String

Range("Q1").Value = "Old sheet names" 'put the heading on

'name the flie
Dim FileName As Variant
FileName = "*"

'open and enter the password
Workbooks.Open FileName, Password:="*"

'get all the sheet names in the old document and copy on to the new spreadsheet
For y = 1 To Sheets.Count
    sheetname = Sheets(y).Name
    Windows("*").Activate
    Range("Q" & y + 1).Value = sheetname
    Windows("*").Activate
Next y

sheetname = "" 'reset the name of the spreadhseet

For x = 2 To 27
Windows("*").Activate 'swich to the new sheet
sheetname = Range("Q" & x) 'get the old sheet name
Windows("*").Activate 'switch to the old sheet
Sheets(sheetname).Select 'go to the sheet name
Range("A1:BO3000").Copy 'copy everything in the tab
Windows("*").Activate 'go back to new sheet
Sheets.Add.Name = Range("Q" & x) 'make the new sheet
Sheets(sheetname).Select 'go to the new sheet
Range("A1:BO3000").PasteSpecial 'paste the old data on to the new sheet
Sheets("Data").Select 'go to the data tab
Next x

End Sub

Sub sheetstodelete()

Sheets("Data").Select
Range("O1").Value = "Sheets to delete"
Range("O2", "O100").ClearContents

For x = 1 To Sheets.Count - 2
Range("O" & x + 1) = Sheets(x).Name
Next x

Range("J:K").ClearContents
'
End Sub

Sub checkingsheetsexistance()
'number of entried
Dim finalNumber As Integer
finalNumber = 59

'number of sheets
Dim finalSheet
finalSheet = 21

'cycle through entries
For x = 2 To finalNumber
    'cycle through sheet names
    For y = 2 To finalSheet
        If Range("E" & x) = Range("O" & y) Then
            Range("H" & x) = "I exist" 'if exists
            GoTo break
        Else
            Range("H" & x) = "I don't exist" 'if doesn't exist
        End If
    Next y
break: 'stop looking if found
    
Next x
    
End Sub

Sub checkingsheetdoesntexist()

Dim coursecodenumber As String

For x = 2 To 59
coursecodenumber = Range("E" & x)
    If Range("H" & x) = "I exist" Then
        Sheets(coursecodenumber).Select
        Application.Wait (Now + TimeValue("00:00:01"))
        Sheets("Data").Select
    End If
    
Next x

End Sub

Sub addahyperlink()

Dim last_row As Integer
last_row = Application.WorksheetFunction.CountA(ActiveSheet.Range("C:C"))

'For x = 2 To last_row
'Range("E" & x).Select
'sheetname = Range("E" & x)
'    ActiveSheet.Hyperlinks.Add Anchor:=Selection, Address:="", SubAddress:= _
'        sheetname & "!A1"
'Next x

maxSheets = Sheets.Count - 1
For x = 1 To maxSheets
Sheets(x).Select
Range("A1").Select
ActiveSheet.Hyperlinks.Add Anchor:=Selection, Address:="", SubAddress:= _
        "'Data'!A1"
Next x

Sheets("Data").Select

End Sub
