
Import-Module ExchangeOnlineManagement

Connect-ExchangeOnline -UserPrincipalName 30002084@lot.pl

# Підключення до Exchange сервера (введіть свої дані)


# Отримання повного списку членів дистрибуційної групи (введіть ім'я групи)
$DistributionGroupName = "ndctech@lot.pl"
$GroupMembers = Get-DistributionGroupMember -Identity $DistributionGroupName

# Виведення інформації про членів групи
$GroupMembers | Select PrimarySmtpAddress

# Відключення сесії після завершення

