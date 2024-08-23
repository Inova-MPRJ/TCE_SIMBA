import streamlit as st
import pandas as pd

df_empresas = pd.read_pickle(r'C:\workspace\navega\assets\df_empresa.pkl')
df_empresas_valores = pd.read_pickle(r'C:\workspace\navega\assets\df_empresas_valores.pkl')
df_maiores = pd.read_pickle(r'C:\workspace\navega\assets\df_maiores_reset.pkl')

# Pagina de Teste Inicial

st.title("Estes são os dados do navega")

st.write('Todas as empresas/pessoas que receberam:')
st.dataframe(df_empresas)
st.write('Todas as transações:')
st.dataframe(df_empresas_valores)
st.write('As empresas/pessoas que mais receberam:')
st.dataframe(df_maiores)
st.bar_chart(df_maiores.set_index('Empresa'))