"""Scheduling page - Automata + Full Stack module."""
import streamlit as st
from backend.models import ScheduleRule
from backend.automata import DEVICE_DFA
from backend.services import set_device_state


def scheduling_page(db):
    """Scheduling - Automata + Full Stack module."""
    st.subheader("⏰ Scheduling — **Automata + Full Stack Module**")

    c1, c2 = st.columns(2)
    with c1:
        dev_name = st.selectbox("Device", list(db["devices"].keys()))
        allowed = set(DEVICE_DFA.get(dev_name, {}).keys())
        for s in DEVICE_DFA.get(dev_name, {}).values():
            allowed.update(s)
        action = st.selectbox("Action (state to set)", sorted(list(allowed)))
    with c2:
        at = st.time_input("Time (24h)")

    if st.button("Add Rule"):
        rid = db["next_rule_id"]
        db["next_rule_id"] += 1
        db["schedules"].append(ScheduleRule(id=rid, device=dev_name, at=at, action=action))
        st.success(f"Rule #{rid} added: IF time=={at.strftime('%H:%M')} THEN {dev_name}→{action}")

    if db["schedules"]:
        st.markdown("### Existing Rules (Grammar-like)")
        for r in db["schedules"]:
            st.code(f"IF time == {r.at.strftime('%H:%M')} THEN set {r.device} -> {r.action}")
        if st.button("Clear All Rules"):
            db["schedules"] = []
            st.success("All rules cleared")

    st.caption("Engine checks rules every minute and applies matching transitions (valid by DFA only).")
