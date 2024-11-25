import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def show():
    st.title('Informações gerais sobre acidentes de trânsito no Brasil')

    # lendo base de dados formatada
    dados = pd.read_csv('./data/processed/data.csv')

    contagem_por_uf = dados.groupby('uf').size().reset_index(name='quantidade')

    # Plotar o gráfico de pizza usando Plotly
    fig = px.pie(contagem_por_uf, names='uf', values='quantidade', title='Quantidade de acidentes por estado')

    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig)
