$groups=import-csv ./usergroups.csv
$member=Read-host "What is the username? "; $creds=Get-Credential ; foreach ($group in $groups) {
    Add-ADGroupMember -Identity $group.name -Members $member -Credential $creds
}
$creds=""
