# -*- coding: utf-8 -*-

import pandas as pd


#ENTRADA NDO ARQUIVO
entrada = input("Digite nome do arquivo.csv: ")

#APLICAÇÃO DAS EXTENSÕES
print(entrada)
nomeArquivocsv = entrada+'.csv'

#AJUSTE DA TABELA

print(nomeArquivocsv)
print("tabela sendo ajustada. Separando ord e data")
df = pd.read_csv(nomeArquivocsv)
df_drop = df['ORD DATA']
lista = []
for item in df_drop:
    aux = str(item)
    lista.append(aux[3:])
#print(lista)
print ("Tabela separada e limpa")
df['ORD DATA'] = pd.DataFrame(lista)
#df['ORD DATA'] = pd.to_datetime(df['ORD DATA'])
print("salvando novo arquivo")
#print(df.columns)
df_final = df[['VÍTIMA (S)','ORD DATA','ID', 'HORA', 'ARMA', 'BAIRRO/FATO','MUNICÍPIO/FATO', 'Unnamed: 7']]
df_final.to_csv(entrada+"final.csv", encoding='utf-8', index=False)

#['ORD DATA', 'HORA', 'VÍTIMA (S)', 'ID', 'ARMA', 'BAIRRO/FATO','MUNICÍPIO/FATO', 'Unnamed: 7'],

