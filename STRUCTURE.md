# 🏠 Home Automation System - Project Structure

## Directory Layout

```
Home Automation Streamlit/
├── app.py                          # Main entry point (refactored orchestrator)
├── requirements.txt                # Python dependencies
│
├── backend/                        # Business logic & data management
│   ├── models/
│   │   └── __init__.py             # Data models (User, Device, ScheduleRule, NetLog)
│   ├── automata/
│   │   └── __init__.py             # DFA definitions (DEVICE_DFA, valid_transition)
│   ├── services/
│   │   └── __init__.py             # Core services (set_device_state, process_due_schedules)
│   └── utils/
│       ├── websocket_server.py     # Real-time mobile WebSocket server
│       └── network_sim.py          # Network command simulation & latency
│
└── frontend/                       # User interface & components
    ├── auth/
    │   ├── __init__.py             # Auth module exports
    │   ├── login.py                # Login form (login_view)
    │   └── register.py             # Registration form (register_view)
    │
    ├── pages/
    │   ├── __init__.py             # Pages module exports
    │   ├── dashboard.py            # Device overview & quick controls
    │   ├── device_manager.py       # State manager with DFA validation
    │   ├── scheduling.py           # Time-based automation rules
    │   ├── network_monitor.py      # Latency simulation & charts
    │   ├── device_connectivity.py  # Online/offline status management
    │   ├── mobile_latency.py       # Real-time WebSocket latency
    │   ├── automata_simulator.py   # Custom DFA tester
    │   └── profile.py              # User profile & logout
    │
    ├── components/
    │   ├── __init__.py             # Components module exports
    │   ├── device_card.py          # Reusable device card with controls
    │   ├── network_chart.py        # Network latency visualization
    │   └── sidebar.py              # Navigation & QR code display
    │
    └── utils/
        └── __init__.py             # Styling & utility functions
```

## Key Architecture Decisions

### ✅ Separation of Concerns
- **Backend**: Business logic, data models, DFA automata, network simulation
- **Frontend**: UI components, page structures, user interaction
- **Components**: Reusable UI building blocks
- **Utils**: Styling and helper functions

### ✅ Modular Page Structure
Each page module follows consistent pattern:
```python
def page_name_page(db):
    """Page implementation."""
    st.subheader("Page Title")
    # UI logic here
```

### ✅ Import Hierarchy
```
app.py
├─ backend.models (data structures)
├─ backend.automata (DFA validation)
├─ backend.services (business logic)
├─ backend.utils (networking, WebSocket)
│
├─ frontend.auth.login (login_view)
├─ frontend.auth.register (register_view)
├─ frontend.pages.* (8 page modules)
└─ frontend.components.sidebar (navigation)
```

## Running the Application

```bash
# Start the Streamlit app
streamlit run app.py

# The app will:
# 1. Show login/register tabs if not authenticated
# 2. Generate QR code for mobile access (same WiFi)
# 3. Provide sidebar navigation to 8 pages
# 4. Run WebSocket server in background (port 8765)
```

## Module Responsibilities

### Backend Modules
| Module | Purpose | Key Functions |
|--------|---------|---|
| `models` | Data definitions | User, Device, ScheduleRule, NetLog |
| `automata` | DFA logic | DEVICE_DFA dict, valid_transition() |
| `services` | Business logic | set_device_state(), process_due_schedules() |
| `utils.websocket_server` | Real-time updates | WebSocket handler, mobile_latency_data list |
| `utils.network_sim` | Network sim | send_network_command(), latency calculation |

### Frontend Modules
| Module | Type | Pages |
|--------|------|-------|
| `auth` | Auth | login, register |
| `pages` | Pages | dashboard, device_manager, scheduling, network_monitor, device_connectivity, mobile_latency, automata_simulator, profile |
| `components` | Components | device_card, network_chart, sidebar |
| `utils` | Helpers | COLORS dict, custom CSS, format_* functions |

## Session State Management

```python
st.session_state.db = {
    "users": {username: User},
    "devices": {device_name: Device},
    "schedules": [ScheduleRule, ...],
    "netlogs": [NetLog, ...],
    "next_rule_id": int
}
st.session_state.user = username  # After login
```

## Subjects Coverage

🧮 **Formal Language & Automata**
- Deterministic Finite Automata (DFA) for device state transitions
- Valid transition validation across all device state changes
- Automata Simulator page for custom DFA testing

🧩 **Full Stack Development**
- Frontend: Streamlit UI components, multi-page navigation
- Backend: Python business logic, session management, data models
- Database: In-memory session state (expandable to persistent DB)

🌐 **Computer Networks**
- Network protocol simulation (MQTT, HTTP, Bluetooth)
- Latency calculation based on protocol type
- WebSocket server for real-time mobile network monitoring
- Network command logging and visualization

---

**Last Updated:** Refactor Complete  
**Status:** Ready for Testing  
**To Run:** `streamlit run app.py`
