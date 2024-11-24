import streamlit as st
from pages import home, general

# Criação da barra lateral para navegação
st.sidebar.title('Navegação')
pagina_selecionada = st.sidebar.selectbox('Selecione uma página:', ['Home', 'Gerais'])

# Renderizar a página selecionada
if pagina_selecionada == 'Home':
    home.show()
elif pagina_selecionada == 'Gerais':
    general.show()

