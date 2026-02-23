**Home Automation Streamlit**

A Streamlit-based home automation simulator that combines:
- Formal Language & Automata (DFA-based device transitions)
- Full Stack concepts (authentication, routing, state management)
- Computer Networks (protocol simulation, latency, WebSocket monitoring)

Features :
- Login and registration
- Device control for Light, Fan, AC, and Door
- DFA validation for all device state transitions
- Time-based scheduling rules
- Network command simulation with protocol-aware latency (MQTT, HTTP, Bluetooth)
- Network logs and latency charts
- Device online/offline connectivity simulation
- Mobile latency monitoring via WebSocket (ws://<host>:8765)
- Sidebar QR code for opening the app on mobile
- Custom DFA simulator page

Tech Stack :
- Python
- Streamlit
- Pandas
- WebSockets (websockets)
- QR generation (pyqrcode, pypng)
  
# 🚀 Quick Start

Follow these steps to run the **Home Automation Streamlit Application** locally.

## 1️⃣ Clone the Repository
```bash
git clone <your-repo-url>
cd "Home Automation Streamlit"
```

## 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
```

## 3️⃣ Activate the Virtual Environment

### Windows (PowerShell)
```bash
.\venv\Scripts\Activate.ps1
```

### macOS / Linux
```bash
source venv/bin/activate
```

## 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

## 5️⃣ Run the Application
```bash
streamlit run app.py
```

---

# 🌐 Application URL

Once the application starts, open your browser and go to:

```
http://localhost:8501
```

---

# 🔐 Demo Login

Use the following credentials to access the system:

```
Username: ullas
Password: 1234
```

⚠️ These credentials are **for demonstration purposes only**.

---

# 📄 Application Pages

## 📊 Dashboard
Provides an overview of all connected smart devices and quick control options.

## ⚙️ Device State Manager
Implements a **Deterministic Finite Automaton (DFA)** transition table to control and manage device state transitions.

## ⏰ Scheduling
Create and manage **time-based automation rules** for device control.

## 🌐 Network Monitor
Send commands to devices, inspect logs, and monitor **network latency charts**.

## 🔌 Device Connectivity
Simulate device connectivity by toggling devices **online or offline**.

## 📡 Mobile Network Latency
Displays **real-time latency data** received from the mobile client.

## 🤖 Automata Simulator
Allows users to define and test a **custom DFA** with specific input symbols and transitions.

## 👤 Profile
View account details and securely log out of the system.

---

# 🛠 Technologies Used

- Python
- Streamlit
- Plotly (for charts)
- Automata Theory (DFA simulation)
- Networking concepts
- Session-based state management

---

# 📝 Notes

- Application data is currently stored in **`st.session_state`**, meaning it uses **temporary in-memory storage**.
- **Passwords are stored as plain text** for demo purposes only.
- This project is designed as a **prototype for smart home automation and intelligent device monitoring systems**.

---

# 🔮 Future Improvements

- Database integration (PostgreSQL / MongoDB)
- Secure authentication system
- IoT device integration with Raspberry Pi
- Cloud deployment (AWS / Docker)
- Mobile app integration
- Real-time device communication via MQTT

---

# 👨‍💻 Author

**Ullas**

Engineering Student | Developer  
Interested in **Cloud Computing, AI Systems, and Full Stack Development**
For mobile access and live latency, ensure ports 8501 and 8765 are allowed through firewall.
Keep mobile device and host machine on the same Wi-Fi network.
