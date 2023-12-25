import warnings
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn import tree
import streamlit as st

from web_function import train_model

def app(df,x,y):
    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.title("Visualisasi Klasifikasi Kelulusan Mahasiswa")

    if st.checkbox("Plot Confusion Matrix"):
        model, score = train_model(x, y)
        
        # Menghitung matriks kebingungan
        cm = confusion_matrix(y, model.predict(x))
        
        # Menampilkan matriks kebingungan dengan heatmap
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
        plt.xlabel('Predicted')
        plt.ylabel('Actual')
        plt.title('Confusion Matrix')
        st.pyplot()
    
    if st.checkbox("Plot Decision Tree"):
        model, score = train_model(x, y)
        dot_data = tree.export_graphviz(
            decision_tree=model, max_depth=3, out_file=None, filled=True, rounded=True, feature_names=x.columns, class_names=['Tepat', 'Telat']
        )
        st.graphviz_chart(dot_data)
