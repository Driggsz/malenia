import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
import sweetviz as sv



df = pd.read_csv('malenia.csv')


st.title('Análise do CSV de Mortes para o chefe de Elden Ring - Malenia')

# URL do seu GIF
gif_url = "https://64.media.tumblr.com/ceb16120b9a3d1581cfccec53840b47d/9f4f365ded9ad133-3f/s540x810/d3afb216c5d1198194a5b92a7e597ef1335415ca.gifv"

# Exibe o GIF na página inicial
st.image(gif_url, use_column_width=True)

st.markdown("""
    <style>
        .title {
            font-size: 36px;
            font-weight: bold;
            font-style: italic;
            color: rgba(255, 255, 255, 0.7);
            background-color: rgba(0, 0, 0, 0);
            padding: 10px;
            margin-bottom: 20px;
        }
    </style>
    <div class="title"> "Tarnished, are we?" - White Mask Varre </div>
""", unsafe_allow_html=True)

# Apresentação do estudo
st.title("Estudo analítico de Dados: Batalhas contra Malenia")

st.write("""
Este estudo analisa dados relacionados à batalha contra Malenia, um chefe em um jogo, com foco em várias métricas significativas.
O conjunto de dados fornece informações detalhadas sobre cada encontro, permitindo uma compreensão mais profunda da dinâmica das batalhas.
""")

# Apresentação das principais colunas e métricas
st.subheader("Principais Colunas e Métricas:")
st.write("""
- **Host_Death_Time:** Indica o tempo que o anfitrião (host) sobreviveu durante a batalha.
- **Level:** Representa o nível do jogador durante o encontro.
- **Host_Build:** Descreve o tipo de construção (RAW_MELEE, HYBRID, RAW_CAST, PROC_CAST, PROC_MELEE) adotada pelo host.
- **Phase:** Indica a fase específica da batalha contra Malenia.
- **Waterflow_Death:** Booleano indicando se o jogador morreu devido ao ataque especial de Malenia chamado Waterflow.
- **Health_Pct:** Porcentagem da vida do chefe retirada durante o encontro.
- **Location:** Refere-se à localização específica da batalha (INNER, CENTER, OUTER).
- **Phantom_Count:** Representa a quantidade de visitantes que ajudam o host durante a luta.
""")

# Apresentação das principais análises realizadas
st.subheader("Principais Análises Realizadas:")
st.write("""
- **Filtros e Agrupamentos:** Implementação de filtros para Location, Phase e Waterflow_Death, permitindo uma análise segmentada dos dados.
- **Gráficos de Linha e Média:** Criação de gráficos de linha para a média de tempo de sobrevivência do host, considerando a variável Host_Death_Time e a linha de média de sangue retirado do chefe usando Health_Pct.
- **Gráficos de Pizza e Análise de Mortes Rápidas:** Utilização de gráficos de pizza para visualizar a distribuição de mortes por localização e análise detalhada das mortes rápidas em relação à localização.
- **Análise Estatística por Localização:** Avaliação das mortes rápidas em cada localização (INNER, CENTER, OUTER) e comparação estatística.
- **Filtros Adicionais e Comentários:** Implementação de filtros opcionais para o tipo de construção (Host_Build) e inclusão de comentários para contextualizar os resultados.
- **Correlação entre Variáveis:** Análise da correlação entre variáveis, incluindo a matriz de correlação entre Host_Death_Time e Waterflow_Death.
- **Análise de Phantom_Count e Health_Pct:** Exploração da relação entre a contagem de visitantes (Phantom_Count) e a média de porcentagem de vida retirada do chefe (Health_Pct).
""")

# Considerações Finais
st.subheader("Considerações Finais:")
st.write("""
Este estudo fornece uma visão abrangente da batalha contra Malenia, destacando padrões, correlações e tendências significativas.
A análise detalhada das diferentes métricas permite uma compreensão mais completa das estratégias eficazes, desafios enfrentados e o impacto da colaboração entre os jogadores nas batalhas.
""")


