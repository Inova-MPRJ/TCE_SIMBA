import streamlit as st
import pandas as pd
import hmac


df_empresas = pd.read_pickle('assets/df_empresa.pkl')
df_empresas_valores = pd.read_pickle('assets/df_empresas_valores.pkl')
df_maiores = pd.read_pickle('assets/df_maiores_reset.pkl')
df_valor_total = pd.read_pickle('assets/df_valor_total.pkl')



st.session_state.status = st.session_state.get("status", "unverified")
st.title("Entre com a senha")


def check_password():
    if hmac.compare_digest(st.session_state.password, st.secrets.database.password):
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


pg = st.navigation([st.Page("page_1.py"), st.Page("page_2.py")])
pg.run()
