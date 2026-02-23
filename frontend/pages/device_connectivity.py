"""Device Connectivity page - Networks module."""
import streamlit as st


def device_connectivity_page(db):
    """Device Connectivity - Networks module."""
    st.subheader("📶 Device Connectivity — **Networks Module**")

    grid = st.columns(2)
    i = 0
    for name, dev in db["devices"].items():
        with grid[i % 2]:
            st.markdown(f"#### {name}")
            st.write(f"IP: `{dev.ip}`  |  MAC: `{dev.mac}`")
            status = "🟢 Online" if dev.online else "🔴 Offline"
            st.write(f"Status: **{status}**")
            toggle = st.button("Toggle Online/Offline", key=f"net_{name}")
            if toggle:
                dev.online = not dev.online
                st.toast(f"{name} is now {'Online' if dev.online else 'Offline'}", icon="🔌")
        i += 1
