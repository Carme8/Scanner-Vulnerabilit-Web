# Scanner Vulnerabilità Web

Il progetto è uno scanner di vulnerabilità web che combina l'uso delle librerie Python request , BeautifulSoup e tkinter per analizzare pagine web alla ricerca di vulnerabilità comuni.
L'applicazione fornisce un'interfaccia grafica intuitiva per facilitarne l'uso.

# Funzionalità principali:
URL di scansione: consentire agli utenti di inserire un URL per l'analisi.

Semplificare l'identificazione delle vulnerabilità comuni nei siti web.

Aumentare la consapevolezza sulla sicurezza informatica.

Offrire una piattaforma didattica per imparare le basi della sicurezza web.

Questo progetto è ideale per chi desidera esplorare la sicurezza informatica in modo pratico ed educativo.

# Controllo Vulnerabilità:

• Effettua una richiesta GET all'URL fornito.

• Controlla la presenza della parola "vulnerable" nel contenuto.

• Analizza il contenuto per cercare commenti HTML.

• Controlla la presenza di form senza protezione.

• Gestisce gli errori e verifica il codice di stato della risposta.

• Recupera l'URL dall'input dell'utente e verifica se è valido.

• Chiama la funzione di controllo delle vulnerabilità e mostra i risultati.


# Include i controlli per SQL Injection + Cross-Site Scripting (XSS)

# Controllo per SQL Injection:

• Viene effettuata una richiesta GET all'URL con un payload di SQL Injection comune (' OR '1'='1).
Se la risposta contiene errori relativi a SQL, viene segnalata una possibile vulnerabilità.

# Controllo per XSS:

• Viene inviata una richiesta GET all'URL con un payload di test XSS (<script>alert('XSS')</script>).
Se il payload appare nella risposta, viene segnalata una possibile vulnerabilità XSS.

<img width="445" alt="Anteprima Scanner Vulnerabilità Web" src="https://github.com/user-attachments/assets/9badff36-bb27-4dfb-b66f-ddf26b95cc98" />


Utilizzo Responsabile: Questo scanner è solo a scopo didattico. 

Non utilizzare su siti web senza autorizzazione esplicita.

Testare in Sicurezza: Esegui sempre test di sicurezza in un ambiente controllato e autorizzato.



# Dipendenze:

• È richiesto Python 3.13.0.

• Sono richiesti i moduli: Requests, BeautifulSoup, Tkinter, Messagebox.
