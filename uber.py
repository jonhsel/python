import pandas as pd
import numpy as np
import streamlit as st

DATA_URL = "https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz"

@st.cache
def load_data(nrows = 1000):
    #definir a compressão e o número de linhas
    df = pd.read_csv(DATA_URL, compression="gzip", nrows=1000)

    #Renomear as colunas
    columns = {"Date/Time": "date",
               "Lat" : "lat",
               "Lon": "lon"}
    df = df.rename(columns = columns)
    df.date = pd.to_datetime(df.date)
    df = df[list(columns.values())]
    return df


#carregar dados
df = load_data(1500)

#main

#Titulo
st.title("Uber NYC")
st.success("Site: **jonhselmo.com.br**")

st.markdown(

    """
        
    ### Dashboard para análises de horários em solicitações da **Uber**
    """
)
#sidebar
st.sidebar.header("Configurações")

#Tabela de dados
if st.sidebar.checkbox("Tabela de dados"):
    st.subheader('Tabela de dados')
    st.markdown(
        f"""
        Total de amostras: {df.shape[0]}
        """
    )
    st.write(df)

#HISTOGRAMA
if st.sidebar.checkbox('Histograma'):
    st.subheader("Histograma")
    st.markdown(
        f"""
            Total de amostras: {df.shape[0]}
            """
    )
    hist = np.histogram( df.date.dt.hour, bins=24, range=(0,24))[0]
    st.bar_chart(hist)

#mapa
if st.sidebar.checkbox("Mapa"):
    st.subheader("Mapa")

    hora = st.slider("Selecione a hora", 0, 23, 12) #("string", min, max, default)
    df_filter = df[df.date.dt.hour == hora] # a selecção dos dados eh sempre dentro do DataFrame df[df.data.. >= kdkd]
    df_reg = pd.DataFrame(df_filter) #Data frame para carregar o numero de registros
    st.markdown(
        f'''
            Registros carregados: {df_reg.shape[0]} 
            '''
    )
    st.map(df_filter)

#imprimir tabela
#st.write(df)