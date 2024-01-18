#Importujemy moduł
Import-Module ActiveDirectory




#liczymy linijki ze skrzynkami
$lines = Get-Content -Path "C:\Users\30002084\Documents\imiona.txt" | Measure-Object -Line | Select-Object -ExpandProperty Lines

for ($i = 0; $i -ne $lines; $i++){
    $user = Get-Content -Path "C:\Users\30002084\Documents\imiona.txt" | Select-Object -Index $i
   # Приклад: Установка дати вигасання профілю на 31 грудня 2022 року
    $UserSamAccountName = $user
    
# Отримання об'єкта користувача
    $User = Get-ADUser -Identity $UserSamAccountName

# Установка дати вигасання профілю
    $groupName = "SEC_Office365_F3"
    Add-ADGroupMember -Identity $groupName -Members $user
    Write-Host "Profil $UserSamAccountName dodany do grupy $groupName."


    
}