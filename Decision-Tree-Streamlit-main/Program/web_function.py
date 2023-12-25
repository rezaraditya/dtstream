# Import Library yang akan digunakan
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import streamlit as st

@st.cache_data
def load_data(): #load dataset
    df = pd.read_csv('kelulusan_mahasiswa.csv')

    x = df[["JK","Usia_Tahun","IPS1","IPS2","IPS3","IPS4","IPS5","IPS6","IPK_Lulus"]]
    y = df[["Status_Kelulusan"]]

    return df,x,y

@st.cache_data
def train_model(x,y): #Decision Tree model
    model = DecisionTreeClassifier(
            ccp_alpha=0.0, class_weight=None, criterion='entropy',
            max_depth=4, max_features=None, max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_samples_leaf=1, 
            min_samples_split=2, min_weight_fraction_leaf=0.0,
            random_state=42,splitter='best'
    )
    model.fit(x,y)
    score = model.score(x,y)

    return model, score

def predict(x,y, features): #Prediction
    model,score = train_model(x,y)
    prediction = model.predict(np.array(features).reshape(1,-1))

    return prediction, score