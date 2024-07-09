import requests
import streamlit as st

st.set_page_config(page_title='Prediction', page_icon='🏠')

st.title('House Price Prediction')
st.subheader('', divider='red')

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

if st.button('Prever'):
    features = [[tamanho, quartos, vagas]]
    response = requests.post(
        'https://eng-api-e8wg.onrender.com/predict/ \
           accept: application/json \
           Content-Type: application/json \
            { \
            "tamanho": 100, \
            "quartos": 1, \
            "vagas": 0, \
            }'
    )

    prediction = response.json()
    st.success(f'Preço previsto: R$ {prediction}')
    st.write(f'Preço previsto: R$ {prediction}')
