import streamlit as st
from pages import home, general, travel

# Configurar o título da página e o ícone
st.set_page_config(page_title="Informações de Trânsito do Brasil", page_icon="./dashboard/assets/logo.png")

# Esconder parte barra de navegação lateral 
st.markdown( """ <style> [data-testid="stSidebarNav"] { display: none; } </style> """, unsafe_allow_html=True)

# Criação da barra lateral para navegação
st.sidebar.title('Navegação')
pagina_selecionada = st.sidebar.selectbox('Selecione uma página:', ['Início', 'Gerais', 'Viagens'])

# Renderizar a página selecionada
if pagina_selecionada == 'Início':
    home.show()
elif pagina_selecionada == 'Gerais':
    general.show()
    general.show_map()
elif pagina_selecionada == 'Viagens':
    travel.show()
    travel.interacao()
    travel.show_day()
    travel.show_period()
