Attribute VB_Name = "getDataFromOutlook"
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
