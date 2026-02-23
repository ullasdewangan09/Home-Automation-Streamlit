"""Pages module."""
from .dashboard import dashboard_page
from .device_manager import device_state_manager_page
from .scheduling import scheduling_page
from .network_monitor import network_monitor_page
from .device_connectivity import device_connectivity_page
from .mobile_latency import mobile_latency_page
from .automata_simulator import automata_simulator_page
from .profile import profile_page

__all__ = [
    "dashboard_page",
    "device_state_manager_page",
    "scheduling_page",
    "network_monitor_page",
    "device_connectivity_page",
    "mobile_latency_page",
    "automata_simulator_page",
    "profile_page",
]
