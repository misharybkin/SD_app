import tkinter as tk
from tkinter import ttk
import subprocess
from flask import Flask, request, jsonify

#1st tab content
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
        self.progressbar = ttk.Progressbar(self.frame, length=200, mode="determinate")
        self.progressbar.pack(pady=5)
        self.text_var = tk.Text(self.frame, height=5,  width=30)
        self.text_var.pack(pady=10)
        self.button = tk.Button(self.frame, text="Uruchom polecenie", command=self.on_button_click)
        self.button.pack(pady=8)
    def on_button_click(self):
        
        nr_ewidencyjny = self.entry_var.get()
        print(nr_ewidencyjny)
        skrzynki = self.text_var.get("1.0", tk.END)
        print(skrzynki)
        with open("C:/aplikacja_moja/SD_app/temporary/jeden_user_wiele_skrzynek/skrzynki.txt", "w") as temp_skrzynki:
            temp_skrzynki.truncate()
            temp_skrzynki.write(skrzynki)
        with open ("/aplikacja_moja/SD_app/temporary/jeden_user_wiele_skrzynek/user.txt", "w") as temp_user:
            temp_user.truncate()
            temp_user.write(nr_ewidencyjny)
        
        skrypt = Scripts()
        skrypt.jeden_user_wiele_sw()
    
    
        

#2nd tab content
class Zakladka2:
    def __init__(self, parent, content):
        self.frame = ttk.Frame(parent)
        self.entry_label = tk.Label(self.frame, text = "Wpisz adres skrzynki:")
        self.entry_label.pack(pady=5)
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self.frame, textvariable=self.entry_var)
        self.entry.pack(pady=10)
        self.text_label = tk.Label(self.frame, text="Podaj listę osób:")
        self.text_label.pack(pady=10)
        self.progressbar = ttk.Progressbar(self.frame, length=200, mode="determinate")
        self.progressbar.pack(pady=5)
        self.text_var = tk.Text(self.frame, height=5,  width=30)
        self.text_var.pack(pady=10)
        self.button = tk.Button(self.frame, text="Uruchom polecenie", command=self.on_button_click)
        self.button.pack(pady=8)
    def on_button_click(self):
        self.progressbar.start()
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
        skrypt = Scripts()
        skrypt.jedna_sw_wiele_userow()
        self.progressbar.stop()



#3rd tab content
class Zakladka3:
    def __init__(self, parent, content):
        self.frame = ttk.Frame(parent)
        label = tk.Label(self.frame, text=content)
        self.entry_label = tk.Label(self.frame, text = "Wpisz adres DG:")
        self.entry_label.pack(pady=5)
        self.entry_dg = tk.StringVar()
        self.entry = tk.Entry(self.frame, textvariable=self.entry_dg)
        self.entry.pack(pady=10)
        self.text_label = tk.Label(self.frame, text="Podaj listę osób:")
        self.text_label.pack(pady=10)
        self.text_numer = tk.Text(self.frame, height=5,  width=30)
        self.text_numer.pack(pady=10)
        self.progressbar = ttk.Progressbar(self.frame, length=200, mode="determinate")
        self.progressbar.pack(pady=5)
        
        
        self.button = tk.Button(self.frame, text="Uruchom polecenie", command=self.on_button_click)
        self.button.pack(pady=8)
    def on_button_click(self):
        self.progressbar.start()
        nr_ewidencyjny = self.text_numer.get("1.0", tk.END)
        print(nr_ewidencyjny)
        skrzynki = self.entry_dg.get()
        print(skrzynki)
        with open("C:/aplikacja_moja/SD_app/temporary/jedna_dg_wiele_userow/dg.txt", "w") as temp_skrzynki:
            temp_skrzynki.truncate()
            temp_skrzynki.write(skrzynki)
        with open ("C:/aplikacja_moja/SD_app/temporary/jedna_dg_wiele_userow/userzy.txt", "w") as temp_user:
            temp_user.truncate()
            temp_user.write(nr_ewidencyjny)
        skrypt = Scripts()
        skrypt.jedna_dg_wiele_userow()
        self.progressbar.stop()


