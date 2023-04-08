Attribute VB_Name = "Module1"
Sub passwordBreak()

attempt = 0

Dim i As Integer, j As Integer, k As Integer
Dim l As Integer, m As Integer, n As Integer
Dim i1 As Integer, i2 As Integer, i3 As Integer
Dim i4 As Integer, i5 As Integer, i6 As Integer

counter = 1

On Error Resume Next
For x = 1 To 1

On Error Resume Next
For i = 32 To 126: For j = 32 To 126: For k = 32 To 126: For l = 32 To 126: For m = 32 To 126:

If attempt < (95 ^ 5) Then
    attempt = attempt + 1
End If

If attempt > 7078 Then
passwordAttempt = Chr(i) & Chr(j) & Chr(k) & Chr(l) & Chr(m)
        
Call mainBreakProcess(passwordAttempt, attempt)

If Sheets.Count > 1 Then
    GoTo opened
End If

If counter = 10 Then
    Application.Wait (Now + TimeValue("00:00:01"))
    counter = 0
End If

counter = counter + 1

If attempt > (95 ^ 5) And attempt < (95 ^ 6) Then
For i1 = 32 To 126

passwordAttempt = Chr(i) & Chr(j) & Chr(k) & _
        Chr(l) & Chr(m) & Chr(i1)
        
Call mainBreakProcess(passwordAttempt, attempt)

If Sheets.Count > 1 Then
    GoTo opened
End If

If counter = 10 Then
    Application.Wait (Now + TimeValue("00:00:01"))
    counter = 0
End If

counter = counter + 1

Next

ElseIf attempt > (95 ^ 6) And attempt < (95 ^ 7) Then
For i2 = 32 To 126

passwordAttempt = Chr(i) & Chr(j) & Chr(k) & _
        Chr(l) & Chr(m) & Chr(i1) & Chr(i2)

Call mainBreakProcess(passwordAttempt, attempt)

If Sheets.Count > 1 Then
    GoTo opened
End If

If counter = 10 Then
    Application.Wait (Now + TimeValue("00:00:01"))
    counter = 0
End If

counter = counter + 1

Next

ElseIf attempt > (95 ^ 7) And attempt < (95 ^ 8) Then
For i3 = 32 To 126

passwordAttempt = Chr(i) & Chr(j) & Chr(k) & _
        Chr(l) & Chr(m) & Chr(i1) & Chr(i2) & Chr(i3)

Call mainBreakProcess(passwordAttempt, attempt)

If Sheets.Count > 1 Then
    GoTo opened
End If

If counter = 10 Then
    Application.Wait (Now + TimeValue("00:00:01"))
    counter = 0
End If

counter = counter + 1

Next

ElseIf attempt > (95 ^ 8) And attempt < (95 ^ 9) Then
For i4 = 32 To 126

passwordAttempt = Chr(i) & Chr(j) & Chr(k) & _
        Chr(l) & Chr(m) & Chr(i1) & Chr(i2) & Chr(i3) & _
        Chr(i4)
        
Call mainBreakProcess(passwordAttempt, attempt)

If Sheets.Count > 1 Then
    GoTo opened
End If

If counter = 10 Then
    Application.Wait (Now + TimeValue("00:00:01"))
    counter = 0
End If

counter = counter + 1

Next

ElseIf attempt > (95 ^ 9) And attempt < (95 ^ 10) Then
For i5 = 32 To 126

passwordAttempt = Chr(i) & Chr(j) & Chr(k) & _
        Chr(l) & Chr(m) & Chr(i1) & Chr(i2) & Chr(i3) & _
        Chr(i4) & Chr(i5)
        
Call mainBreakProcess(passwordAttempt, attempt)

If Sheets.Count > 1 Then
    GoTo opened
End If

If counter = 10 Then
    Application.Wait (Now + TimeValue("00:00:01"))
    counter = 0
End If

counter = counter + 1

Next

ElseIf attempt > (95 ^ 10) And attempt < (95 ^ 11) Then
For i6 = 32 To 126

passwordAttempt = Chr(i) & Chr(j) & Chr(k) & _
        Chr(l) & Chr(m) & Chr(i1) & Chr(i2) & Chr(i3) & _
        Chr(i4) & Chr(i5) & Chr(i6)
        
Call mainBreakProcess(passwordAttempt, attempt)

If Sheets.Count > 1 Then
    GoTo opened
End If

If counter = 10 Then
    Application.Wait (Now + TimeValue("00:00:01"))
    counter = 0
End If

counter = counter + 1

Next

ElseIf attempt > (95 ^ 11) And attempt < (95 ^ 12) Then
For n = 32 To 126

passwordAttempt = Chr(i) & Chr(j) & Chr(k) & _
        Chr(l) & Chr(m) & Chr(i1) & Chr(i2) & Chr(i3) & _
        Chr(i4) & Chr(i5) & Chr(i6) & Chr(n)

Call mainBreakProcess(passwordAttempt, attempt)

If Sheets.Count > 1 Then
    GoTo opened
End If

If counter = 10 Then
    Application.Wait (Now + TimeValue("00:00:01"))
    counter = 0
End If

counter = counter + 1
        
Next

End If

End If

Next: Next: Next: Next: Next

Next x

opened:

End Sub

Sub OpenWorkBookBroken(passwordAttempt)

w2 = Workbooks.Open("C:\Users\jc2207\Desktop\temp\2016-2017 Apprentice Database.xlsx", Password:=passwordAttempt)

End Sub


Sub mainBreakProcess(passwordAttempt, attempt)

Debug.Print ("I'm trying attempt: " & attempt & " password: |" & passwordAttempt & "| at " & Now)

Call OpenWorkBookBroken(passwordAttempt)

End Sub
