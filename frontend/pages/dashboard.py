"""Dashboard page - device overview and quick controls."""
import streamlit as st
from backend.services import set_device_state


def dashboard_page(db):
    """Dashboard - device overview and quick controls."""
    st.subheader("📊 Device Dashboard — **Full Stack Module**")
    cols = st.columns(4)
    idx = 0

    for name, dev in db["devices"].items():
        with cols[idx % 4]:
            st.markdown(f"### {name}")
            state_badge = (
                f"🟢 {dev.state}" if dev.state not in ["OFF", "LOCKED"] else f"🔴 {dev.state}"
            )
            st.markdown(f"**Status:** {state_badge}")

            if name == "Light":
                c1, c2, c3 = st.columns(3)
                if c1.button("OFF", key=f"{name}_off"):
                    ok, msg = set_device_state(db, name, "OFF")
                    st.toast(msg, icon="✅" if ok else "❌")
                if c2.button("DIM", key=f"{name}_dim"):
                    ok, msg = set_device_state(db, name, "DIM")
                    st.toast(msg, icon="✅" if ok else "❌")
                if c3.button("ON", key=f"{name}_on"):
                    ok, msg = set_device_state(db, name, "ON")
                    st.toast(msg, icon="✅" if ok else "❌")

            elif name == "Fan":
                c1, c2, c3, c4 = st.columns(4)
                for label, col in zip(["OFF", "LOW", "MEDIUM", "HIGH"], [c1, c2, c3, c4]):
                    if col.button(label, key=f"{name}_{label}"):
                        ok, msg = set_device_state(db, name, label)
                        st.toast(msg, icon="✅" if ok else "❌")

            elif name == "AC":
                c1, c2, c3 = st.columns(3)
                for label, col in zip(["OFF", "COOL", "HEAT"], [c1, c2, c3]):
                    if col.button(label, key=f"{name}_{label}"):
                        ok, msg = set_device_state(db, name, label)
                        st.toast(msg, icon="✅" if ok else "❌")

            elif name == "Door":
                c1, c2 = st.columns(2)
                if c1.button("LOCK", key=f"{name}_LOCKED"):
                    ok, msg = set_device_state(db, name, "LOCKED")
                    st.toast(msg, icon="✅" if ok else "❌")
                if c2.button("UNLOCK", key=f"{name}_UNLOCKED"):
                    ok, msg = set_device_state(db, name, "UNLOCKED")
                    st.toast(msg, icon="✅" if ok else "❌")

        idx += 1
