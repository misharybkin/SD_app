# Підключення до Active Directory
Import-Module ActiveDirectory

# Читання імен комп'ютерів з файлу
$computerNames = Get-Content -Path "C:\Users\30002084\Desktop\kompy.txt"

foreach ($partialComputerName in $computerNames) {

    
    # Знаходження комп'ютерів за частиною імені
    $computers = Get-ADComputer -Filter {Name -like $partialComputerName}

    # Видалення знайдених комп'ютерів
    foreach ($computer in $computers) {
        $childComputers = Get-ADComputer -Filter "Name -like '$($computer.Name)*'"

        # Видалення всіх підкомп'ютерів
        foreach ($childComputer in $childComputers) {
            Remove-ADComputer -Identity $childComputer -Confirm:$false
        }

        # Видалення батьківського комп'ютера
        Remove-ADComputer -Identity $computer -Confirm:$false
    }
}
