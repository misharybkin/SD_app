Import-Module ExchangeOnlineManagement

#łączymy się z Exchange
Connect-ExchangeOnline -UserPrincipalName 30002084@lot.pl

$user = Get-Content -Path "C:\aplikacja_moja\SD_app\temporary\jeden_user_wiele_dg\users.txt"
#liczymy linijki ze skrzynkami
$lines = Get-Content -Path "C:\aplikacja_moja\SD_app\temporary\jeden_user_wiele_dg\dg.txt" | Measure-Object -Line | Select-Object -ExpandProperty Lines

for ($i = 0; $i -ne $lines; $i++){
    $dg = Get-Content -Path "C:\aplikacja_moja\SD_app\temporary\jeden_user_wiele_dg\dg.txt" | Select-Object -Index $i
    Add-DistributionGroupMember -Identity $dg -Member $user
    Write-Output "Użytkownik dodany do DG $dg"
    
}