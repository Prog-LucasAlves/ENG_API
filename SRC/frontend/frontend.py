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
    data = {
        'tamanho': tamanho,
        'quartos': quartos,
        'vagas': vagas,
    }
    response = requests.post('https://eng-api-e8wg.onrender.com/predict/', json=data)
    prediction = response.json()
    st.success(f'Preço previsto: R$ {prediction['prediction']:,.2f}')
    st.balloons()
