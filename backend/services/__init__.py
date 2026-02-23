"""Service layer for device control and scheduling."""
from datetime import datetime
from typing import Dict, List, Tuple
import streamlit as st
from backend.models import Device, ScheduleRule
from backend.automata import valid_transition
from backend.utils.network_sim import send_network_command


def set_device_state(
    db: Dict,
    device_name: str,
    target_state: str,
    protocol: str = "MQTT"
) -> Tuple[bool, str]:
    """
    Set a device to a target state, validating via DFA.
    Returns (success, message).
    """
    dev = db["devices"][device_name]

    if not valid_transition(device_name, dev.state, target_state):
        send_network_command(
            db, dev, f"INVALID->{target_state}", protocol
        )
        return False, f"Invalid transition: {dev.state} → {target_state} not allowed by DFA"

    log = send_network_command(db, dev, f"SET {target_state}", protocol)

    if log.status != "ACK":
        return False, f"Network error: {log.status}"

    dev.state = target_state
    return True, f"{device_name} → {target_state} (latency {log.latency_ms} ms via {protocol})"


def process_due_schedules(db: Dict, now: datetime):
    """
    Check and execute any schedule rules due at the current time.
    Ensures each rule runs only once per minute.
    """
    due: List[ScheduleRule] = []

    for rule in db["schedules"]:
        if rule.at.hour == now.hour and rule.at.minute == now.minute:
            due.append(rule)

    stamp = now.strftime("%Y-%m-%d %H:%M")

    if "last_exec" not in st.session_state:
        st.session_state.last_exec = set()

    if stamp not in st.session_state.last_exec:
        for r in due:
            set_device_state(db, r.device, r.action)
        st.session_state.last_exec.add(stamp)
