import joblib
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# fungsi
def prediksi():
    st.header("Proyek: Prediksi Churn Pelanggan")
    
    # Deskripsi proyek
    st.markdown("""
    <div class="project-box">
    <h3>Deskripsi Proyek</h3>
    <p>Model ini memprediksi apakah seorang pelanggan akan berhenti menggunakan layanan (churn) berdasarkan karakteristik demografis dan perilaku mereka.</p>
    <p><strong>Metrik Performa:</strong>  Recall 64%</p>
    <p><strong>Algoritma:</strong> Random Forest Classifier</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Bagian demo prediksi
    st.markdown("""
    <div class="project-box">
    <h3>Demo Prediksi</h3>
    <p>Coba model dengan input berikut:</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Input form untuk prediksi
    col1, col2, col3 = st.columns(3)
    
    with col1:
        CreditScore = st.slider("Credit Score", 300, 850, 650)
        Age = st.slider("Usia", 18, 100, 35)
        Tenure = st.slider("Tenure (tahun)", 0, 10, 3)
    
    with col2:
        Gender = st.selectbox("Jenis Kelamin", ["Male", "Female"])
        NumOfProducts = st.selectbox("Jumlah Produk", [1, 2, 3, 4])
        HasCrCard = st.selectbox("Memiliki Kartu Kredit?", [1, 0])
    
    with col3:
        IsActiveMember = st.selectbox("Member Aktif?", [1, 0])
        EstimatedSalary = st.slider("Estimasi Gaji ($)", 0, 200000, 50000)
        Balance = st.slider("Saldo ($)", 0, 250000, 50000)
        
    # Tombol prediksi
    if st.button("Prediksi Churn"):
        # Preprocessing input
        gender_mapping = {"Male": 1, "Female": 0}
        Gender_encoded = gender_mapping[Gender]
        
        # Membuat dataframe input
        input_data = pd.DataFrame([[CreditScore, Gender_encoded,Age, Tenure,Balance,
                                  NumOfProducts, HasCrCard, IsActiveMember, 
                                  EstimatedSalary]],
                                columns=['CreditScore', 'Gender', 'Age','Tenure', 'Balance', 
                                         'NumOfProducts', 'HasCrCard', 'IsActiveMember', 
                                         'EstimatedSalary'])
        
        model = joblib.load('model_churn.joblib')
        prediction = model.predict(input_data)[0]
        prediction_proba = model.predict_proba(input_data)[0]
    
    
        # Tampilkan hasil
        st.subheader("Hasil Prediksi")
        if prediction == 1:
            st.error(f"Prediksi: Churn (Pelanggan akan berhenti) - Probabilitas: {prediction_proba[1]:.2f}")
        else:
            st.success(f"Prediksi: Tidak Churn (Pelanggan akan tetap) - Probabilitas: {prediction_proba[0]:.2f}")