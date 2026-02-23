"""Network Monitor page - Networks module."""
import streamlit as st
import pandas as pd
from backend.automata import DEVICE_DFA
from backend.services import set_device_state


def network_monitor_page(db):
    """Network Activity Monitor - Networks module."""
    st.subheader("🌐 Network Activity Monitor — **Networks Module**")

    colA, colB = st.columns([1, 1])
    with colA:
        st.markdown("**Simulate Commands**")
        dev_name = st.selectbox("Device", list(db["devices"].keys()), key="nm_dev")
        proto = st.selectbox("Protocol", ["MQTT", "HTTP"], key="nm_proto")
        allowed = set(DEVICE_DFA.get(dev_name, {}).keys())
        for s in DEVICE_DFA.get(dev_name, {}).values():
            allowed.update(s)
        action = st.selectbox("Action (state)", sorted(list(allowed)), key="nm_action")
        if st.button("Send", key="nm_send"):
            ok, msg = set_device_state(db, dev_name, action, protocol=proto)
            st.toast(msg, icon="✅" if ok else "❌")

    with colB:
        st.markdown("**Quick Stats**")
        last10 = db["netlogs"][-10:]
        if last10:
            avg = sum([n.latency_ms for n in last10]) / len(last10)
            st.metric("Avg Latency (last 10)", f"{avg:.0f} ms")
        st.markdown("**Latest Logs**")
        for n in reversed(last10):
            st.code(
                f"{n.timestamp.strftime('%H:%M:%S')} | {n.device} -> {n.action} | {n.protocol} | {n.status} | {n.latency_ms} ms"
            )

    st.markdown("### Latency Chart (Last 100)")
    if db["netlogs"]:
        logs = db["netlogs"][-100:]
        df = pd.DataFrame({
            "t": [x.timestamp for x in logs],
            "latency_ms": [x.latency_ms for x in logs]
        })
        df = df.set_index("t")
        st.line_chart(df)
    else:
        st.info("No logs yet. Send a command above.")
