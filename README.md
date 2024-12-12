
# Painel de Visualização de Dados

Este repositório contém um painel de visualização de dados desenvolvido com [Streamlit](https://streamlit.io/) para análise de dados a partir de arquivos CSV. O projeto permite carregar, processar e visualizar dados financeiros de forma interativa.

## Funcionalidades

- **Carregamento de Arquivos CSV**: Aceita arquivos no formato CSV com codificação `latin1` e delimitador `;`.
- **Conversão de Dados**: Conversão automática de colunas numéricas, ajustando valores para o formato adequado.
- **Seleção de Meses**: Filtro interativo para selecionar os meses desejados para análise.
- **Agrupamento e Somas**: Soma acumulada de valores para os meses selecionados.
- **Visualização de Dados**: Exibição de tabelas filtradas e gráficos de barras interativos.

## Requisitos

- Python 3.7 ou superior
- Bibliotecas necessárias:
  - `streamlit`
  - `pandas`

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/TN-Junior/SEPE-DisponibilidadeCaixa-RP.git
   ````
   ``` bash
   cd SEPE-DisponibilidadeCaixa-RP
    ```
2. Crie um ambiente virtual (opcional, mas recomendado):
    ``` bash
    python -m venv venv
    ```
    ``` bash
    source venv/bin/activate  # Linux/Mac
     ```
    ``` bash
    venv\Scripts\activate     # Windows
    
  3. Instale as dependências:
``` bash
    pip install -r requirements.txt
```

## Uso

1. Execute o aplicativo:
``` bash
streamlit run app.py
```

2. Acesse o painel no navegador:
``` bash
http://localhost:8501
```

## Deploy
https://sepe-disponibilidadecaixa-rp.onrender.com





