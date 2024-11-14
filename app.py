import streamlit as st
import pandas as pd
import hmac


LOGO = "https://4b78e3927324ab5e61334f9a5a714ad9.cdn.bubble.io/f1727446498078x837520776516588800/logo.svg?_gl=1*1lgejkq*_gcl_au*MTMxODk4NjUyOC4xNzI2MTUzNDMx*_ga*MTQzMzAyMDg5NC4xNzA5OTIwNjY4*_ga_BFPVR2DEE2*MTcyNzQ0MTE2Mi40MS4xLjE3Mjc0NDY0ODkuNTYuMC4w"

st.logo(LOGO)
bases_cadastradas = ['São Fidélis', 'Silva Jardim']
st.session_state.status = st.session_state.get("status", "unverified")

if st.session_state.status == "unverified":
    st.image(LOGO) 
    st.title("Análise de Contas Públicas")
    municipio = st.selectbox("Escolha o munícipio a ser investigado", bases_cadastradas)

    if (municipio == bases_cadastradas[0]):
        st.session_state['df'] = pd.read_pickle('assets/df_filtrado.pkl')
    elif (municipio == bases_cadastradas[1]):
        st.session_state['df'] = pd.read_pickle('assets/df_filtradoSJ.pkl')

    # uploaded_file = st.file_uploader("Entre com a planilha do munícipio investigado:", type=["xlsx", "csv"])

    # if uploaded_file is not None:
    #     if uploaded_file.name.endswith('.csv'):
    #         df = pd.read_csv(uploaded_file)
    #     else:
    #         df = pd.read_excel(uploaded_file)
    #     st.session_state['planilha'] = df
    #     st.session_state['df'] = df_filtrado = df[~df['OBSERVACAO'].isin(['DESBLOQ.ORDEM JUDICIAL','BLOQUEIO-ORDEM JUDICIAL', 'RECEBIMENTO DE TRIBUTO MUNICIPAL (ERJ TESOURO ESTADO CONTA UNICA)'])]
    #     st.session_state['df'] = df_filtrado[~df_filtrado['NATUREZA_LANCAMENTO'].isin(['C'])]
        
    #     st.success("Planilha carregada com sucesso! Vá para a próxima página.")
    # else:
    #     st.session_state['df'] = pd.read_pickle('assets/df_filtradoSJ.pkl')
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


pg = st.navigation([st.Page("Visão_Geral.py"), st.Page("Análise_de_Destinatários.py"), st.Page("Transações_Suspeitas.py")]) # , st.Page("Chat.py")
pg.run()
