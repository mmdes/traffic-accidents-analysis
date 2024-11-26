import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


# lendo base de dados processada
dados = pd.read_csv('./data/processed/data.csv')

def show():
    st.title('Informações gerais sobre acidentes de trânsito no Brasil')
    st.write('''Aqui é possível encontrar alguns gráficos relacionados às informações gerais dos acidentes acontecidos no Brasil
             durante o período de 2021 a 2024''')
    
    contagem_por_uf = dados.groupby('uf').size().reset_index(name='quantidade')

    # Plotar o gráfico de pizza usando Plotly
    fig = px.pie(contagem_por_uf, names='uf', values='quantidade', title='Quantidade de acidentes por estado')

    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig)


# Função para mostrar o mapa com acidentes de trânsito
def show_map():
    st.title('Mapa de Acidentes de Trânsito no Brasil')
    st.write('''Este mapa mostra a localização dos acidentes de trânsito no Brasil durante o período especificado.''')

    # Verificar se as colunas de latitude e longitude estão presentes
    if 'latitude' in dados.columns and 'longitude' in dados.columns:
        # Criar o mapa de dispersão usando Plotly
        fig = px.scatter_mapbox(dados, lat='latitude', lon='longitude', 
                                hover_name='municipio', hover_data=['causa_acidente', 'tipo_acidente'],
                                color_discrete_sequence=['fuchsia'], zoom=4, height=600)
        
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

        # Exibir o mapa no Streamlit
        st.plotly_chart(fig)
  