class Zakladka4:
    def __init__(self, parent, content):
        self.frame = ttk.Frame(parent)
        label = tk.Label(self.frame, text=content)
        self.entry_label = tk.Label(self.frame, text = "Wpisz adres czy nr ewidencyjny osoby:")
        self.entry_label.pack(pady=5)
        self.entry_dg = tk.StringVar()
        self.entry = tk.Entry(self.frame, textvariable=self.entry_dg)
        self.entry.pack(pady=10)
        self.text_label = tk.Label(self.frame, text="Podaj listę DG:")
        self.text_label.pack(pady=10)
        self.text_numer = tk.Text(self.frame, height=5,  width=30)
        self.text_numer.pack(pady=10)
        self.progressbar = ttk.Progressbar(self.frame, length=200, mode="determinate")
        self.progressbar.pack(pady=5)
        
        
        self.button = tk.Button(self.frame, text="Uruchom polecenie", command=self.on_button_click)
        self.button.pack(pady=8)
    def on_button_click(self):
        self.progressbar.start()
        nr_ewidencyjny = self.text_numer.get("1.0", tk.END)
        print(nr_ewidencyjny)
        user = self.entry_dg.get()
        
        with open("C:/aplikacja_moja/SD_app/temporary/jeden_user_wiele_dg/users.txt", "w") as temp_user:
            temp_user.truncate()
            temp_user.write(user)
        with open ("C:/aplikacja_moja/SD_app/temporary/jeden_user_wiele_dg/dg.txt", "w") as temp_dg:
            temp_dg.truncate()
            temp_dg.write(nr_ewidencyjny)
        skrypt = Scripts()
        skrypt.jedna_dg_wiele_userow()
        self.progressbar.stop()

class Scripts:
    #One distribution group to many users script implementation
    def jedna_dg_wiele_userow(self):
        powershell_script_path = r"C:\aplikacja_moja\SD_app\scripts\jedna_dg_wiele_userow.ps1"
        with subprocess.Popen(['powershell.exe', '-ExecutionPolicy', 'Unrestricted', '-File', powershell_script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as process:
            stdout, stderr = process.communicate()
    
            print("Standard Output:")
            print(stdout)
    
            print("Error Output:")
            print(stderr)
    #One shared mailbox to many users script implementation
    def jedna_sw_wiele_userow(self):
        powershell_script_path = r"C:\aplikacja_moja\SD_app\scripts\jedna_skrzynka_wiele_uzytkownikow.ps1"
        with subprocess.Popen(['powershell.exe', '-ExecutionPolicy', 'Unrestricted', '-File', powershell_script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as process:
            stdout, stderr = process.communicate()
    
            print("Standard Output:")
            print(stdout)
    
            print("Error Output:")
            print(stderr)
        

    def jeden_user_wiele_sw(self):
        powershell_script_path = r"C:\aplikacja_moja\SD_app\scripts\jeden_uzytkownik_wiele_skrzynek.ps1"
        
        with subprocess.Popen(['powershell.exe', '-ExecutionPolicy', 'Unrestricted', '-File', powershell_script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as process:
            
            print("Прогрес завершено")
            stdout, stderr = process.communicate()
    
            print("Standard Output:")
            print(stdout)
    
            print("Error Output:")
            print(stderr)
    def jeden_user_wiele_dg(self):
        powershell_script_path = r"C:\aplikacja_moja\SD_app\scripts\wiele_dg_jeden_user.ps1"
        
        with subprocess.Popen(['powershell.exe', '-ExecutionPolicy', 'Unrestricted', '-File', powershell_script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as process:
            
            print("Прогрес завершено")
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

        tab3_content = Zakladka3(self.notebook, "22")
        self.notebook.add(tab3_content.frame, text="1 DG - wiele użytkowników")

        tab4_content = Zakladka4(self.notebook, "22")
        self.notebook.add(tab4_content.frame, text="1 user - wiele DG")

api = Flask(__name__)
@api.route('/api/jedna_dg_wiele_userow', methods=['POST'])
def jedna_dg_wiele_userow():
    data = request.get_json()
    nr_ewidencyjny = data.get('nr_ewidencyjny')
    skrzynki = data.get('skrzynki')

    with open("C:/aplikacja_moja/SD_app/temporary/jedna_dg_wiele_userow/dg.txt", "w") as temp_skrzynki:
        temp_skrzynki.truncate()
        temp_skrzynki.write(skrzynki)

    with open("C:/aplikacja_moja/SD_app/temporary/jedna_dg_wiele_userow/userzy.txt", "w") as temp_user:
        temp_user.truncate()
        temp_user.write(nr_ewidencyjny)

    skrypt = Scripts()
    skrypt.jedna_dg_wiele_userow()

    return jsonify({'status': 'success'})




if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.geometry("700x600")
    root.mainloop()
    api.run(debug=True)