import streamlit as st

st.set_page_config(
    page_title='Prediction',
    page_icon='🏠',
    layout='wide',
    initial_sidebar_state='expanded',
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': 'https://www.extremelycoolapp.com/bug',
        'About': '# This is a header. This is an *extremely* cool app!',
    },
)

st.title('House Price Prediction')

tamanho = st.number_input(
    'Tamanho (em m²)', min_value=20.0, max_value=500.0, value=100.0
)
st.write('The current number is ', tamanho)
