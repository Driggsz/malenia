import streamlit as st
import pandas as pd 
import numpy as np
import seaborn as sns

df = pd.read_csv('malenia.csv')

st.title('Análise do Conjunto de Dados - Malenia')

st.write("""
Este aplicativo Streamlit fornece uma análise inicial do conjunto de dados relacionado às batalhas contra Malenia, um dos chefes mais desafiadores do jogo Elden Ring.
A seguir, apresentamos uma visão geral das colunas disponíveis e uma lista das colunas presentes no conjunto de dados.
""")

# Exibindo o DataFrame
st.subheader("Visualização do DataFrame:")
st.write(df)

# Lista de Colunas
st.subheader("Lista de Colunas:")
st.write(df.columns.tolist())

# Comentário
st.write("""
Observando o DataFrame acima, temos uma visão detalhada dos dados disponíveis, incluindo diversas métricas relacionadas às batalhas contra Malenia.
A lista de colunas fornece uma rápida referência das variáveis presentes no conjunto de dados, facilitando a identificação das informações disponíveis para análise.
Este é o ponto de partida para explorar mais a fundo as características e padrões das batalhas registradas no jogo.
""")
