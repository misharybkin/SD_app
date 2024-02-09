# Zaloguj się do Azure AD
Connect-AzureAD

# Podaj adres e-mail użytkownika
$userEmailAddress = "A.Wieruch2@lot.pl"

# Pobierz wszystkie grupy, do których użytkownik jest przypisany
$groups = Get-AzureADUserMembership -ObjectId (Get-AzureADUser -Filter "Mail eq '$userEmailAddress'").ObjectId

$emailAddresses = $groups | ForEach-Object { $_.Mail }

$emailAddresses