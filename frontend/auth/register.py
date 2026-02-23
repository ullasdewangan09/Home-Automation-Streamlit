"""Register view for new user accounts."""
import streamlit as st
from backend.models import User


def register_view(db):
    """User registration form."""
    st.markdown("### 🧾 Register")
    with st.form("register_form"):
        u = st.text_input("Username")
        p1 = st.text_input("Password", type="password")
        p2 = st.text_input("Confirm Password", type="password")
        submitted = st.form_submit_button("Create Account")

    if submitted:
        if not u or not p1:
            st.error("Username and password required")
            return
        if p1 != p2:
            st.error("Passwords do not match")
            return
        if u in db["users"]:
            st.error("User already exists")
            return
        db["users"][u] = User(username=u, password=p1)
        st.success("Account created. Please login.")
