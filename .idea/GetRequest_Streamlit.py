import streamlit as st
import requests

def getRequest():
    response = requests.get('https://api.github.com/search/repositories')
    response.text
getRequest()








