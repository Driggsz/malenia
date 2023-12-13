import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar o conjunto de dados
# Substitua 'seu_arquivo.csv' pelo nome do seu arquivo CSV
df = pd.read_csv('malenia.csv')

# Encontrar a menor Host_Death_Time por local
min_death_time = df.groupby('Location')['Host_Death_Time'].min().reset_index()

# Criar um gráfico de barras
fig = px.bar(min_death_time, x='Location', y='Host_Death_Time',
             labels={'Location': 'Local', 'Host_Death_Time': 'Menor Tempo de Morte'},
             title='Menor Tempo de Morte por Local na Arena')

# Exibir o gráfico
st.plotly_chart(fig)


# Calcular a média de Host_Death_Time por local
avg_death_time = df.groupby('Location')['Host_Death_Time'].mean().reset_index()

# Exibir a tabela com a média de morte por local
st.write("Média de Host_Death_Time por Local:")
st.write(avg_death_time)


# Filtros
quick_death_threshold = st.slider('Limite de Tempo para Morte Rápida (segundos):', min_value=10, max_value=60, value=10)
selected_location = st.selectbox('Selecione o Local:', ['CENTER', 'INNER', 'OUTER'])

# Aplicar filtros ao DataFrame
filtered_df = df[(df['Location'] == selected_location) & (df['Host_Death_Time'] <= quick_death_threshold)]

# Exibir a tabela com os dados filtrados
st.write("Dados relacionados a mortes rápidas no local", selected_location)
st.write(filtered_df)

# Explicação detalhada sobre as observações na luta contra Malenia
st.write("""
**Análise Detalhada das Mortes Rápidas em Batalhas Contra Malenia:**

Tendo em vista que a luta contra Malenia se inicia no CENTER, podemos observar o seguinte:

- A maioria das mortes rápidas ocorre no centro da arena, indicando que jogadores que foram direto ao boss enfrentaram um risco maior. O limite mínimo de morte é de 10 segundos, e estatísticas de mortes aos 10 segundos são exclusivas do CENTER.

- Em Inner e Outer, as primeiras mortes rápidas ocorrem a partir de 11 segundos. Essa diferença de 1 segundo sugere que os jogadores que morreram mais rápido escolheram enfrentar o chefe diretamente, enquanto nas outras localizações o chefe teve que se locomover por 1 segundo adicional.

- É crucial notar que a primeira morte rápida em CENTER na primeira fase ocorre aos 12 SEGUNDOS. Isso aponta para uma postura mais agressiva de Malenia na segunda fase, o que é evidenciado pelo fato de que mortes aos 11 segundos são registradas em inner e outer na primeira fase.

Essas observações fornecem insights sobre a dinâmica da batalha, as estratégias dos jogadores e as nuances do comportamento de Malenia em diferentes fases e localizações na arena.
""")



st.title("Mortes mais rápidas na 1° fase do chefe")

# Filtro para Phase 1
df_phase1 = df[df['Phase'] == 1]

# Encontrar o menor Host_Death_Time em cada localização
min_deaths = df_phase1.groupby('Location')['Host_Death_Time'].min().reset_index()

# Exibir o DataFrame com os menores Host_Death_Time em cada localização
st.write(min_deaths)

st.write(""" 
         - Aqui fica comprovado que apesar da morte mais rápida ter 10 segundos e ela ter ocorrido em Center, as mortes mais rápidas de FATO ocorreram em INNER e OUTER
        
         - O Timer reseta quando você sai da primeira para a segunda fase, contando novamente do 0
         
         - Então na verdade talvez por medo ou excesso de cautela, esperaram com que o boss se aproximasse
        
         - Essas mortes foram as mais rápidas de fato, pois pra chegar na segunda fase do boss, precisa passar da primeira fase
         """)

st.title("Gráfico Pizza para mortes por local seja por porcentagem de HP ou por tempo de morte do Host")

# Escolha da métrica (Host_Death_Time ou Health_Pct)
metric_choice = st.radio("Escolha a métrica para o gráfico de pizza:", ['Host_Death_Time', 'Health_Pct'])

# Criar gráfico de pizza
fig = px.pie(df, names='Location', values=metric_choice, title=f'Distribuição de {metric_choice} por Localização')

# Exibir o gráfico
st.plotly_chart(fig)


# Título para a seção de gráfico de pizza
st.title("Distribuição das mortes por métricas HP restante e Local da morte")

# Explicação sobre o gráfico de pizza
st.write("""
O gráfico de pizza acima apresenta a distribuição de mortes em relação à localização, considerando duas métricas distintas: 
tempo de morte do host (Host_Death_Time) ou porcentagem de saúde retirada do chefe (Health_Pct).

**Como Interpretar o Gráfico:**
- Cada fatia do gráfico representa uma localização específica onde as batalhas ocorreram.


**Observações Importantes:**
- Se a métrica escolhida for o tempo de morte do host, a fatia maior indica a localização onde as mortes ocorreram mais rapidamente.
- Se a métrica escolhida for a porcentagem de saúde retirada, a fatia maior indica a localização onde o chefe foi mais efetivo em causar dano.

**Como Pode Ser Útil:**
- **Identificação de Pontos Críticos:** Permite identificar localizações críticas onde as mortes ocorrem mais frequentemente ou onde o chefe é mais letal.
- **Avaliação de Estratégias:** Ajuda os jogadores a ajustar estratégias com base na análise das mortes em diferentes localizações.
- **Foco em Melhorias:** Facilita a identificação de áreas que exigem melhorias para aumentar a sobrevivência do host ou otimizar o dano causado ao chefe.

Esse gráfico fornece uma visão visual e comparativa das mortes em diferentes localizações, destacando áreas de desafio e oportunidade nas batalhas contra Malenia.
""")