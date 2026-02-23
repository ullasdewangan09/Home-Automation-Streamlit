"""Sidebar navigation component."""
import streamlit as st


def show_sidebar(db):
    """Display sidebar navigation and return selected page."""
    st.sidebar.markdown("### 📱 Connect from mobile")

    from backend.utils.websocket_server import mobile_latency_data
    import socket
    import pyqrcode
    import io

    # QR Code
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
    except Exception:
        local_ip = "127.0.0.1"
    finally:
        s.close()

    port = 8501
    url = f"http://{local_ip}:{port}"

    qr = pyqrcode.create(url)
    buffer = io.BytesIO()
    qr.png(buffer, scale=6)
    buffer.seek(0)
    st.sidebar.image(buffer.getvalue(), caption=f"Scan to open:\n{url}")

    st.sidebar.caption(
        "Scan this QR code on your phone. Make sure your phone and this computer are on the same WiFi network. "
        "You may need to allow this port (default 8501) through your firewall."
    )

    # Navigation
    page = st.sidebar.radio(
        "Navigate",
        [
            "Dashboard",
            "Device State Manager",
            "Scheduling",
            "Network Monitor",
            "Device Connectivity",
            "Mobile Network Latency",
            "Automata Simulator",
            "Profile",
        ]
    )

    SUBJECT_BADGES = {
        "Dashboard": "🧩 Full Stack",
        "Device State Manager": "🧮 Automata",
        "Scheduling": "🧮 Automata + 🧩 Full Stack",
        "Network Monitor": "🌐 Networks",
        "Device Connectivity": "🌐 Networks",
        "Automata Simulator": "🧮 Automata",
        "Profile": "🧩 Full Stack + 🌐 Networks",
    }

    st.sidebar.markdown(f"**Module:** {SUBJECT_BADGES.get(page, '')}")

    return page
