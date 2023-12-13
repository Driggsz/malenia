import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar o conjunto de dados
# Substitua 'seu_arquivo.csv' pelo nome do seu arquivo CSV
df = pd.read_csv('malenia.csv')

# Sidebar para seleção de filtros
st.sidebar.header('Filtros')
selected_location = st.sidebar.selectbox('Selecione a Location:', df['Location'].unique())
selected_phase = st.sidebar.selectbox('Selecione a Phase:', df['Phase'].unique())
selected_waterflow_death = st.sidebar.selectbox('Selecione a Waterflow_Death:', df['Waterflow_Death'].unique())

# Aplicar filtros ao DataFrame
filtered_df = df[(df['Location'] == selected_location) & 
                 (df['Phase'] == selected_phase) & 
                 (df['Waterflow_Death'] == selected_waterflow_death)]

# Calcular média de tempo que o host sobreviveu e a média da porcentagem de saúde do chefe tirado
avg_time_survived = filtered_df.groupby('Host_Build')['Host_Death_Time'].mean()
avg_health_pct = filtered_df.groupby('Host_Build')['Health_Pct'].mean()

# Criar um gráfico interativo usando plotly express
fig = px.line(x=avg_time_survived.index, y=avg_time_survived, labels={'x': 'Tipo de Build do Host', 'y': 'Tempo Médio de Sobrevivência'},
              title='Média de Tempo de Sobrevivência por Tipo de Build do Host')

# Adicionar linha de média de saúde do chefe tirado
fig.add_scatter(x=avg_health_pct.index, y=avg_health_pct, mode='lines', name='Média de HP tirado do chefe', yaxis='y2')

# Adicionar eixo secundário para a média de saúde do chefe tirado
fig.update_layout(yaxis2=dict(title='Média de HP tirado do chefe', overlaying='y', side='right'))

# Exibir o gráfico
st.plotly_chart(fig)


# Título para a seção de gráficos
st.subheader("Análise Gráfica: Média de Tempo de Sobrevivência e Saúde do Chefe por Tipo de Build")

# Explicação sobre o gráfico
st.write("""
O gráfico interativo acima apresenta a média de tempo de sobrevivência do host e a média da porcentagem de HP restante no chefe no momento da morte, 
segmentadas pelo tipo de build adotado durante as batalhas contra Malenia em Elden Ring.

**Como Interpretar o Gráfico:**
- O eixo x representa os diferentes tipos de build do chefe, indicando a média de porcentagem de saúde restante no chefe.
- A linha azul clara representa a média de tempo de sobrevivência (em segundos) do host para cada tipo de build.
- A linha azul escura simboliza a média da porcentagem de HP do chefe que o restava no momento da morte do host, agrupadas por tipo de build do host.

**Observações Importantes:**
- Tipos de build do chefe com maior porcentagem de HP restante indicam maior resistência ou dificuldade da batalha.
- A média de tempo de sobrevivência do host fornece insights sobre a durabilidade e eficácia defensiva de diferentes builds do host.
- A análise conjunta dessas métricas ajuda a identificar tendências e otimizar estratégias para enfrentar Malenia.

Esse gráfico fornece uma visão visual e comparativa das diferentes abordagens dos jogadores, auxiliando na tomada de decisões informadas para melhorar o desempenho nas batalhas.
""")