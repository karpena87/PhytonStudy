import streamlit as st
import requests

def getRequest():
    if 'url' not in st.session_state:
        st.session_state.disabled = False

    url = st.text_input("Введите URL", placeholder="https://", key='url', disabled=st.session_state.disabled)
    st.button_submit = st.button('Проверить запрос', key='but_sub')

    response = requests.get(url)

    if response.status_code == 200:
        st.session_state.disabled = True
        st.write_stream(response)
    else:
        st.session_state.disabled = False
        st.write('Некорректный URL. Попробуйте еще раз.')
getRequest()



#https://github.com/karpena87/PhytonStudy/blob/main/Disable_Input.py
#https://api.kraken.com/0/public/SystemStatus
#url с ошибкой https://api.kraken.com/0/public/SystemStat


