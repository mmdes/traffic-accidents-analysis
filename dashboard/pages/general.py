import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt


# lendo base de dados processada
dados = pd.read_csv('./data/processed/data.csv')

def show():
    st.title('Quantidade de acidentes de trânsito no Brasil por estado')
    st.write('''Neste gráfico podemos ver a distribuição da quantidade de acidentes de trânsito no Brasil separados por estado
             durante o período de 2021 a 2024''')
    
    # Contar o número de acidentes por estado
    contagem_por_uf = dados.groupby('uf').size().reset_index(name='quantidade')

    # Criar o gráfico de barras com Plotly
    fig = px.bar(
        contagem_por_uf,
        x='uf',  # Estado no eixo X
        y='quantidade',  # Quantidade de acidentes no eixo Y
        title='Quantidade de acidentes por estado',
        labels={'uf': 'Estado', 'quantidade': 'Quantidade de Acidentes'},
        text='quantidade'  # Adiciona os valores no gráfico
    )

    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig)


# Função para mostrar o mapa com acidentes de trabalho
def show_map():
    st.title('Mapa de Acidentes de Trânsito no Brasil')
    st.write('''Este mapa mostra a localização dos acidentes de trânsito no Brasil durante o período especificado.''')

    # Verificar se as colunas de latitude e longitude estão presentes
    if 'latitude' in dados.columns and 'longitude' in dados.columns:
        try:
            # Criar o mapa de dispersão usando Plotly
            fig = px.scatter_mapbox(dados, lat='latitude', lon='longitude', 
                                    hover_name='municipio', hover_data=['causa_acidente', 'tipo_acidente'],
                                    color_discrete_sequence=['fuchsia'], zoom=4, height=600)
            
            fig.update_layout(mapbox_style="open-street-map")
            fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

            # Exibir o mapa no Streamlit
            st.plotly_chart(fig)

        except Exception as e:
            st.error(f"Erro ao processar os dados para o mapa: {e}")
  
def show_topfive_causa():
    # Título e descrição
    st.title('As 5 principais causas de acidentes no Brasil')
    st.write('''Este gráfico mostra o top 5 das causas de acidentes de trânsito no Brasil durante o período especificado.''')

    # Verificar se a coluna 'causa_acidente' existe no dataset
    if 'causa_acidente' in dados.columns:
        # Contar as ocorrências das causas
        causa_counts = dados['causa_acidente'].value_counts()

        # Selecionar os 5 maiores e somar o restante como 'OUTROS'
        top_5_causas = causa_counts.head(5)
        outros = causa_counts.iloc[5:].sum()

        # Adicionar a categoria 'OUTROS'
        top_5_causas = pd.concat([top_5_causas, pd.Series({'Outras Causas': outros})])

        # Calcular o total de acidentes
        total_acidentes = dados.shape[0]

        # Calcular a porcentagem de cada causa e arredondar para 2 casas decimais
        top_5_causas_percent = (top_5_causas / total_acidentes) * 100
        top_5_causas_percent = top_5_causas_percent.round(2).reset_index()
        top_5_causas_percent.columns = ['Causa', 'Porcentagem']

        # Criar o gráfico de pizza com Plotly
        fig = px.pie(
            top_5_causas_percent,
            names='Causa',
            values='Porcentagem',
            title='As 5 maiores causas de acidentes (com outros)',
            labels={'Causa': 'Causa dos Acidentes', 'Porcentagem': 'Porcentagem de Acidentes (%)'},
            hole=0.3  # Se quiser um gráfico de anel
        )

        # Exibir o gráfico no Streamlit
        st.plotly_chart(fig)


def show_topfive_tipo():
    # Título e descrição
    st.title('Os 5 principais tipos de acidentes no Brasil')
    st.write('''Este gráfico mostra o top 5 dos tipos de acidentes de trânsito no Brasil durante o período especificado.''')

    # Verificar se a coluna 'tipo_acidente' existe no dataset
    if 'tipo_acidente' in dados.columns:
        # Contar as ocorrências das causas
        tipo_counts = dados['tipo_acidente'].value_counts()

        # Selecionar os 5 maiores e somar o restante como 'OUTROS'
        top_5_causas = tipo_counts.head(5)
        outros = tipo_counts.iloc[5:].sum()

        # Adicionar a categoria 'OUTROS'
        top_5_causas = pd.concat([top_5_causas, pd.Series({'Outros tipos': outros})])

        # Calcular o total de acidentes
        total_acidentes = dados.shape[0]

        # Calcular a porcentagem de cada causa e arredondar para 2 casas decimais
        top_5_causas_percent = (top_5_causas / total_acidentes) * 100
        top_5_causas_percent = top_5_causas_percent.round(2).reset_index()
        top_5_causas_percent.columns = ['Tipo', 'Porcentagem']

        # Criar o gráfico de pizza com Plotly
        fig = px.pie(
            top_5_causas_percent,
            names='Tipo',
            values='Porcentagem',
            title='Os 5 maiores tipos de acidentes (com outros)',
            labels={'Tipo': 'Tipo dos Acidentes', 'Porcentagem': 'Porcentagem de Acidentes (%)'},
            hole=0.3  # Se quiser um gráfico de anel
        )

        # Exibir o gráfico no Streamlit
        st.plotly_chart(fig)



