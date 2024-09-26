import streamlit as st
import pandas as pd
from data import consulta, transacoes_cnab, valor_data, valor_total, total_cnab, valor_ano


df = pd.read_pickle('assets/df_filtrado.pkl')
df_cnab = pd.read_pickle('assets/df_cnab_desc.pkl')

# Pagina com filtros

opcoes_empresa = df['NOME_PESSOA_OD'].unique()
opcoes_cnab = df_cnab['descricao'].unique()

escolha_empresa = st.selectbox("Escolha alguem para investigar: ", opcoes_empresa)


if escolha_empresa != None:
    df_empresa = consulta(df,escolha_empresa)
    df_transacoes = valor_data(df, escolha_empresa)

    num_linhas, _ = df_transacoes.shape

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Transações", num_linhas)

    with col2:
        st.metric("Valor Total", valor_total(df_empresa, escolha_empresa)) # Pode ser passado o df geral ou o específico 


    st.write('Evolução anual: ')
    st.bar_chart(valor_ano(df_empresa))

    escolha_cnab = st.selectbox("Escolha um tipo de transação ", opcoes_cnab)
    #st.dataframe(df_transacoes.reset_index(drop=True))
    if escolha_cnab != None:
        df_transacoes_cnab = transacoes_cnab(df, escolha_cnab, escolha_empresa) # Pode ser passado o df geral ou o específico 
        st.dataframe(df_transacoes_cnab.reset_index(drop=True))

        st.metric('Total CNAB:', total_cnab(df, escolha_empresa, escolha_cnab))
        