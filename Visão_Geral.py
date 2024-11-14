import streamlit as st
import pandas as pd
from data import empresas, maiores

# df_empresas_valores = pd.read_pickle('assets/df_empresas_valores.pkl')
# df_filtrado = pd.read_pickle('assets/df_filtrado.pkl')

orgaos_publicos = [29111093000103, 29111622000179, 11835031000189, 
                   1193480000117, 2098399000110, 42498675000152, 
                   13499878000165, 60746948000112, 28700000000000]

# Pagina de Teste Inicial

nome =  st.session_state['df']['NOME_TITULAR'].iloc[0]
st.title(f"Visão geral das Transações -{nome}")

st.write('Todas as empresas/pessoas que receberam:')
st.dataframe(empresas(st.session_state['df']))
# st.write('Todas as transações:')
# st.dataframe(df_empresas_valores) # TO DO função que retorna empresa - valor transacionado
st.write('As empresas/pessoas que mais receberam:')
df_maiores = maiores(st.session_state['df'], orgaos_publicos) 
st.dataframe(df_maiores)
st.bar_chart(df_maiores.set_index('Empresa'))