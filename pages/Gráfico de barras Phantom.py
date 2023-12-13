import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar o conjunto de dados
# Substitua 'malenia.csv' pelo nome do seu arquivo CSV
df = pd.read_csv('malenia.csv')

st.title("Relação entre o número de Phantom ajudando o host e a média de HP tirado do chefe")

# Filtro para a fase
selected_phase = st.selectbox('Selecione a Fase:', df['Phase'].unique())

# Filtrar para a fase selecionada
filtered_df = df[df['Phase'] == selected_phase]



# Criar um gráfico de barras interativo usando o Plotly
fig = px.bar(filtered_df, x='Phantom_Count', y='Health_Pct', title=f'Média de Health_Pct por Phantom_Count na Fase {selected_phase}',
             labels={'Phantom_Count': 'Quantidade de Phantom', 'Health_Pct': 'Média de Health_Pct'})
st.plotly_chart(fig)


st.write("Disclaimer: A quantidade máxima de Phantom é 2, quem fez o estudo já contava ele mesmo como phantom, no mundo do Host só podem 4 pessoas, contando com o Host, então quando a contagem de phantom chega em 2, já bate em limite, pois já tem o phantom de quem fez o estudo e a contagem de player do Host.")

st.write("""A análise da relação entre Phantom_Count e Health_Pct fornece insights valiosos sobre o desempenho dos visitantes (phantoms) durante as batalhas contra o chefe.

Em primeiro lugar, Phantom_Count representa a quantidade de visitantes que ajudam o host durante a luta. Ao examinar como essa contagem se correlaciona com Health_Pct, a porcentagem de vida tirada do chefe pelos jogadores, podemos entender melhor o impacto coletivo da participação dos visitantes na batalha.

Um aumento em Phantom_Count pode indicar uma maior cooperação entre os jogadores, resultando em uma diminuição mais significativa na vida do chefe. Por outro lado, uma baixa contagem de visitantes pode significar um desafio maior para o host, exigindo estratégias mais cuidadosas para preservar a vida durante o confronto.

A análise dessa relação pode ser particularmente útil para entender como a dinâmica de grupo influencia o progresso na luta contra o chefe. Além disso, identificar padrões entre Phantom_Count e Health_Pct pode orientar estratégias de equipe, incentivando uma colaboração mais eficaz para alcançar melhores resultados nas batalhas.""")