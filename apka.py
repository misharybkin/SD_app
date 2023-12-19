import tkinter as tk
from tkinter import ttk
import subprocess

class Zakladka1:
    def __init__(self, parent, content):
        self.frame = ttk.Frame(parent)
        label = tk.Label(self.frame, text=content)
        self.entry_label = tk.Label(self.frame, text = "Wpisz numer ewidencyjny lub email osoby:")
        self.entry_label.pack(pady=5)
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self.frame, textvariable=self.entry_var)
        self.entry.pack(pady=10)
        self.text_label = tk.Label(self.frame, text="Podaj skrzynki, do których chciałbyś dodać użytkownika:")
        self.text_label.pack(pady=10)
        
        self.text_var = tk.Text(self.frame, height=5,  width=30)
        self.text_var.pack(pady=10)
        self.button = tk.Button(self.frame, text="Uruchom polecenie", command=self.on_button_click)
        self.button.pack(pady=8)
    def on_button_click(self):
        nr_ewidencyjny = self.entry_var.get()
        print(nr_ewidencyjny)
        skrzynki = self.text_var.get("1.0", tk.END)
        print(skrzynki)
        with open("C:/aplikacja_moja/1 zakładka/pliczek.txt", "w") as temp_skrzynki:
            temp_skrzynki.truncate()
            temp_skrzynki.write(skrzynki)
        with open ("C:/aplikacja_moja/1 zakładka/user.txt", "w") as temp_user:
            temp_user.truncate()
            temp_user.write(nr_ewidencyjny)
        
        powershell_script_path = r"C:\aplikacja_moja\jeden_uzytkownik_wiele_skrzynek.ps1"

        with subprocess.Popen(['powershell.exe', '-ExecutionPolicy', 'Unrestricted', '-File', powershell_script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as process:
            stdout, stderr = process.communicate()
    
            print("Standard Output:")
            print(stdout)
    
            print("Error Output:")
            print(stderr)


class Zakladka2:
    def __init__(self, parent, content):
        self.frame = ttk.Frame(parent)
        label = tk.Label(self.frame, text=content)
        self.entry_label = tk.Label(self.frame, text = "Wpisz adres skrzynki:")
        self.entry_label.pack(pady=5)
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self.frame, textvariable=self.entry_var)
        self.entry.pack(pady=10)
        self.text_label = tk.Label(self.frame, text="Podaj listę osób:")
        self.text_label.pack(pady=10)
        
        self.text_var = tk.Text(self.frame, height=5,  width=30)
        self.text_var.pack(pady=10)
        self.button = tk.Button(self.frame, text="Uruchom polecenie", command=self.on_button_click)
        self.button.pack(pady=8)
    def on_button_click(self):
        nr_ewidencyjny = self.entry_var.get()
        print(nr_ewidencyjny)
        skrzynki = self.text_var.get("1.0", tk.END)
        print(skrzynki)
        with open("C:/aplikacja_moja/2 zakładka/pliczek.txt", "w") as temp_skrzynki:
            temp_skrzynki.truncate()
            temp_skrzynki.write(skrzynki)
        with open ("C:/aplikacja_moja/2 zakładka/user.txt", "w") as temp_user:
            temp_user.truncate()
            temp_user.write(nr_ewidencyjny)
        powershell_script_path = r"C:\aplikacja_moja\jedna_skrzynka_wiele_uzytkownikow.ps1"
        with subprocess.Popen(['powershell.exe', '-ExecutionPolicy', 'Unrestricted', '-File', powershell_script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as process:
            stdout, stderr = process.communicate()
    
            print("Standard Output:")
            print(stdout)
    
            print("Error Output:")
            print(stderr)


class MyApp:
    def __init__(self, root):
        self.root = root
        root.title("My App")

        # Створення віджету Notebook
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Створення першої закладки
        tab1_content = Zakladka1(self.notebook, "Вміст для закладки 1")
        self.notebook.add(tab1_content.frame, text="1 użytkownik - wiele skrzynek")

        # Створення другої закладки
        tab2_content = Zakladka2(self.notebook, "11")
        self.notebook.add(tab2_content.frame, text="1 skrzynka - wiele użytkowników")

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.geometry("500x400")
    root.mainloop()