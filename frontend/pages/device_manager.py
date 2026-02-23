"""Device State Manager page - Automata module."""
import streamlit as st
from backend.automata import DEVICE_DFA
from backend.services import set_device_state


def device_state_manager_page(db):
    """Device State Manager - Automata module."""
    st.subheader("🔄 Device State Manager — **Automata Module**")
    dev_name = st.selectbox("Select Device", list(db["devices"].keys()))

    st.markdown("**Valid transitions (DFA):**")
    for s, nxt in DEVICE_DFA.get(dev_name, {}).items():
        st.markdown(f"- `{s}` → {sorted(list(nxt))}")

    possible_states = list(DEVICE_DFA.get(dev_name, {}).keys())
    target = st.selectbox("Target State", possible_states)

    if st.button("Apply Transition"):
        ok, msg = set_device_state(db, dev_name, target)
        if ok:
            st.success(msg)
        else:
            st.error(msg)

    st.info(f"Current: {db['devices'][dev_name].state}")
