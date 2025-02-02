import streamlit as st
from pages import home, general, travel

# Configurar o título da página e o ícone
st.set_page_config(page_title="Informações de Trânsito do Brasil", page_icon="./dashboard/assets/logo.png")

# Esconder parte barra de navegação lateral 
st.markdown( """ <style> [data-testid="stSidebarNav"] { display: none; } </style> """, unsafe_allow_html=True)

# Criação da barra lateral para navegação
st.sidebar.title('Navegação')
pagina_selecionada = st.sidebar.selectbox('Selecione uma página:', ['Início', 'Dados Gerais de Acidentes', 'Simulação de Viagem'])

# Renderizar a página selecionada
if pagina_selecionada == 'Início':
    home.show()
elif pagina_selecionada == 'Dados Gerais de Acidentes':
    general.show()
    general.show_topfive_causa()
    general.show_topfive_tipo()
    general.show_acidentes_por_condicao_meteorologica()
    general.show_acidentes_filtrados_por_condicao_meteorologica()
    general.show_map()
    general.show_map_accidents_state()
elif pagina_selecionada == 'Simulação de Viagem':
    travel.show()
    travel.interacao()
    travel.show_day()
    travel.show_period()
