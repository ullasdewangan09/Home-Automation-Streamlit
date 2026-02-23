"""Automata Simulator page - Automata module."""
import streamlit as st
import json


def automata_simulator_page(db):
    """Automata Simulator - Automata module."""
    st.subheader("⚙️ Automata Simulator — **Automata Module**")
    st.caption("Define a small DFA and test a transition sequence.")

    with st.form("dfa_form"):
        states_csv = st.text_input("States (comma)", value="A,B,C")
        start_state = st.text_input("Start State", value="A")
        accepting_csv = st.text_input("Accepting States (comma)", value="C")
        trans_json = st.text_area(
            "Transitions JSON",
            value=json.dumps({"A": {"x": "B"}, "B": {"y": "C"}}, indent=2)
        )
        input_symbols = st.text_input("Input string (space-separated symbols)", value="x y")
        submitted = st.form_submit_button("Run")

    if submitted:
        try:
            states = [s.strip() for s in states_csv.split(',') if s.strip()]
            accepting = set([s.strip() for s in accepting_csv.split(',') if s.strip()])
            trans = json.loads(trans_json)
            tape = [s.strip() for s in input_symbols.split(' ') if s.strip()]

            cur = start_state
            trace = [cur]
            for sym in tape:
                nxt = trans.get(cur, {}).get(sym)
                if not nxt:
                    st.error(f"No transition from {cur} on '{sym}'")
                    break
                cur = nxt
                trace.append(cur)
            else:
                ok = cur in accepting
                st.success(f"Final: {cur} | Accepted: {ok}")
                st.code(" -> ".join(trace))
        except Exception as e:
            st.exception(e)