def show_acidentes_por_condicao_meteorologica():
    # Título e descrição
    st.title('Quantidade de Acidentes por Condição Meteorológica')
    st.write('Este gráfico mostra a quantidade de acidentes de trânsito em diferentes condições meteorológicas.')

    # Contar as ocorrências das diferentes condições meteorológicas
    condicao_count = dados['condicao_metereologica'].value_counts().reset_index()
    condicao_count.columns = ['Condição Meteorológica', 'Quantidade de Acidentes']

    # Criar o gráfico de barras
    fig = px.bar(
        condicao_count,
        x='Condição Meteorológica',
        y='Quantidade de Acidentes',
        title='Quantidade de Acidentes por Condição Meteorológica',
        labels={'Condição Meteorológica': 'Condição Meteorológica', 'Quantidade de Acidentes': 'Número de Acidentes'},
        color='Condição Meteorológica',
        color_discrete_sequence=px.colors.qualitative.Set3
    )

    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig)

def show_acidentes_filtrados_por_condicao_meteorologica():
    # Título e descrição
    st.title('Acidentes com Feridos Graves ou Mortes por Condição Meteorológica')
    st.write(
        'Este gráfico mostra a quantidade de acidentes em diferentes condições meteorológicas, '
        'considerando apenas os casos com pelo menos um ferido grave ou uma morte.'
    )

    # Filtrar os dados com feridos graves ou mortes
    acidentes_filtrados = dados[(dados['feridos_graves'] >= 1) | (dados['mortos'] >= 1)]

    # Contar as ocorrências das diferentes condições meteorológicas
    condicao_count_filtrada = acidentes_filtrados['condicao_metereologica'].value_counts().reset_index()
    condicao_count_filtrada.columns = ['Condição Meteorológica', 'Quantidade de Acidentes']

    # Criar o gráfico de barras
    fig = px.bar(
        condicao_count_filtrada,
        x='Condição Meteorológica',
        y='Quantidade de Acidentes',
        title='Acidentes com Feridos Graves ou Mortes por Condição Meteorológica',
        labels={'Condição Meteorológica': 'Condição Meteorológica', 'Quantidade de Acidentes': 'Número de Acidentes'},
        color='Condição Meteorológica',
        color_discrete_sequence=px.colors.qualitative.Set3
    )

    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig)


def show_map_accidents_state():
    # Título e descrição
    st.title('Distribuição de acidentes de trânsito por estado')
    st.write('''Neste gráfico podemos ver a distribuição da quantidade de acidentes de trânsito no Brasil separados por estado
             durante o período de 2021 a 2024''')

    # Dados de acidentes agrupados por estado
    contagem_por_uf = dados.groupby('uf').size().reset_index(name='quantidade')

    # Dicionário com coordenadas médias dos estados brasileiros
    coordenadas = {
        'AC': [-8.77, -70.55], 'AL': [-9.19, -36.82], 'AP': [1.41, -51.77], 'AM': [-3.12, -60.67],
        'BA': [-12.46, -41.71], 'CE': [-5.21, -39.53], 'DF': [-15.78, -47.93], 'ES': [-20.30, -40.30],
        'GO': [-16.64, -49.31], 'MA': [-5.43, -47.53], 'MT': [-12.64, -56.08], 'MS': [-20.51, -54.54],
        'MG': [-18.10, -44.38], 'PA': [-3.53, -52.29], 'PB': [-7.06, -35.55], 'PR': [-25.43, -49.27],
        'PE': [-8.28, -35.07], 'PI': [-7.53, -41.41], 'RJ': [-22.91, -43.70], 'RN': [-5.22, -36.52],
        'RS': [-30.02, -51.22], 'RO': [-10.83, -63.77], 'RR': [1.98, -61.33], 'SC': [-27.60, -48.55],
        'SP': [-23.55, -46.64], 'SE': [-10.57, -37.43], 'TO': [-10.25, -48.30]
    }

    # Adicionar as coordenadas ao DataFrame de acidentes
    contagem_por_uf['latitude'] = contagem_por_uf['uf'].map(lambda x: coordenadas[x][0])
    contagem_por_uf['longitude'] = contagem_por_uf['uf'].map(lambda x: coordenadas[x][1])

    # Criar o mapa de dispersão com Plotly usando scatter_mapbox para manter a consistência
    fig = px.scatter_mapbox(contagem_por_uf,
                            lat='latitude',
                            lon='longitude',
                            size='quantidade',
                            color='quantidade',
                            hover_name='uf',
                            size_max=30,
                            color_continuous_scale="Viridis",
                            zoom=4,
                            height=600,
                            title="Distribuição de acidentes de trânsito por estado no Brasil")

    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig)
