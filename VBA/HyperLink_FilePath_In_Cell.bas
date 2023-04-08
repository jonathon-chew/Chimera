Attribute VB_Name = "Module1"
Sub make_hyperlinks()

lastrow = ActiveSheet.Cells(ActiveSheet.Rows.Count, "A").End(xlUp).Row

For x = 2 To lastrow
            commitmentstatement = Range("A" & x).Value
            Range("A" & x).Select
            ActiveSheet.Hyperlinks.Add Anchor:=Selection, Address:=commitmentstatement
Next x

End Sub
