Attribute VB_Name = "Module1"
Sub makedata()

'generate a random number
Dim randomNumber As Integer

For x = 1 To 300
cellNumber = Int(2 + rnd * (101 - 2 + 1))
columnNumber = Int(2 + rnd * (11 - 2 + 1))

'input the data

Cells(cellNumber, columnNumber).Value = "Done"

Next x

For y = 2 To 11
    For x = 2 To 101
        If Cells(x, y) = "" Then
            Cells(x, y) = "Not Done"
        End If
    Next x
Next y

End Sub
