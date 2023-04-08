Attribute VB_Name = "insertforumla"
Sub insertforumla()

For x = 257 To 1980
    If Rows(x).EntireRow.Hidden Then
    Else
    If Range("IG" & x) <> "" Then
    Range("IF" & x) = "=" & Range("BJ" & x).Value & "-'" & Range("IG" & x).Value
    Else
    End If
    End If
Next x

End Sub
