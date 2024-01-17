#Importujemy moduł
Import-Module ExchangeOnlineManagement

#łączymy się z Exchange
Connect-ExchangeOnline -UserPrincipalName 30002084@lot.pl

$skrzynka = Get-Content -Path "C:\aplikacja_moja\SD_app\temporary\jedna_skrzynka_wiele_userow\skrzynka.txt"
#liczymy linijki ze skrzynkami
$lines = Get-Content -Path "C:\aplikacja_moja\SD_app\temporary\jedna_skrzynka_wiele_userow\users.txt" | Measure-Object -Line | Select-Object -ExpandProperty Lines

for ($i = 0; $i -ne $lines; $i++){
    $user = Get-Content -Path "C:\aplikacja_moja\SD_app\temporary\jedna_skrzynka_wiele_userow\users.txt" | Select-Object -Index $i
    Add-MailboxPermission -Identity $skrzynka -User $user -AccessRights FullAccess -Confirm:$false
    Add-RecipientPermission -Identity $skrzynka -Trustee $user -AccessRights SendAs -Confirm:$false
    Write-Output "Użytkownik dodany do skrzynki $skrzynka"

    
}