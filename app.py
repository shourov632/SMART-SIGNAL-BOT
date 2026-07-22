import streamlit as st
from tradingview_ta import TA_Handler, Interval
from datetime import datetime
from zoneinfo import ZoneInfo

st.set_page_config(
    page_title="SMART SIGNAL BOT V11",
    page_icon="📈",
    layout="wide"
)

st.title("🤖 SMART SIGNAL BOT V11 PRO")
st.write("Forex Live Signal Scanner")

bd_time = datetime.now(ZoneInfo("Asia/Dhaka"))

st.success(
    "🇧🇩 Bangladesh Time : " +
    bd_time.strftime("%d-%m-%Y %I:%M:%S %p")
)

pairs = [
    "EURUSD",
    "GBPUSD",
    "USDJPY",
    "AUDUSD",
    "USDCAD",
    "USDCHF",
    "NZDUSD"
]
