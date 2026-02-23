"""
Home Automation System - Main Streamlit App
Integrated subjects: Formal Language & Automata • Full Stack Development • Computer Networks
"""
from __future__ import annotations
import streamlit as st
from datetime import datetime

# Import backend modules
from backend.models import User, Device, ScheduleRule, NetLog
from backend.automata import DEVICE_DFA, valid_transition
from backend.utils.websocket_server import mobile_latency_data
from backend.utils.network_sim import send_network_command
from backend.services import set_device_state, process_due_schedules

# Import frontend modules
from frontend.auth.login import login_view
from frontend.auth.register import register_view
from frontend.pages.dashboard import dashboard_page
from frontend.pages.device_manager import device_state_manager_page
from frontend.pages.scheduling import scheduling_page
from frontend.pages.network_monitor import network_monitor_page
from frontend.pages.device_connectivity import device_connectivity_page
from frontend.pages.mobile_latency import mobile_latency_page
from frontend.pages.automata_simulator import automata_simulator_page
from frontend.pages.profile import profile_page
from frontend.components.sidebar import show_sidebar

# ==============================
# --- Page Configuration ---
# ==============================

st.set_page_config(
    page_title="Home Automation – Automata • FS • Networks",
    layout="wide"
)

# Header
st.markdown("""
# 🏠 Home Automation System""")


# ==============================
# --- Initialize Session State ---
# ==============================

if "db" not in st.session_state:
    st.session_state.db = {
        "users": {
            "ullas": User(username="ullas", password="1234")
        },
        "devices": {
            "Light": Device(name="Light", ip="192.168.1.20", mac="AA:BB:CC:11:22:33", state="OFF"),
            "Fan": Device(name="Fan", ip="192.168.1.21", mac="AA:BB:CC:44:55:66", state="OFF"),
            "AC": Device(name="AC", ip="192.168.1.22", mac="AA:BB:CC:77:88:99", state="OFF"),
            "Door": Device(name="Door", ip="192.168.1.23", mac="AA:BB:CC:00:11:22", state="LOCKED"),
        },
        "schedules": [],
        "netlogs": [],
        "next_rule_id": 1,
    }

DB = st.session_state.db

# ==============================
# --- Authentication Gate ---
# ==============================

if "user" not in st.session_state:
    tabs = st.tabs(["Login", "Register"])
    with tabs[0]:
        login_view(DB)
    with tabs[1]:
        register_view(DB)
    st.stop()

# ==============================
# --- Process Schedules ---
# ==============================

process_due_schedules(DB, datetime.now())

# ==============================
# --- Sidebar Navigation ---
# ==============================

page = show_sidebar(DB)

# ==============================
# --- PAGE ROUTING ---
# ==============================

if page == "Dashboard":
    dashboard_page(DB)

elif page == "Device State Manager":
    device_state_manager_page(DB)

elif page == "Scheduling":
    scheduling_page(DB)

elif page == "Network Monitor":
    network_monitor_page(DB)

elif page == "Device Connectivity":
    device_connectivity_page(DB)

elif page == "Mobile Network Latency":
    mobile_latency_page(DB)

elif page == "Automata Simulator":
    automata_simulator_page(DB)

elif page == "Profile":
    profile_page(DB)

# Footer
st.markdown("---")
st.markdown(
    "**Legend:** 🧮 Automata  •  🧩 Full Stack  •  🌐 Networks  — Buttons are functional with DFA checks & network log simulation."
)
