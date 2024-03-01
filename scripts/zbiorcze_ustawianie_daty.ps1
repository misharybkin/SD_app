#Importujemy moduł
Import-Module ActiveDirectory


#liczymy linijki ze skrzynkami
$lines = Get-Content -Path "C:\Users\30002084\Documents\imiona.txt" | Measure-Object -Line | Select-Object -ExpandProperty Lines

for ($i = 0; $i -ne $lines; $i++){
    $user = Get-Content -Path "C:\Users\30002084\Documents\imiona.txt" | Select-Object -Index $i
   # Приклад: Установка дати вигасання профілю на 31 грудня 2022 року
    $UserSamAccountName = $user
    $ExpirationDate = Get-Date "2024-08-31"
    $ExpirationDateUTC = $ExpirationDate.ToUniversalTime()

# Отримання об'єкта користувача
    $User = Get-ADUser -Identity $UserSamAccountName

# Установка дати вигасання профілю
    #Set-ADUser -Identity $UserSamAccountName -AccountExpirationDate $ExpirationDateUTC

    Set-ADUser -Identity $UserSamAccountName -AccountExpirationDate $neverExpires #- без вигасання

    Write-Host "Дата вигасання профілю для користувача $UserSamAccountName була встановлена"


    
}