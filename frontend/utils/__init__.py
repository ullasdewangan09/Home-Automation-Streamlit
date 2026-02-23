"""Frontend utilities and styling."""

# Color scheme
COLORS = {
    "primary": "#FF6B6B",
    "secondary": "#4ECDC4",
    "success": "#95E1D3",
    "warning": "#FFE66D",
    "danger": "#FF6B6B",
    "info": "#74B9FF",
    "light": "#F5F5F5",
    "dark": "#2D3436",
}

# Custom CSS
CUSTOM_CSS = """
<style>
    .device-card {
        border: 2px solid #E0E0E0;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 12px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    .status-badge {
        display: inline-block;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: bold;
    }
    
    .status-online {
        background-color: #95E1D3;
        color: #2D3436;
    }
    
    .status-offline {
        background-color: #FFB6B6;
        color: #2D3436;
    }
</style>
"""


def apply_custom_css():
    """Apply custom CSS to the page."""
    import streamlit as st
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


def format_device_status(device):
    """Format device status for display."""
    status = "🟢 Online" if device.online else "🔴 Offline"
    return f"{status} | {device.state}"


def format_timestamp(dt):
    """Format datetime for display."""
    return dt.strftime("%H:%M:%S") if dt else "N/A"
