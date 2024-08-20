import streamlit as st
import pandas as pd

df_empresas = pd.read_pickle(r'C:\workspace\navega\assets\df_empresa.pkl')
df_empresas_valores = pd.read_pickle(r'C:\workspace\navega\assets\df_empresas_valores.pkl')
df_maiores = pd.read_pickle(r'C:\workspace\navega\assets\df_maiores_reset.pkl')
df_valor_total = pd.read_pickle(r'C:\workspace\navega\assets\df_valor_total.pkl')

# Pagina de Teste Inicial

# st.title("Estes são os dados do navega")

# st.write('Todas as empresas/pessoas que receberam:')
# st.dataframe(df_empresas)
# st.write('Todas as transações:')
# st.dataframe(df_empresas_valores)
# st.write('As empresas/pessoas que mais receberam:')
# st.dataframe(df_maiores)
# st.bar_chart(df_maiores.set_index('Empresa'))

# Pagina com filtros

def consulta(nome):
    df_valor = df_valor_total[df_valor_total['Empresa'] == nome]
    df_transacoes = df_empresas_valores[df_empresas_valores['NOME_PESSOA_OD'] == nome]
    return df_valor, df_transacoes


opcoes = df_empresas['NOME_PESSOA_OD'].unique()

escolha = st.selectbox("Escolha alguem para investigar: ", opcoes)

if escolha != None:
    df_valor, df_transacoes = consulta(escolha)
    num_linhas, _ = df_transacoes.shape

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Transações", num_linhas)

    with col2:
        st.metric("Valor Total", df_valor['Valor'])

    with col3:
        st.metric(label="Contratos Vínculados", value="")
    
    st.dataframe(df_transacoes.reset_index(drop=True))
    # Adicionar gráfico com as trasações baseada nas datas
