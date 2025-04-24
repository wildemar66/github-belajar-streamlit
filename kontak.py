import streamlit as st

def display_contact():
    st.header("Hubungi Saya")
    
    with st.form(key='contact_form'):
        name = st.text_input("Nama Lengkap")
        email = st.text_input("Email")
        message = st.text_area("Pesan")
        submit_button = st.form_submit_button("Kirim Pesan")
        
        if submit_button:
            if name and email and message:
                st.success("Pesan Anda telah terkirim! Saya akan segera menghubungi Anda.")
                
            else:
                st.warning("Harap isi semua field!")
                
    st.markdown("""
    **Media Sosial:**  
    - [LinkedIn](www.linkedin.com/in/wildemarminggu.com)  
    - [GitHub](https://github.com/wildemar66/github-belajar-streamlit)  
    """)