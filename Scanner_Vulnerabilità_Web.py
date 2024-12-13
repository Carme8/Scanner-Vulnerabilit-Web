import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox

# FUNZIONI PER CONTROLLARE VULNERABILITÀ COMUNI
def check_vulnerabilities(url):
    vulnerabilities = []
    
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # CONTROLLO PER VULNERABILITÀ COMUNI
        if "vulnerable" in soup.text:
            vulnerabilities.append("Possibile vulnerabilità trovata: 'vulnerable' nel contenuto.")
        
        # CONTROLLO PER PRESENZA DI COMMENTI HTML
        if "<!--" in soup.text:
            vulnerabilities.append("Commenti HTML trovati, possono rivelare informazioni.")
        
        # CONTROLLO PER FORM SENZA PROTEZIONE
        forms = soup.find_all('form')
        if forms:
            vulnerabilities.append(f"Trovati {len(forms)} form(s) nella pagina. Controllare se sono protetti.")
        
        # CONTROLLO PER RISPOSTE DI ERRORE COMUNI (e.g., 404)
        if response.status_code != 200:
            vulnerabilities.append(f"Errore: codice di stato {response.status_code}.")

        # CONTROLLO PER SQL Injection
        sql_injection_test = "' OR '1'='1"
        sql_response = requests.get(url + "?id=" + sql_injection_test)
        if "error" in sql_response.text.lower() or "mysql" in sql_response.text.lower():
            vulnerabilities.append("Possibile vulnerabilità di SQL Injection rilevata.")

        # CONTROLLO PER XSS
        xss_test = "<script>alert('XSS')</script>"
        xss_response = requests.get(url + "?input=" + xss_test)
        if xss_test in xss_response.text:
            vulnerabilities.append("Possibile vulnerabilità XSS rilevata.")

    except Exception as e:
        vulnerabilities.append(f"Errore durante la richiesta: {str(e)}")

    return vulnerabilities

# FUNZIONE PER AVVIARE LA SCANSIONE E MOSTRARE I RISULTATI
def scan_vulnerability(event=None):  
    url = url_entry.get()
    if not url.startswith("http://") and not url.startswith("https://"):
        messagebox.showerror("Errore", "Inserisci un URL valido che inizi con 'http://' o 'https://'.")
        return
    
    results = check_vulnerabilities(url)
    if results:
        result_text = "\n".join(results)
    else:
        result_text = "Nessuna vulnerabilità trovata."
    
    result_label.config(text=result_text)

# FUNZIONE PER RESETTARE L'INTERFACCIA
def reset_fields(event=None):  
    url_entry.delete(0, tk.END)  
    result_label.config(text="")   

# INTERFACCIA GRAFICA
root = tk.Tk()
root.title("Scanner di Vulnerabilità Web")
root.geometry("450x300")
root.configure(bg='#ececec')

# LAYOUT INTERFACCIA
tk.Label(root, text="Inserisci l'URL da scansionare:", bg='#ececec', fg='black', font=('BigNoodleTitling', 16)).pack(pady=10)

url_entry = tk.Entry(root, width=50, bg='white', fg='black', font=('BigNoodleTitling', 16))
url_entry.pack(pady=5)

# FRAME BUTTONS
button_frame = tk.Frame(root, bg='#ececec')
button_frame.pack(pady=20)

scan_button = tk.Button(button_frame, text="Scansiona", command=scan_vulnerability, bg='lightblue', fg='black', font=('BigNoodleTitling', 16))
scan_button.pack(side=tk.LEFT, padx=5)

reset_button = tk.Button(button_frame, text="Reset", command=reset_fields, bg='lightcoral', fg='black', font=('BigNoodleTitling', 16))
reset_button.pack(side=tk.LEFT, padx=5)

result_label = tk.Label(root, bg='#ececec', fg='black', font=('BigNoodleTitling', 16), justify='left')
result_label.pack(pady=10)

# BINDING DEL TASTO INVIO SACNSIONE E RESET
url_entry.bind("<Return>", scan_vulnerability)
url_entry.bind("<Control-r>", reset_fields)  # command + R PER ESEGUIRE RESET

root.mainloop()