"""Profile page - user account and settings."""
import streamlit as st


def profile_page(db):
    """Profile - user account and settings."""
    st.subheader("👤 Profile — **Full Stack + Networks**")
    st.write(f"Logged in as **{st.session_state.user}**")
    if st.button("Log out"):
        del st.session_state.user
        st.success("Logged out")
        st.rerun()
