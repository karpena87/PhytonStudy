import streamlit as st
import urllib3
import requests

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

st.write (token.text)