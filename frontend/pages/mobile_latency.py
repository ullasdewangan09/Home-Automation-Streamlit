"""Mobile Network Latency page - Networks module."""
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from backend.utils.websocket_server import mobile_latency_data


def mobile_latency_page(db):
    """Real-Time Mobile Network Latency - Networks module."""
    st.subheader("📱 Real-Time Mobile Network Latency — Networks Module")

    st.markdown("""
    This feature measures your **mobile network latency** in real time.
    Follow these steps:
    1️⃣ Make sure your **mobile and PC are on the same Wi-Fi network**.
    2️⃣ Open this Streamlit page on your **phone browser** (scan QR or enter local IP).
    3️⃣ Allow the page to run latency checks — data will appear below.
    """)

    st.info("📡 WebSocket server running at: `ws://<your-PC-IP>:8765`")

    # Embedded JavaScript for mobile latency measurement
    components.html(
        """
        <script>
        const ws = new WebSocket("ws://" + location.hostname + ":8765");

        ws.onopen = () => console.log("✅ WebSocket connected");
        ws.onerror = (e) => console.error("❌ WebSocket error", e);

        async function pingLoop() {
          while (true) {
            const start = performance.now();
            try {
              await fetch("/", { cache: "no-store" });
              const latency = performance.now() - start;

              if (ws.readyState === WebSocket.OPEN) {
                ws.send(latency.toFixed(2));
              }
            } catch (e) {
              console.error("Ping failed", e);
            }
            await new Promise(r => setTimeout(r, 2000));
          }
        }

        pingLoop();
        </script>
        """,
        height=0,
    )

    # Display live latency metrics
    if mobile_latency_data:
        st.success("🟢 Mobile connected — receiving live latency data")

        latest_time, latest_latency = mobile_latency_data[-1]
        values = [lat for _, lat in mobile_latency_data]

        col1, col2, col3 = st.columns(3)
        col1.metric("📡 Latest Latency", f"{latest_latency:.2f} ms")
        col2.metric("📉 Min Latency", f"{min(values):.2f} ms")
        col3.metric("📈 Max Latency", f"{max(values):.2f} ms")

        st.markdown("---")

        df = pd.DataFrame(
            mobile_latency_data,
            columns=["timestamp", "latency_ms"]
        )
        st.line_chart(df.set_index("timestamp")["latency_ms"])
    else:
        st.info("⏳ Waiting for mobile to connect... Open this page on your phone.")
