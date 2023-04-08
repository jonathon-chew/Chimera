Attribute VB_Name = "Module3"
Option Explicit
Private Function GetHyperAddy(Cell As Range) As String
On Error Resume Next
GetHyperAddy = Cell.Hyperlinks.Item(1).Address
If Err.Number <> 0 Then GetHyperAddy = "None"
On Error GoTo 0
End Function
Sub DistillHyperlinks()

'select all the cells that you want to check in a document - not an entire worksheet

Dim HyperAddy As String, cl As Range, wsTarget As Worksheet, clSource As Range
Application.ScreenUpdating = False
Set clSource = Selection
On Error Resume Next
Set wsTarget = Sheets("Hyperlink List")
If Err.Number <> 0 Then
    Set wsTarget = Worksheets.Add
    With wsTarget
        .Name = "Hyperlink List"
        With .Range("A1")
            .Value = "Location"
            .ColumnWidth = 20
            .Font.Bold = True
        End With
        With .Range("B1")
            .Value = "Displayed Text"
            .ColumnWidth = 25
            .Font.Bold = True
        End With
        With .Range("C1")
            .Value = "Hyperlink Target"
            .ColumnWidth = 40
            .Font.Bold = True
        End With
    End With
    Set wsTarget = Sheets("Hyperlink List")
End If
On Error GoTo 0
For Each cl In clSource
    HyperAddy = GetHyperAddy(cl)
    If Not HyperAddy = "None" Then
        With wsTarget.Range("A65536").End(xlUp).Offset(1, 0)
            .Parent.Hyperlinks.Add Anchor:=.Offset(0, 0), _
            Address:="", SubAddress:=(cl.Parent.Name) & "!" & (cl.Address)
            .Offset(0, 1).Value = cl.Text
            .Hyperlinks.Add Anchor:=.Offset(0, 2), Address:=HyperAddy
        End With
    End If
Next cl
wsTarget.Select
End Sub

