import streamlit as st

def tentang_skil():
    st.header("Keterampilan Teknis")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Bahasa Pemrograman")
        st.markdown("""
        - Python
        - JavaScript
        - SQL
        """)
        
    with col2:
        st.subheader("Framework & Tools")
        st.markdown("""
        - Streamlit
        - React
        - TensorFlow
        """)
        
    with col3:
        st.subheader("Lainnya")
        st.markdown("""
        - Analisis Data
        - Machine Learning
        - Manajemen Proyek
        """)
        