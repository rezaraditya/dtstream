#import Library yang dibutuhkan
import streamlit as st
from web_function import load_data

from Tabs import home, predict, visualise

Tabs = {
    "Home" : home,
    "Prediction" : predict,
    "Visualisation" : visualise
}

#membuat sidebar
st.sidebar.title("Navigasi")

#membuat radio option
page = st.sidebar.radio("Page", list(Tabs.keys()))

#load dataset
df, x, y = load_data()

#Kondisi call app function
if page in ["Prediction", "Visualisation"]:
    Tabs[page].app(df,x, y)