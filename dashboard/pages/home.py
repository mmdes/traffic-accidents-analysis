import streamlit as st

def show():
    st.title('Acidentes de Trânsito no Brasil')
    st.write('''Bem-vindo à página inicial 
             da aplicação. Esta aplicação foi desenvolvida por Gabriel Bittencourt e Matheus Matos 
             para ser apresentada como atividade na residência de Inteligência Artificial do SENAI-PR.''')
    st.image("./dashboard/assets/logo.png", caption='Logotipo da Aplicação. Imagem gerada por Inteligência Artificial', width=700)