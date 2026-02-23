"""Network simulation and command logging."""
import random
from datetime import datetime
from typing import Dict
from backend.models import Device, NetLog


def send_network_command(
    db: Dict,
    device: Device,
    action: str,
    protocol: str = "MQTT",
    source: str = "WebUI"
) -> NetLog:
    """
    Simulate sending a network command to a device.
    Records latency based on protocol type and jitter.
    """
    if protocol == "Bluetooth":
        base = 20  # Bluetooth lower latency base
        jitter = random.randint(0, 20)  # smaller jitter
    elif protocol == "MQTT":
        base = 40
        jitter = random.randint(0, 60)
    else:  # HTTP or others
        base = 80
        jitter = random.randint(0, 60)

    latency = base + jitter
    status = "ACK" if device.online else "NO LINK"

    log = NetLog(
        timestamp=datetime.now(),
        device=device.name,
        action=action,
        protocol=protocol,
        status=status,
        latency_ms=latency,
    )

    db["netlogs"].append(log)
    if len(db["netlogs"]) > 400:
        db["netlogs"] = db["netlogs"][-400:]

    return log
