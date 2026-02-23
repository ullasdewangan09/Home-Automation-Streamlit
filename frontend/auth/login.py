"""Login view for user authentication."""
import streamlit as st


def login_view(db):
    """User login form."""
    st.markdown("### 🔐 Login")
    with st.form("login_form"):
        u = st.text_input("Username", value="ullas")
        p = st.text_input("Password", type="password", value="1234")
        submitted = st.form_submit_button("Login")

    if submitted:
        user = db["users"].get(u)
        if user and user.password == p:
            st.session_state.user = u
            st.success("Logged in!")
            st.rerun()
        else:
            st.error("Invalid credentials")
