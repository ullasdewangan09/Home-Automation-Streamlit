"""Data models for Home Automation System."""
from dataclasses import dataclass
from datetime import datetime, time as dtime


@dataclass
class User:
    """User account model."""
    username: str
    password: str  # NOTE: plaintext for demo only


@dataclass
class Device:
    """Smart device model."""
    name: str
    ip: str
    mac: str
    online: bool = True
    state: str = "OFF"


@dataclass
class ScheduleRule:
    """Scheduled automation rule."""
    id: int
    device: str
    at: dtime
    action: str  # e.g., "ON", "OFF", ...


@dataclass
class NetLog:
    """Network command log entry."""
    timestamp: datetime
    device: str
    action: str
    protocol: str
    status: str
    latency_ms: int
