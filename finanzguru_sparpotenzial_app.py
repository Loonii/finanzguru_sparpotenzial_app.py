
import streamlit as st
import pandas as pd

contracts = [
    {
        "current_provider": "CSS",
        "current_price": 324.0,
        "cheapest_alternative": "Wingo",
        "product": "Fair Flat 2GB",
        "new_price": 29.0,
        "monthly_saving": 295.0,
        "annual_saving": 3540.0
    },
    {
        "current_provider": "Salt",
        "current_price": 69.0,
        "cheapest_alternative": "Wingo",
        "product": "Fair Flat 2GB",
        "new_price": 29.0,
        "monthly_saving": 40.0,
        "annual_saving": 480.0
    }
]

st.set_page_config(page_title="Finanzguru CH – Sparpotenzial", layout="centered")

st.title("💰 Deine Sparpotenziale")

for contract in contracts:
    with st.container():
        st.subheader(f"{contract['current_provider']} → {contract['cheapest_alternative']}")
        st.write(f"Aktueller Vertrag: **CHF {contract['current_price']}/Monat**")
        st.write(f"Besseres Angebot: **{contract['product']} für CHF {contract['new_price']}/Monat**")
        st.success(f"💸 Du kannst **CHF {contract['annual_saving']}/Jahr** sparen!")
        if st.button(f"Wechseln zu {contract['cheapest_alternative']} ({contract['product']})", key=contract['current_provider']):
            st.info("Wechsel-Stub ausgelöst – hier kommt bald der Kündigungsprozess 😉")
        st.markdown("---")
