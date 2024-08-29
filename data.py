import pandas as pd
dados = r'C:\workspace\navega\planilhas\ExtratoDetalhado.xlsx'

def consulta(df, nome):
    new_df = df[df['NOME_PESSOA_OD'] == nome]
    print(new_df)
    return

df_full = pd.read_excel(dados)

df_filtrado = df_full[~df_full['OBSERVACAO'].isin(['DESBLOQ.ORDEM JUDICIAL','BLOQUEIO-ORDEM JUDICIAL'])]


df_empresas = df_filtrado[['NOME_PESSOA_OD','VALOR_TRANSACAO', 'CNAB']].dropna(subset=['NOME_PESSOA_OD']).drop_duplicates()
df_empresas_valores = df_filtrado[['NOME_PESSOA_OD', 'VALOR_TRANSACAO', 'CPF_CNPJ_OD']].dropna(subset=['NOME_PESSOA_OD'])

empresa = 'NOME_PESSOA_OD'
valor = 'VALOR_TRANSACAO'
cpf_cnpj = 'CPF_CNPJ_OD'
valores_empresas = {}

for i, row in df_empresas.iterrows():
    valores_empresas[row[empresa]] = 0
for i, row in df_empresas_valores.iterrows():
    # print(row[empresa])
    valores_empresas[row[empresa]] += row[valor]

# print(valores_empresas)

df = pd.DataFrame(list(valores_empresas.items()), columns=['Empresa', 'Valor'])
df_maiores = df.nlargest(20, 'Valor')
df_maiores_10_20 = df_maiores.iloc[10:20]

df_maiores_reset = df_maiores_10_20.reset_index(drop=True)

# print(df_empresas)

# # Salvar os dfs
#df_empresas.to_pickle(r'C:\workspace\navega\assets\df_empresa_cnab_valor.pkl')
# df_empresas_valores.to_pickle(r'C:\workspace\navega\assets\df_empresas_valores.pkl')
#df.reset_index(drop=True).to_pickle(r'C:\workspace\navega\assets\df_valor_total.pkl')
df_maiores_reset.reset_index(drop=True).to_pickle(r'C:\workspace\navega\assets\df_maiores_reset_20.pkl')

# consulta(df_empresas_valores, 'RIO  SANEAMENTO BL3 S.A.')