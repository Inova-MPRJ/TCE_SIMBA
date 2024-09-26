import streamlit as st
import pandas as pd
from data import empresas, maiores

df_empresas_valores = pd.read_pickle('assets/df_empresas_valores.pkl')
df_filtrado = pd.read_pickle('assets/df_filtrado.pkl')
# Pagina de Teste Inicial

st.title("Visão geral do município")

st.write('Todas as empresas/pessoas que receberam:')
st.dataframe(empresas(df_filtrado))
st.write('Todas as transações:')
st.dataframe(df_empresas_valores)
st.write('As empresas/pessoas que mais receberam:')
df_maiores = maiores(df_filtrado, 29111093000103, 29111622000179, 11835031000189, 1193480000117, 2098399000110, 42498675000152, 13499878000165, 60746948000112) 
st.dataframe(df_maiores)
st.bar_chart(df_maiores.set_index('Empresa'))