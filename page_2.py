import streamlit as st
import pandas as pd


df_empresas = pd.read_pickle('assets/df_empresa.pkl')
df_empresas_valores = pd.read_pickle('assets/df_empresas_valores.pkl')
df_valor_total = pd.read_pickle('assets/df_valor_total.pkl')
df_empresa_cnab = pd.read_pickle('assets/df_empresa_cnab.pkl')
df_cnab = pd.read_pickle('assets/df_cnab.pkl')
df_empresa_cnab_valor = pd.read_pickle('assets/df_empresa_cnab_valor.pkl')

# Pagina com filtros

def consulta(nome):
    df_valor = df_valor_total[df_valor_total['Empresa'] == nome]
    df_transacoes = df_empresas_valores[df_empresas_valores['NOME_PESSOA_OD'] == nome]
    return df_valor, df_transacoes

def consulta_cnab(cnab, nome):

    df_1 = df_empresa_cnab_valor[df_empresa_cnab_valor['CNAB'] == cnab]
    df_transacao = df_1[df_1['NOME_PESSOA_OD'] == nome].drop('NOME_PESSOA_OD', axis=1)

    return df_transacao


opcoes_empresa = df_empresas['NOME_PESSOA_OD'].unique()
opcoes_cnab = df_cnab['CNAB'].unique()

escolha_empresa = st.selectbox("Escolha alguem para investigar: ", opcoes_empresa)

escolha_cnab = st.selectbox("Escolha um tipo de transação ", opcoes_cnab)

if escolha_empresa != None:
    df_valor, df_transacoes = consulta(escolha_empresa)
    num_linhas, _ = df_transacoes.shape

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Transações", num_linhas)

    with col2:
        st.metric("Valor Total", df_valor['Valor'])

    with col3:
        st.metric(label="Contratos Vínculados", value="")
    
    #st.dataframe(df_transacoes.reset_index(drop=True))
    if escolha_cnab != None:
        df_transacoes_cnab = consulta_cnab(escolha_cnab, escolha_empresa)
        st.dataframe(df_transacoes_cnab.reset_index(drop=True))
        # Adicionar gráfico com as trasações baseada nas datas