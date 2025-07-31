
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Finanzguru CH – Vertrags-Erkennung", layout="centered")
st.title("🔍 Automatische Vertragserkennung aus Transaktionen")

uploaded_file = st.file_uploader("📎 Lade deine Transaktionen als CSV hoch", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📄 Hochgeladene Transaktionen")
    st.dataframe(df)

    # Liste bekannter Anbieter (vereinfachte Heuristik)
    bekannte_vertragspartner = ["CSS", "Salt", "Sunrise", "UPC", "Helsana", "Sanitas", "Swisscom"]

    # Vertragserkennung basierend auf Empfänger und Wiederholungen
    df["Erkannt als Vertrag"] = df["Empfänger"].apply(
        lambda x: any(anbieter.lower() in x.lower() for anbieter in bekannte_vertragspartner)
    )

    # Gruppieren nach Empfänger und zählen
    counts = df[df["Erkannt als Vertrag"]].groupby("Empfänger").size()

    if not counts.empty:
        st.subheader("📑 Erkannte Verträge")
        for empfänger, anzahl in counts.items():
            monatlicher_betrag = df[df["Empfänger"] == empfänger]["Betrag"].mean()
            alternative = round(monatlicher_betrag * 0.8, 2)  # Dummy-Sparvorschlag: 20% günstiger
            st.markdown(f"""
**{empfänger}**  
🔁 Zahlungen erkannt: {anzahl}  
💰 Aktueller Betrag: CHF {monatlicher_betrag:.2f}/Monat  
💡 Vorschlag: Günstigere Alternative für CHF {alternative}/Monat  
---
""")
    else:
        st.info("Keine regelmässigen Vertragszahlungen erkannt.")
else:
    st.info("Bitte lade zuerst eine Transaktionsdatei im CSV-Format hoch.")
