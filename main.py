import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from PIL import Image

# Konfigurasi halaman
st.set_page_config(
    page_title="Portfolio Saya",
    page_icon=":briefcase:",
    layout="wide"
)

# CSS kustom
st.markdown("""
<style>
    .big-font {
        font-size:24px !important;
    }
    .project-box {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# Header
col1, col2 = st.columns([1, 3])
with col1:
    # Tampilkan gambar profil
    image = Image.open("wil.jpg") 
    st.image(image, width=200)
    
with col2:
    st.title("Wildemar Minggu")
    st.markdown("""
    **Data Scientist**  
    :email: wildemarminggu66@gmail.com.com | :phone: +62 812 4157 8073 
    :briefcase: [LinkedIn](www.linkedin.com/in/wildemarminggu)
    """)
    
# navigasi
st.sidebar.title("Navigasi")
page = st.sidebar.radio('Pilih halaman:',["Tentang Saya", "Proyek", "Keterampilan", "Kontak"])
if page == 'Tentang Saya':
    import tentang_saya as ts
    ts.display_about_me()
    
elif page == 'Kontak':
    import kontak as kc
    kc.display_contact()
    
elif page == 'Keterampilan':
    import skil as sk
    sk.tentang_skil()