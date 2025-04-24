import streamlit as st

def display_about_me():
    st.header("Tentang Saya")
    st.markdown("""
        **Data Scientist | Machine Learning Engineer**  
        *Spesialis Predictive Modeling & Business Intelligence*
        
        > Dengan mengikuti bootcamp data science di dibimbing, saya memiliki keahlian dalam membangun solusi ML end-to-end 
        yang berdampak langsung pada bisnis. Fokus saya adalah mengubah data kompleks menjadi 
        wawasan yang dapat ditindaklanjuti melalui pendekatan berbasis data.
        """)
    
    st.subheader("Keahlian")
    st.markdown("""
     **Keahlian Inti:**
        - 🔍 Predictive Modeling (Classification & Regression)
        - 📊 Data Visualization & Business Intelligence
        - � SQL & Big Data Processing
        - 📈 Machine Learning & Deep Learning
        """)
    