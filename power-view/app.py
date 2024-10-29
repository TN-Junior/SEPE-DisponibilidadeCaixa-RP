import streamlit as st
import pandas as pd

# Título do painel
st.title("Painel de Visualização de Dados")

# Caminho do arquivo carregado
uploaded_file = 'SEPE - DISPONIBILIDADE DE CAIXA E RP - OUTROS PODERES E ÓRGÃOS Cópia_1729190602294.csv'

# Verificação se o arquivo foi carregado
if uploaded_file:
    try:
        # Ler o arquivo com codificação 'latin1' e delimitador ';'
        df = pd.read_csv(uploaded_file, encoding='latin1', delimiter=';')

        # Verificação se o DataFrame está vazio após a leitura
        if df.empty:
            st.error("O arquivo não contém dados ou está vazio.")
        else:
            # Converter as colunas numéricas para o formato correto, substituindo a vírgula por ponto
            colunas_para_converter = df.columns[df.columns.get_loc('DISPONIBILIDADE DE CAIXA BRUTA (a)'):]
            df[colunas_para_converter] = df[colunas_para_converter].replace(',', '.', regex=True).astype(float)

            # Manter a ordem original da coluna 'IDENTIFICAÇÃO DOS RECURSOS'
            ordem_original = df['IDENTIFICAÇÃO DOS RECURSOS'].unique()

            # Filtro para selecionar múltiplos meses
            meses_selecionados = st.multiselect("Selecione os meses", df['Mês'].unique())

            if meses_selecionados:
                # Filtrar o DataFrame pelos meses selecionados mantendo a ordem original
                df_filtrado = df[df['Mês'].isin(meses_selecionados)]

                # Agrupar e somar os valores apenas se houver múltiplos meses selecionados
                if len(meses_selecionados) > 1:
                    df_soma = df_filtrado.groupby('IDENTIFICAÇÃO DOS RECURSOS')[colunas_para_converter].sum().reset_index()
                else:
                    df_soma = df_filtrado

                # Reordenar o DataFrame com base na ordem original
                df_soma['IDENTIFICAÇÃO DOS RECURSOS'] = pd.Categorical(df_soma['IDENTIFICAÇÃO DOS RECURSOS'], categories=ordem_original, ordered=True)
                df_soma = df_soma.sort_values('IDENTIFICAÇÃO DOS RECURSOS')

                # Exibir a soma dos valores acumulados
                st.subheader(f"Soma Acumulada para os Meses Selecionados: {', '.join(meses_selecionados)}")
                st.write(df_soma)

                # Exibição de gráfico de barras para a coluna 'DISPONIBILIDADE DE CAIXA BRUTA (a)'
                if 'DISPONIBILIDADE DE CAIXA BRUTA (a)' in df_soma.columns:
                    st.subheader("Gráfico de Barras - Soma Acumulada de 'DISPONIBILIDADE DE CAIXA BRUTA (a)'")
                    st.bar_chart(df_soma.set_index('IDENTIFICAÇÃO DOS RECURSOS')['DISPONIBILIDADE DE CAIXA BRUTA (a)'])

            else:
                st.write("Por favor, selecione pelo menos um mês para visualizar os dados.")

    except Exception as e:
        st.error(f"Erro ao ler o arquivo: {e}")

else:
    st.write("Por favor, faça o upload de um arquivo CSV para visualizar os dados.")
