import streamlit as st

def show():
    st.title('Acidentes de Trânsito no Brasil')
    st.write('''Bem-vindo à página inicial da nossa aplicação!
                Esta aplicação foi desenvolvida por Gabriel Eduardo Bittencourt Moraes 
                e Matheus Matos de Souza como parte de um exercício na residência de Inteligência Artificial do SENAI-PR. 
                Esperamos que você aproveite a experiência e encontre insights valiosos sobre os acidentes de trânsito no Brasil.''')
    
    st.image("./dashboard/assets/logo.png", caption='Logotipo da Aplicação. Imagem gerada por Inteligência Artificial', width=700)

