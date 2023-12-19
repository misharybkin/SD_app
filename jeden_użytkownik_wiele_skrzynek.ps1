#Importujemy moduł
Import-Module ExchangeOnlineManagement

#łączymy się z Exchange
Connect-ExchangeOnline -UserPrincipalName 30002084@lot.pl

$user = Get-Content -Path "C:\aplikacja_moja\1 zakładka\user.txt"
#liczymy linijki ze skrzynkami
$lines = Get-Content -Path "C:\aplikacja_moja\1 zakładka\pliczek.txt" | Measure-Object -Line | Select-Object -ExpandProperty Lines

for ($i = 0; $i -ne $lines; $i++){
    $skrzynka = Get-Content -Path "C:\aplikacja_moja\1 zakładka\pliczek.txt" | Select-Object -Index $i
    Add-MailboxPermission -Identity $skrzynka -User $user -AccessRights FullAccess
    Add-RecipientPermission -Identity $skrzynka -Trustee $user -AccessRights SendAs
    Write-Output "Użytkownik dodany do skrzynki $skrzynka"

    
}