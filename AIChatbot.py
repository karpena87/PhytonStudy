import streamlit as st

st.title("Эхо чат Copilot")

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

    response = f"Эхо: {prompt}"
    # Вывод ответа ассистента в контейнере сообщений
    with st.chat_message("Ассистент"):
        st.markdown(response)
    # Добавление ответа ассистента в историю чата
    st.session_state.messages.append({"role": "Ассистент", "content": response})