#Importujemy moduł
Import-Module ExchangeOnlineManagement

#łączymy się z Exchange
Connect-ExchangeOnline -UserPrincipalName 30002084@lot.pl

$user = Get-Content -Path "C:\aplikacja_moja\SD_app\temporary\jeden_user_wiele_skrzynek\user.txt"
#liczymy linijki ze skrzynkami
$lines = Get-Content -Path "C:\aplikacja_moja\SD_app\temporary\jeden_user_wiele_skrzynek\skrzynki.txt" | Measure-Object -Line | Select-Object -ExpandProperty Lines

for ($i = 0; $i -ne $lines; $i++){
    $skrzynka = Get-Content -Path "C:\aplikacja_moja\SD_app\temporary\jeden_user_wiele_skrzynek\skrzynki.txt" | Select-Object -Index $i
    Add-MailboxPermission -Identity $skrzynka -User $user -AccessRights FullAccess -Confirm:$false
    Add-RecipientPermission -Identity $skrzynka -Trustee $user -AccessRights SendAs -Confirm:$false
    Write-Output "Użytkownik dodany do skrzynki $skrzynka"
}