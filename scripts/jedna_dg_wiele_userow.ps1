Import-Module ExchangeOnlineManagement

#łączymy się z Exchange
Connect-ExchangeOnline -UserPrincipalName 30002084@lot.pl

$skrzynka = Get-Content -Path "C:\aplikacja_moja\SD_app\temporary\jedna_dg_wiele_userow\dg.txt"
#liczymy linijki ze skrzynkami
$lines = Get-Content -Path "C:\aplikacja_moja\SD_app\temporary\jedna_dg_wiele_userow\userzy.txt" | Measure-Object -Line | Select-Object -ExpandProperty Lines

for ($i = 0; $i -ne $lines; $i++){
    $user = Get-Content -Path "C:\aplikacja_moja\SD_app\temporary\jedna_dg_wiele_userow\userzy.txt" | Select-Object -Index $i
    Add-DistributionGroupMember -Identity $skrzynka -Member $user
    Write-Output "Użytkownik $user dodany do dg $skrzynka"
    
}