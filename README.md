# traffic-accidents-analysis
Exercício em dupla com o objetivo de **analisar os dados de acidentes de trânsito no Brasil** entre os anos de 2021 a 2024. Neste exercício praticamos processamento e visualização de dados e desenvolvimento colaborativo através do git.

## Entendendo os diretórios
### `dashboard`
- **assets**: Contém recursos estáticos da nossa aplicação Streamlit.
- **pages**: Contém os arquivos Python que representam as diferentes páginas da aplicação Streamlit.
  - **general.py**: Script contendo a lógica e a visualização da página "Gerais" da aplicação.
  - **home.py**: Script contendo a lógica e a visualização da página inicial da aplicação.
- **app.py**: Arquivo principal que gerencia a aplicação Streamlit.
### `data`
- **processed**: Armazena os dados que já foram processados e estão prontos para serem utilizados na aplicação Streamlit.
  - **data.csv**: Arquivo CSV contendo os dados processados prontos para análise.
- **raw**: Armazena os dados brutos, que ainda não foram processados.
  - **2021.csv**, **2022.csv**, **2023.csv**, **2024.csv**: Arquivos CSV contendo os dados brutos de acidentes de trânsito dos respectivos anos.
### `notebooks`
- **exploratory_analysis.ipynb**: Notebook Jupyter contendo a análise exploratória dos dados de acidentes de trânsito.
- **feature_engineering.ipynb**: Notebook Jupyter contendo a engenharia de atributos dos dados, transformando-os em um formato adequado para aplicação.


## Colaboração

## Como rodar?
Siga os seguintes passos para rodar a aplicação em modo de desenvolvimento:

1. **Instalação das dependências:**
   - Instale todas as dependências necessárias para rodas aplicação em seu ambiente usando o seguinte comando:

     ```bash
        pip install -r requirements.txt
     ```
2. **Arquivos de dados:**
    - Disponha os arquivos de dados brutos no diretório **/data/raw**
3. **Execute os notebooks:**
    - Execute o notebook **/notebooks/exploratory_analysis.ipynb** célula a célula e acompanhe a análise exploratória dos dados.
    - Execute o notebook **/notebook/feature_engineering.ipynb** e acompanhe a transformação do dado até sua persistência em **/data/processed** como data.csv
4. **Executando a aplicação Streamlit:**
    - Para executar a aplicação rode o seguinte comando

    ```bash
        streamlit run ./dashboard/app.py
    ```
