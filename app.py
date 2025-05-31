import streamlit as st
st.set_page_config(page_title="Gold Bias Dashboard", layout="wide")
import plotly.graph_objs as go
from data_sources import *
import time

# ⏱ Auto-Refresh alle 15 Minuten
st.query_params(t=int(time.time()))
st.markdown(f"<meta http-equiv='refresh' content='900'>", unsafe_allow_html=True)

# 🔘 Manueller Refresh
if st.button("🔄 Jetzt manuell aktualisieren"):
    st.experimental_rerun()

st.set_page_config(page_title="Gold Bias Dashboard", layout="wide")

st.title("📊 Gold Bias Dashboard")
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

col4, col5, col6 = st.columns(3)
col4.metric("10Y Treasury", f"{get_yield_10y():.2f} %")
col5.metric("IG Sentiment", f"{get_ig_sentiment()} % Long")
col6.metric("CoT Netto-Longs", f"{get_cot_data():,}")

st.markdown("---")

# Bias-Ampel
bias = "🔴 Short" if get_ig_sentiment() > 60 and get_cot_data() < 180000 else "🟡 Neutral"
st.subheader(f"Aktueller Bias: {bias}")
