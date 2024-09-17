import pandas as pd

# Retorna um dataframe com todas as infos da empresa passada
def consulta(df, nome):
    new_df = df[df['NOME_PESSOA_OD'] == nome]
    return new_df

# Lista de contas públicas presentes
def empresas(df):
    df_empresas = df[['NOME_PESSOA_OD']].dropna(subset=['NOME_PESSOA_OD']) 
    return df_empresas

# Retorna as maiores transações
def maiores(df, *args):  
    cnpjs = []

    for arg in args:
        cnpjs.append(arg)

    # df['CPF_CNPJ_OD'] = df['CPF_CNPJ_OD'].astype(str)
    df_maiores = df[['NOME_PESSOA_OD','VALOR_TRANSACAO', 'CPF_CNPJ_OD']]

    # Filtra CNPJs/CPFs que não devem ser exibidos
    df_maiores_filtrado = df_maiores[~df_maiores['CPF_CNPJ_OD'].isin(cnpjs)]
    # print(df_maiores_filtrado)

    # Cria uma lista para somar os valores através de For
    empresa = 'NOME_PESSOA_OD'
    valor = 'VALOR_TRANSACAO'
    valores_empresas = {}

    for i, row in df_maiores_filtrado.iterrows():
        valores_empresas[row[empresa]] = 0
    for i, row in df_maiores_filtrado.iterrows():
        # print(row[empresa])
        valores_empresas[row[empresa]] += row[valor]

    # print(valores_empresas)


    df_f = pd.DataFrame(list(valores_empresas.items()), columns=['Empresa', 'Valor'])
    df_f = df_f.nlargest(10, 'Valor')

    print(df_f)
    
    return df_f

# Retorna um dataframe com as transações de um determinado CNAB de uma empresa
def transacoes_cnab(df, cnab, nome):
    df_empresas = df[['NOME_PESSOA_OD', 'VALOR_TRANSACAO', 'CNAB']]

    df_1 = df_empresas[df_empresas['CNAB'] == int(cnab[:3])]
    df_transacao = df_1[df_1['NOME_PESSOA_OD'] == nome].drop('NOME_PESSOA_OD', axis=1)
    
    return df_transacao

# Valor por CNAB
def valor_cnab(df):
    df_empresas = df[['NOME_PESSOA_OD', 'VALOR_TRANSACAO', 'CPF_CNPJ_OD', 'CNAB']]


    empresa = 'NOME_PESSOA_OD'
    valor = 'VALOR_TRANSACAO'
    cnab = 'CNAB'
    valores_empresas = {}


    for i, row in df_empresas.iterrows():
        nome_empresa = row[empresa]
        cnab_atual = row[cnab]
        valor_atual = row[valor]
        
        if nome_empresa not in valores_empresas:
            valores_empresas[nome_empresa] = []


        cnab_encontrado = False
        for item in valores_empresas[nome_empresa]:
            if item[0] == cnab_atual:
                item[1] += valor_atual  
                cnab_encontrado = True
                break
        
        if not cnab_encontrado:
            valores_empresas[nome_empresa].append([cnab_atual, valor_atual])

    return valores_empresas

# Retorna o valor total do CNAB escolhido
def total_cnab(df, empresa, cnab):
    valores_empresas = valor_cnab(df)
    for ind in valores_empresas[empresa]:
        if (ind[0] == int(cnab[:3])):
            break
    return ind[1]


# Gera um dataframe com as datas e valores recebidos pela pessoa/empresa
def valor_data(df, empresa):
    df_filtrado = df[df['NOME_PESSOA_OD'].isin([empresa])]
    df_valor_data = df_filtrado[['DATA_LANCAMENTO', 'VALOR_TRANSACAO']]
    
    return df_valor_data

# Soma todos os valores recebidos pela pessoa/empresa (Retorna um Inteiro)
def valor_total(df, empresa):
    df_filtrado = df[df['NOME_PESSOA_OD'].isin([empresa])] 
    valor = 0

    for i, row in df_filtrado.iterrows():
        valor += row['VALOR_TRANSACAO']

    return valor