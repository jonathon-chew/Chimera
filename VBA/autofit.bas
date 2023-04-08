Sub breakupthenames()
Dim surname As String
Dim firstname As String
Dim completetioncode As String
Dim module As String

Sheets("Raw Data").Select
Range("C1").Select
For n = 1 To 3402
    Sheets("Raw Data").Select
    For x = 1 To 26
        If Range("H" & x) <> "" Then
            surname = Range("D" & n)

                If Range("H" & x) = "Completed" Then
                    Sheets("Master Document").Select
                    For y = 1 To 131
                    If Range("B" & y) = surname Then
                        Debug.Print (Range("B" & y))
                        Debug.Print (Range("A" & y))
                            If Range("A" & y) = Sheets("Raw Data").Range("C" & n) Then
                                For m = 1 To 23
                                    If Cells(1, m) = Sheets("Raw Data").Range("E" & x) Then
                                        Cells(y, m) = Sheets("Raw Data").Range("H" & x)
                                    End If
                                Next m
                            End If
                    End If
                    Next y
                ElseIf Range("H" & x) = "Failed" Then
                    Sheets("Master Document").Select
                    For y = 1 To 131
                    If Range("B" & y) = surname Then
                            If Range("A" & y) = Sheets("Raw Data").Range("C" & n) Then
                                For m = 1 To 23
                                    If Cells(1, m) = Sheets("Raw Data").Range("E" & x) Then
                                        Cells(y, m) = Sheets("Raw Data").Range("H" & x)
                                    End If
                                Next m
                            End If
                        End If
                    Next y
                ElseIf Range("H" & x) = "Partial Completion" Then
                Sheets("Master Document").Select
                    Sheets("Master Document").Select
                    For y = 1 To 131
                        If Range("B" & y) = surname Then
                            If Range("A" & y) = Sheets("Raw Data").Range("C" & n) Then
                                For m = 1 To 23
                                    If Cells(1, m) = Sheets("Raw Data").Range("E" & x) Then
                                        Cells(y, m) = Sheets("Raw Data").Range("H" & x)
                                    End If
                                Next m
                            End If
                        End If
                    Next y
        n = n + 25
        End If
    Next x
Next n

End Sub