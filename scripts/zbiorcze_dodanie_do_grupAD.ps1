#Importujemy moduł
Import-Module ActiveDirectory


#liczymy linijki ze skrzynkami
$lines = Get-Content -Path "C:\Users\30002084\Documents\imiona.txt" | Measure-Object -Line | Select-Object -ExpandProperty Lines

for ($i = 0; $i -ne $lines; $i++){
    $user = Get-Content -Path "C:\Users\30002084\Documents\imiona.txt" | Select-Object -Index $i
   # Приклад: Установка дати вигасання профілю на 31 грудня 2022 року
    $UserSamAccountName = $user
    
# Отримання об'єкта користувача
    $user_ad = Get-ADUser -Identity $user

# Установка дати вигасання профілю
    $groupNames = @("fw_opslight_prd_users", "opslite_prd_users_acl10")
    foreach($groupName in $groupNames){
        Add-ADGroupMember -Identity $groupName -Members $user_ad
        
        
}
    #$group = Get-AzureADGroup -Filter "DisplayName eq '$groupName'"
    #Add-AzureADGroupMember -ObjectId $group.ObjectId -RefObjectId $user_azure.ObjectId
    #Write-Host "Profil $UserSamAccountName dodany do grupy $groupName."


    
}