import streamlit as st
import pandas as pd
from data import cheque, cheque_ano, consulta_cheque, tarifa, tarifa_banco, colunaOD_vazia, vazia_ano , df_cheque, calcula_total

df =  pd.read_pickle('assets/df_filtrado.pkl')

st.title("Transações Suspeitas")

st.write("Tarifas pagas pelo munícipio")
st.metric("Valor Total: ", tarifa(df))

st.write('Bancos que cobraram tarifas: ')
st.dataframe(tarifa_banco(df))

st.write("Transações sem destinatário explícito")
st.metric("Valor Total: ", colunaOD_vazia(df))
st.write('Por ano: ')
st.bar_chart(vazia_ano(df))

st.write("Transações realizadas por meio de cheque")
st.metric("Valor Total: ", cheque(df))

st.write('Por ano: ')
st.bar_chart(cheque_ano(df))

opcoes_cheque = df_cheque(df)['OBSERVACAO'].unique()
escolha_cheque = st.selectbox("Escolha uma observação para análisar: ", opcoes_cheque)

if escolha_cheque != None:
    df_recebedor = consulta_cheque(df,escolha_cheque)
    df_transacoes = df_recebedor[['DATA_LANCAMENTO', 'VALOR_TRANSACAO']]

    num_linhas, _ = df_transacoes.shape

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Transações", num_linhas)

    with col2:
        st.metric("Valor Total", calcula_total(df_transacoes))
