import streamlit as st
st.set_page_config(page_title="Gold Bias Dashboard", layout="wide")  # Muss ganz oben stehen

import time
from data_sources import *

# ⏱ Auto-Refresh alle 15 Minuten
st.markdown(f"<meta http-equiv='refresh' content='900'>", unsafe_allow_html=True)

# 🔘 Manueller Refresh
if st.button("🔄 Jetzt manuell aktualisieren"):
    st.experimental_rerun()

# 🧱 Titel
st.title("📊 Gold Bias Dashboard")

# 🔢 Einzelne Werte abrufen
gold = get_gold_price()
dxy = get_dxy()
vix = get_vix()
yield_10y = get_yield_10y()
ig_sent = get_ig_sentiment()
cot = get_cot_data()

# 🧾 Live-Metriken Block 1
col1, col2, col3 = st.columns(3)

if gold:
    col1.metric("Goldpreis", f"${gold:,.2f}")
else:
    col1.metric("Goldpreis", "❌ Fehler")

if dxy:
    col2.metric("DXY", f"{dxy:.2f}")
else:
    col2.metric("DXY", "❌ Fehler")

if vix:
    col3.metric("VIX", f"{vix:.2f}")
else:
    col3.metric("VIX", "❌ Fehler")

# 🧾 Live-Metriken Block 2
col4, col5, col6 = st.columns(3)

if yield_10y:
    col4.metric("10Y Treasury", f"{yield_10y:.2f} %")
else:
    col4.metric("10Y Treasury", "❌ Fehler")

if ig_sent is not None:
    col5.metric("IG Sentiment", f"{ig_sent}% Long")
else:
    col5.metric("IG Sentiment", "❌ Fehler")

if cot:
    col6.metric("CoT Netto-Longs", f"{cot:,}")
else:
    col6.metric("CoT Netto-Longs", "❌ Fehler")

# 🧠 Bias-Berechnung
st.markdown("---")

def determine_bias(cot, ig):
    if cot is None or ig is None:
        return "⚠️ unklar"
    elif cot < 180000 and ig > 60:
        return "🔴 Short"
    elif cot > 200000 and ig < 40:
        return "🟢 Long"
    else:
        return "🟡 Neutral"

bias = determine_bias(cot, ig_sent)
st.subheader(f"Aktueller Bias: {bias}")
