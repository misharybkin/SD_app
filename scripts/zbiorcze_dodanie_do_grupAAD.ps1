#Importujemy moduł
Import-Module ActiveDirectory
Connect-AzureAD


#liczymy linijki ze skrzynkami
$lines = Get-Content -Path "C:\Users\30002084\Documents\imiona.txt" | Measure-Object -Line | Select-Object -ExpandProperty Lines

for ($i = 0; $i -ne $lines; $i++){
    $user = Get-Content -Path "C:\Users\30002084\Documents\imiona.txt" | Select-Object -Index $i
   
    $UserSamAccountName = $user
    
# Otrzymywanie usera
    $user_azure = Get-AzureADUser -Filter "startswith(UserPrincipalName, '$user')"

# Dodanie do grupy w AAD
    $groupName = "Check Report Cabin Crew TEST Users"
    $group = Get-AzureADGroup -Filter "DisplayName eq '$groupName'"
    Add-AzureADGroupMember -ObjectId $group.ObjectId -RefObjectId $user_azure.ObjectId
    Write-Host "Profil $UserSamAccountName dodany do grupy $groupName."


    
}