import requests
import streamlit as st

# Título da página.
st.set_page_config(page_title='Prediction', page_icon='🏠')

# Descrição da aplicação.
st.title('House Price Prediction')
st.subheader('', divider='red')

# Criando colunas aonde serão inseridos os dados.
col1, col2, col3 = st.columns(3)

with col1:
    tamanho = st.number_input('Tamanho (em m²)', min_value=0, max_value=500, value=20)
    st.write('The current number is ', tamanho)

with col2:
    quartos = st.number_input(
        'Quartos (Quantidade)', min_value=0, max_value=10, value=0
    )
    st.write('The current number is ', quartos)

with col3:
    vagas = st.number_input(
        'Vagas de Garagem (Quantidade)', min_value=0, max_value=10, value=0
    )
    st.write('The current number is ', vagas)

# Botão para realizar a previsão da aplicação
if st.button('Prever'):
    data = {
        'tamanho': tamanho,
        'quartos': quartos,
        'vagas': vagas,
    }
    # Acessando a api para realizar a previsão com os dados coletados
    response = requests.post('https://eng-api-e8wg.onrender.com/predict/', json=data)
    prediction = response.json()
    st.success(f'Preço previsto: R$ {prediction['prediction']:,.2f}')
    st.balloons()
    st.subheader('', divider='red')
