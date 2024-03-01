# Підключення до Active Directory
Import-Module ActiveDirectory

# Введіть частину імені комп'ютера, яку ви шукаєте


# Знаходження комп'ютерів за частиною імені

$lines = Get-Content -Path "C:\Users\30002084\Desktop\kompy.txt" | Measure-Object -Line | Select-Object -ExpandProperty Lines

for ($i = 0; $i -ne $lines; $i++){
$partialComputerName = Get-Content -Path "C:\Users\30002084\Desktop\kompy.txt" | Select-Object -Index $i
$computers = Get-ADComputer -Filter {Name -like $partialComputerName}
# Видалення знайдених комп'ютерів
    foreach ($computer in $computers) {
        Remove-ADComputer -Identity $computer
}
}
