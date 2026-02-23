"""Automata DFA definitions and validation."""
from typing import Dict, Set


DEVICE_DFA: Dict[str, Dict[str, Set[str]]] = {
    "Light": {
        "OFF": {"DIM", "ON"},
        "DIM": {"OFF", "ON"},
        "ON": {"DIM", "OFF"},
    },
    "Fan": {
        "OFF": {"LOW"},
        "LOW": {"OFF", "MEDIUM"},
        "MEDIUM": {"LOW", "HIGH"},
        "HIGH": {"MEDIUM"},
    },
    "AC": {
        "OFF": {"COOL", "HEAT"},
        "COOL": {"OFF", "HEAT"},
        "HEAT": {"OFF", "COOL"},
    },
    "Door": {
        "LOCKED": {"UNLOCKED"},
        "UNLOCKED": {"LOCKED"},
    }
}


def valid_transition(device: str, current: str, target: str) -> bool:
    """Check if a state transition is valid per the DFA."""
    if device not in DEVICE_DFA:
        return False
    table = DEVICE_DFA[device]
    if current not in table:
        return False
    return target in table[current]
