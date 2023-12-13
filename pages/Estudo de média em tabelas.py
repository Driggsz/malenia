import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar o conjunto de dados
df = pd.read_csv('malenia.csv')

# Sidebar para seleção de filtros
st.sidebar.header('Filtros')

# Seleção da Localização
selected_location = st.sidebar.selectbox('Selecione a Location:', df['Location'].unique())

# Seleção da Fase
selected_phase = st.sidebar.selectbox('Selecione a Phase:', df['Phase'].unique())

# Seleção de Waterflow_Death
selected_waterflow_death = st.sidebar.selectbox('Selecione a Waterflow_Death:', df['Waterflow_Death'].unique())

# Filtro opcional para o tipo de build
build_options = ['RAW_MELEE', 'HYBRID', 'RAW_CAST', 'PROC_CAST', 'PROC_MELEE', 'Todas']
selected_build = st.sidebar.selectbox('Selecione o Tipo de Build (opcional):', build_options)


# Aplicar filtros ao DataFrame
filtered_df = df[(df['Location'] == selected_location) & 
                 (df['Phase'] == selected_phase) & 
                 (df['Waterflow_Death'] == selected_waterflow_death)]

# Aplicar filtro opcional para o tipo de build
if selected_build != 'Todas':
    filtered_df = filtered_df[filtered_df['Host_Build'] == selected_build]

# Título dos dados após os filtros
st.subheader("Dados após os Filtros")

# Exibir DataFrame filtrado
st.dataframe(filtered_df)

# Título da seção de Análise
st.subheader("Análise Estatística")

# Calcular média de tempo que o host sobreviveu e a média da porcentagem de saúde do chefe tirado
avg_time_survived = filtered_df.groupby('Host_Build')['Host_Death_Time'].mean()
avg_health_pct = filtered_df.groupby('Host_Build')['Health_Pct'].mean()

# Apresentar média de tempo que o host sobreviveu
st.write("Média de Tempo que o Host Sobreviveu:")
st.write(avg_time_survived)

# Apresentar média de saúde do chefe tirado
st.write("Média de Saúde do Chefe Tirado:")
st.write(avg_health_pct)



# Título para a seção de justificativa
st.subheader("Por que isso pode ser útil?")

# Explicação
st.write("""

1. **Filtros Personalizados:** Os usuários podem selecionar a localização, fase e a ocorrência de mortes por Waterflow, adaptando a análise às circunstâncias específicas da batalha.

2. **Comparação de Tipos de Build:** A opção de filtrar por tipo de build possibilita a comparação entre diferentes estratégias adotadas pelos jogadores, avaliando sua eficácia em termos de tempo de sobrevivência e dano causado ao chefe.

3. **Análise Estatística:** A apresentação das médias de tempo de sobrevivência do host e porcentagem de saúde do chefe tirado oferece insights valiosos sobre a performance média dos jogadores em diferentes cenários de batalha.

4. **Tomada de Decisões Informada:** Os jogadores podem utilizar essa ferramenta para tomar decisões mais informadas sobre suas estratégias, baseando-se em padrões e tendências extraídos dos dados disponíveis.

5. **Exploração Interativa:** A interface gráfica permite uma exploração dinâmica dos dados, tornando a análise mais intuitiva e acessível para diferentes usuários, independentemente do nível de familiaridade com análise de dados.

6. **Detalhes Precisos em Tabela:** A apresentação dos dados em tabela permite uma visão detalhada e precisa dos valores específicos, sendo útil quando é necessário um nível maior de precisão numérica.
""")
