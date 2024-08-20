import streamlit as st
import requests
import json
import urllib3

urllib3.disable_warnings()

url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
payload='scope=GIGACHAT_API_PERS'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json',
    'RqUID': '6f0b1291-c7f3-43c6-bb2e-9f3efb2dc98e',
    'Authorization': 'Basic MGUzYmNiNzctOGUwNS00ZTZkLWI0YTgtNTc5NTBhYmY1MTkzOjk1ODgwZWMwLTdiYmMtNGQ5Yi04ZTU0LTM1ZDgzNjBjMGU4OA=='
}

token = requests.request("POST", url, verify=False, headers=headers, data=payload)
#print(token.text)

body_dict = token.json()
giga_chat = body_dict['access_token']
#print(giga_chat)

st.title("Чат-бот Copilot")

# Запустить историю чата
if "messages" not in st.session_state:
    st.session_state.messages = []

# Отобразить историю чата
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Поле для ввода пользовательского запроса
if prompt := st.chat_input("Введите ваш запрос"):
    # Вывод сообщения пользователя в контейнере сообщений
    with st.chat_message("Пользователь"):
        st.markdown(prompt)
    # Добавление пользовательского сообщения в историю чата
    st.session_state.messages.append({"role": "Пользователь", "content": prompt})

    #Запрос к GigaChat
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

    payload = json.dumps({
        "model": "GigaChat",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 1,
        "top_p": 0.1,
        "n": 1,
        "stream": False,
        "max_tokens": 512,
        "repetition_penalty": 1
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer '+ giga_chat
    }

    response = requests.request("POST", url, verify=False, headers=headers, data=payload)

    #body_dict = response.json()
    #response_giga_chat = body_dict['content']

    # Вывод ответа ассистента в контейнере сообщений
    with st.chat_message("Ассистент"):
        st.markdown(response.text)


    # Добавление ответа ассистента в историю чата
    st.session_state.messages.append({"role": "Ассистент ", "content": response.text})