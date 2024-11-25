import streamlit as st
from pages import home, general, travel

# Criação da barra lateral para navegação
st.sidebar.title('Navegação')
pagina_selecionada = st.sidebar.selectbox('Selecione uma página:', ['Início', 'Gerais', 'Viagens'])

# Renderizar a página selecionada
if pagina_selecionada == 'Início':
    home.show()
elif pagina_selecionada == 'Gerais':
    general.show()
elif pagina_selecionada == 'Viagens':
    travel.show()
    travel.interacao()
    travel.show_day()
    travel.show_period()