import streamlit as st
import pandas as pd

# Carregar o conjunto de dados
# Substitua 'malenia.csv' pelo nome do seu arquivo CSV
df = pd.read_csv('malenia.csv')

st.title("Mortes rápidas com ataque especial")

# Filtro para a fase
selected_phase = st.selectbox('Selecione a Fase:', df['Phase'].unique())

# Filtrar para os casos onde Waterflow_Death é verdadeiro e pela fase selecionada
waterflow_deaths_df = df[(df['Waterflow_Death']) & (df['Phase'] == selected_phase)]

# Adicionar a coluna Host_Build
min_deaths = waterflow_deaths_df.groupby(['Phase', 'Host_Build']).apply(lambda group: group.nsmallest(15, 'Host_Death_Time')).reset_index(drop=True)

# Ordenar pelo menor Host_Death_Time
min_deaths = min_deaths.sort_values(by='Host_Death_Time')

# Exibir o DataFrame com os menores Host_Death_Time, Host_Build e Waterflow_Death onde Waterflow_Death é verdadeiro e por fase
st.write(f"Amostras de Mortes Rápidas onde Waterflow_Death é True na Fase {selected_phase} (ordenadas por Host_Death_Time):")
st.write(min_deaths[['Phase', 'Host_Build', 'Host_Death_Time', 'Waterflow_Death']])




# Explicação sobre a análise
st.write("""
Esta análise focaliza as mortes rápidas durante o ataque especial do chefe, conhecido como Waterfowl, na fase selecionada. 
O Waterflow_Death é marcado como verdadeiro para os casos em que um jogador morreu devido a esse ataque, no caso desta análise estamos focando apenas no que está marcado.

**Fase Selecionada:** Os dados são filtrados para a fase escolhida pelo usuário, fornecendo uma visão específica do comportamento do chefe em uma determinada etapa da batalha.

**Ex:** Qual a velocidade que ela demora para usar seu ataque especial em cada fase.


Essa análise ajuda os jogadores a entenderem padrões de mortes rápidas relacionadas ao ataque especial do chefe, 
permitindo que ajustem estratégias para evitar ou lidar melhor com essas situações durante as batalhas contra Malenia.
""")
# URL do GIF de Waterfowl Dance
waterfowl_dance_gif_url = "https://eldenring.wiki.fextralife.com/file/Elden-Ring/skill-waterfowl-dance-elden-ring-wiki-480px.gif"

# Exibir o GIF na aplicação
st.image(waterfowl_dance_gif_url, caption='Waterfowl Dance - Ataque Especial (Waterfowl)', use_column_width=True)