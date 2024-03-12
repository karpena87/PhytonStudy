import streamlit as st
import requests

def getRequest():
    response = requests.get('https://api.github.com/search/repositories')
    return response
st.write_stream(getRequest())









