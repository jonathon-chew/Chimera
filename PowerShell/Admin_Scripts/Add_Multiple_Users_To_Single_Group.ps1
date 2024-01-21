$users=import-csv ./Users_To_Single_Group.csv
$group=Read-host "What is the group? "; $creds=Get-Credential ; foreach ($user in $users) {Add-ADGroupMember -Identity $group -Members $user.User -Credential $creds}
$creds=""