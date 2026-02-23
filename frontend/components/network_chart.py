"""Network chart component."""
import streamlit as st
import pandas as pd


def show_network_chart(netlogs, title="Latency Chart (Last 100)"):
    """Display network latency chart."""
    st.markdown(f"### {title}")
    if netlogs:
        logs = netlogs[-100:]
        df = pd.DataFrame({
            "t": [x.timestamp for x in logs],
            "latency_ms": [x.latency_ms for x in logs]
        })
        df = df.set_index("t")
        st.line_chart(df)
    else:
        st.info("No logs yet.")
