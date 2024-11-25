import streamlit as st
import pandas as pd
import plotly.express as px

# Lendo base de dados formatada
base_path = '../data/processed/' 
dados = pd.read_csv(base_path + 'data.csv')

def show():
    st.title('Acidentes de trânsito no Brasil por dia da semana e por período do dia')
    st.write(''' O objetivo dos seguintes gráficos é informar qual o melhor dia da semana e o melhor período do dia, em relação à quantidade de acidentes,
             para realizar uma viagem. Para que seja atingido tal objetivo, é importante que as 
             BRs e os estados a serem transitados durante esta viagem sejam conhecidos previamente.''')

def filtrar_por_br_e_uf(brs, ufs):
    # Garantir que as colunas 'br' e 'uf' sejam strings
    dados['br'] = dados['br'].astype(str)
    dados['uf'] = dados['uf'].astype(str)

    # Converter BRs para strings (caso sejam números)
    brs = [str(br) for br in brs]

    # Filtrar o dataset
    dataset_filtrado = dados[dados['br'].isin(brs) & dados['uf'].isin(ufs)]

    return dataset_filtrado

def grafico_acidentes_por_dia_plotly(dataset_filtrado):
    # Definir a ordem correta dos dias da semana
    ordem_dias = ['segunda-feira', 'terça-feira', 'quarta-feira',
                  'quinta-feira', 'sexta-feira', 'sábado', 'domingo']

    # Contar acidentes por dia da semana
    acidentes_por_dia = dataset_filtrado['dia_semana'].value_counts().reindex(ordem_dias)
    fig = px.bar(
        x=acidentes_por_dia.index,
        y=acidentes_por_dia.values,
        title="Quantidade de Acidentes por Dia da Semana",
        labels={"x": "Dia da Semana", "y": "Quantidade de Acidentes"},
        color=acidentes_por_dia.values,
        color_continuous_scale="YlOrRd"
    )
    fig.update_layout(xaxis_title="Dia da Semana", yaxis_title="Quantidade de Acidentes")
    return fig

def grafico_acidentes_por_periodo_plotly(dataset_filtrado):
    # Definir a ordem dos períodos do dia
    ordem_periodos = ['madrugada', 'manhã', 'tarde', 'noite']

    # Contar acidentes por período do dia
    acidentes_por_periodo = dataset_filtrado['periodo'].value_counts()
    acidentes_por_periodo = acidentes_por_periodo.reindex(ordem_periodos)

    # Criar o gráfico de barras com Plotly Express
    fig = px.bar(
        x=acidentes_por_periodo.index,
        y=acidentes_por_periodo.values,
        title="Quantidade de Acidentes por Período do Dia",
        labels={"x": "Período do Dia", "y": "Quantidade de Acidentes"},
        color=acidentes_por_periodo.values,
        color_continuous_scale="YlOrRd"
    )

    # Atualizar layout do gráfico
    fig.update_layout(
        xaxis_title="Período do Dia",
        yaxis_title="Quantidade de Acidentes",
        xaxis_tickangle=45
    )

    return fig

def interacao():
    # Interação com o usuário para selecionar BRs e UFs
    st.title('Seleção de BRs e UFs')
    st.write('''Selecione as BRs e os estados a serem transitadas durante a sua viagem.''')

    # Lista de BRs e UFs únicas para o multiselect
    brs_disponiveis = sorted(dados['br'].unique())
    ufs_disponiveis = sorted(dados['uf'].unique())

    # Solicitar ao usuário que selecione as BRs e UFs
    brs_usuario = st.multiselect('Selecione as BRs a serem transitadas:', options=brs_disponiveis, default=brs_disponiveis[0:1])
    ufs_usuario = st.multiselect('Selecione os estados a serem transitados:', options=ufs_disponiveis, default=ufs_disponiveis[0:1])
    
    # Garantir que o usuário tenha selecionado pelo menos uma opção em cada
    if not brs_usuario or not ufs_usuario:
        st.warning("Por favor, selecione pelo menos uma BR e um estado.")
    else:
        # Filtrar os dados com base nas opções selecionadas
        dataset_filtrado = filtrar_por_br_e_uf(brs_usuario, ufs_usuario)
        
        # Armazenar os dados filtrados na sessão para uso nas funções de gráficos
        st.session_state.dataset_filtrado = dataset_filtrado

# Funções para exibir os gráficos com base na seleção do usuário
def show_day():
    st.title('Acidentes de trânsito por dia da semana')

    # Verificar se o dataset está na sessão
    if 'dataset_filtrado' in st.session_state:
        dataset_filtrado = st.session_state.dataset_filtrado
        # Plotar o gráfico de acidentes por dia da semana
        fig_dia = grafico_acidentes_por_dia_plotly(dataset_filtrado)
        # Exibir o gráfico no Streamlit
        st.plotly_chart(fig_dia)
    else:
        st.warning("Por favor, selecione as BRs e UFs primeiro.")

def show_period():
    st.title('Acidentes de trânsito por período do dia')

    # Verificar se o dataset está na sessão
    if 'dataset_filtrado' in st.session_state:
        dataset_filtrado = st.session_state.dataset_filtrado
        # Gerar o gráfico de acidentes por período do dia
        fig_periodo = grafico_acidentes_por_periodo_plotly(dataset_filtrado)
        # Exibir o gráfico no Streamlit
        st.plotly_chart(fig_periodo)
    else:
        st.warning("Por favor, selecione as BRs e UFs primeiro.")