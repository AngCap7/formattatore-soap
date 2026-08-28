# 🩺 Formattatore Appunti Clinici (SOAP)

Una Web App basata sull'Intelligenza Artificiale che trasforma appunti medici grezzi, disordinati e presi di fretta nel formato clinico standard internazionale **SOAP** (Subjective, Objective, Assessment, Plan).

L'applicazione è progettata con un focus rigoroso sulla sicurezza clinica: il modello IA è istruito per **non allucinare** (non inventare sintomi, diagnosi o terapie non presenti nel testo originale). Se un dato manca, il sistema lo segnala esplicitamente.

## ✨ Funzionalità Principali

* **Formattazione Intelligente:** Riconosce il linguaggio medico e categorizza automaticamente i dati grezzi nelle 4 sezioni del referto SOAP.
* **Anti-Allucinazione:** Prompting ingegnerizzato per impedire all'IA di dedurre informazioni cliniche non fornite dal medico.
* **Esportazione in PDF:** Generazione istantanea del referto in formato PDF pulito e pronto per l'archiviazione o la stampa.
* **Elaborazione Ultra-Veloce:** Utilizza l'infrastruttura Groq e il modello *Llama 3.3 70B* per generare referti in frazioni di secondo.

## 🛠️ Tecnologie Utilizzate

* **Python 3**
* **Streamlit:** Per l'interfaccia utente (UI) e il web hosting.
* **Groq API:** Per l'elaborazione del linguaggio naturale a bassissima latenza.
* **FPDF2:** Per la generazione del documento PDF.

## 🚀 Come usare l'app in locale (sul tuo PC)

1. **Clona il repository:**
   Scarica i file del progetto sul tuo computer.

2. **Installa le dipendenze:**
   Apri il terminale nella cartella del progetto ed esegui:
   `pip install -r requirements.txt`

3. **Configura la chiave API (Groq):**
   Crea una cartella chiamata `.streamlit` nella directory principale.
   Al suo interno, crea un file chiamato `secrets.toml` e aggiungi la tua chiave API in questo formato:
   `GROQ_API_KEY = "gsk_la_tua_chiave_qui"`

4. **Avvia l'applicazione:**
   Da terminale esegui:
   `streamlit run app.py`

## ☁️ Deploy (Streamlit Community Cloud)

Per mettere l'app online gratuitamente:
1. Carica questo repository sul tuo account GitHub.
2. Vai su [Streamlit Cloud](https://share.streamlit.io/) e crea una nuova app collegandola al repository.
3. Nelle impostazioni dell'app su Streamlit (Settings > Secrets), inserisci la tua chiave API:
   `GROQ_API_KEY = "gsk_la_tua_chiave_qui"`

## ⚠️ Disclaimer e Privacy

**Attenzione:** Questa applicazione è uno strumento di supporto alla produttività e non sostituisce il giudizio clinico di un professionista sanitario. 
Si raccomanda vivamente di **NON inserire dati sensibili reali (Nome, Cognome, Codice Fiscale, ecc.)** che possano identificare direttamente il paziente durante l'utilizzo dell'app, al fine di rispettare le normative sulla privacy (GDPR).
