import streamlit as st

from web_function import predict

def app(df,x,y):
    st.title("Prediksi Kelulusan") 
    st.caption("Masukkan angka biner (0/1)")

    col1, col2  = st.columns(2)

    with col1:
        JK = st.text_input ('Input Jenis Kelamin')
    with col1:
        Usia_Tahun = st.text_input ('Input Usia Tahun')
    with col1:
        IPS1 = st.text_input ('Input IP Semester 1')
    with col1:
        IPS2 = st.text_input ('Input IP Semester 2')
    with col1:
        IPS3 = st.text_input ('Input IP Semester 3')

    with col2:
        IPS4 = st.text_input ('Input IP Semester 4')
    with col2:
        IPS5 = st.text_input ('Input IP Semester 5')
    with col2:
        IPS6 = st.text_input ('Input IP Semester 6')
    with col2:
        IPK_Lulus = st.text_input ('Input IPK Lulus')

    features = [JK,Usia_Tahun,IPS1,IPS2,IPS3,IPS4,IPS5,IPS6,IPK_Lulus]

    #tombol prediksi
    if st.button("Prediksi"):
        prediction, score = predict(x,y,features)
        score = score
        st.info("Prediksi Sukses")
        
        if (prediction == 1):
            st.success("Mahasiswa tersebut lulus dengan Tepat waktu")
        else:
            st.warning("Mahasiswa tersebut lulus telat")
        
        st.write("Model yang digunakan memiliki tingkat akurasi ", (score*100), "%")