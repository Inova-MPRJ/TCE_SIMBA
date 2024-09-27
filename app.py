import streamlit as st
import pandas as pd
import hmac


LOGO = "https://4b78e3927324ab5e61334f9a5a714ad9.cdn.bubble.io/f1727446498078x837520776516588800/logo.svg?_gl=1*1lgejkq*_gcl_au*MTMxODk4NjUyOC4xNzI2MTUzNDMx*_ga*MTQzMzAyMDg5NC4xNzA5OTIwNjY4*_ga_BFPVR2DEE2*MTcyNzQ0MTE2Mi40MS4xLjE3Mjc0NDY0ODkuNTYuMC4w"

st.logo(LOGO)

st.session_state.status = st.session_state.get("status", "unverified")
if st.session_state.status == "unverified":
    st.image(LOGO) 
    st.title("Análise de Contas Públicas")


def check_password():
    if hmac.compare_digest(st.session_state.password, st.secrets.database.password): # Produção
    # if st.session_state.password == "senha":  # Sandbox
        st.session_state.status = "verified"
    else:
        st.session_state.status = "incorrect"
    st.session_state.password = ""

def login_prompt():
    st.text_input("Enter password:", key="password", on_change=check_password)
    if st.session_state.status == "incorrect":
        st.warning("Incorrect password. Please try again.")

def logout():
    st.session_state.status = "unverified"

def welcome():
    st.success("Login successful.")
    st.button("Log out", on_click=logout)


if st.session_state.status != "verified":
    login_prompt()
    st.stop()
welcome()


pg = st.navigation([st.Page("Visão_Geral.py"), st.Page("Análise_de_Destinatários.py"), st.Page("Transações_Suspeitas.py")])
pg.run()
