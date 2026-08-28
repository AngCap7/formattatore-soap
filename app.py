import streamlit as st
from groq import Groq

# Ricordati di usare una NUOVA chiave!
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.title("🩺 Formattatore Appunti Clinici (SOAP)")

st.warning("⚠️ PRIVACY: Non inserire dati sensibili (nome, cognome, CF) del paziente.")

appunti_grezzi = st.text_area("Appunti veloci della visita:", height = 150)

if st.button("Genera Referto SOAP"):

    #controlla effettivamente se ci sono appunti presi dal medico
    if appunti_grezzi:

        # Le istruzioni ferree per il nostro modello
        prompt_sistema = """Sei un assistente medico. Il tuo compito è riorganizzare gli appunti grezzi nel formato standard SOAP (Subjective, Objective, Assessment, Plan).
        Regole:
        1. NON inventare o dedurre sintomi, diagnosi o terapie.
        2. Se un dato (S, O, A, P) manca, scrivi 'Dato non specificato'.
        3. Restituisci solo il referto finale in formato Markdown."""

        # Mostra una rotellina di caricamento mentre attendiamo la risposta
        with st.spinner("Elaborazione e formattazione in corso..."):

            # La chiamata vera e propria ai server di Groq
            risposta = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": prompt_sistema},
                    {"role": "user", "content": appunti_grezzi }
                ],
                model = "qwen/qwen3.8-27b",
                temperature = 0.1   ## Temperatura bassissima = zero creatività, massima precisione
            )
            
        # Estraiamo il testo dalla risposta di Groq e lo stampiamo a schermo
        st.success("Referto completato!")
        testo_referto = risposta.choices[0].message.content
        st.markdown(testo_referto)
        
        # NUOVO CODICE: Il bottone per scaricare il file
        st.download_button(
            label="📥 Scarica Referto (.pdf)",
            data=testo_referto,
            file_name="referto_SOAP.pdf",
            mime="text/plain"
        )

    else:
        # Messaggio di errore se il medico clicca il bottone senza aver scritto nulla
        st.error("Per favore, inserisci degli appunti prima di generare il referto.")
