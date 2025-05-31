import streamlit as st
st.set_page_config(page_title="Gold Bias Dashboard", layout="wide")  # Muss ganz oben stehen

import plotly.graph_objs as go
from data_sources import *
import time

# ⏱ Auto-Refresh alle 15 Minuten
st.markdown(f"<meta http-equiv='refresh' content='900'>", unsafe_allow_html=True)

# 🔘 Manueller Refresh
if st.button("🔄 Jetzt manuell aktualisieren"):
    st.experimental_rerun()

st.title("📊 Gold Bias Dashboard")

# Goldpreis
gold_price = get_gold_price()
if gold_price:
    st.metric("Goldpreis (Spot)", f"${gold_price:,.2f}")
else:
    st.warning("Goldpreis konnte nicht geladen werden.")

# Live-Werte
col1, col2, col3 = st.columns(3)
col1.metric("Goldpreis", f"${get_gold_price():,.2f}")
col2.metric("DXY", f"{get_dxy():.2f}")
col3.metric("VIX", f"{get_vix():.2f}")
