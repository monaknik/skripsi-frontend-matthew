import streamlit as st

st.set_page_config(
    page_title="Tentang - Sistem Adaptif",
    page_icon="ℹ️"
)

st.title("ℹ️ Tentang Proyek Ini")

st.subheader("Latar Belakang")
st.markdown("""
Maraknya ulasan produk di *platform e-commerce* berisi wawasan berharga 
yang sulit diekstrak secara manual. Analisis aspek adalah kunci untuk 
memahami sentimen pelanggan. Proyek ini dibangun sebagai upaya untuk 
menyediakan alat bantu berbasis teknologi *Natural Language Processing* (NLP) 
yang dapat mengekstrak aspek dari ulasan secara otomatis dan akurat 
menggunakan *prompt engineering* adaptif.
""")

st.subheader("Teknologi yang Digunakan")
st.markdown("""
Aplikasi ini ditenagai oleh beberapa teknologi modern untuk 
menganalisis teks berbahasa Indonesia. Berikut adalah *tech stack* utama yang digunakan:

* **Model LLM:** Qwen2-7B-Instruct (model dari Alibaba Cloud).
* **Backend:** Flask (Python) berjalan di Google Colab (GPU T4) untuk 
    melayani API model.
* **Frontend:** Streamlit (Python) untuk membangun antarmuka pengguna 
    interaktif ini.
* **Konektivitas:** Ngrok digunakan sebagai layanan *tunneling* untuk 
    menghubungkan *frontend* Streamlit ke *backend* di Google Colab.
""")

st.subheader("Tujuan Proyek")
st.markdown("""
Tujuan utama dari pengembangan aplikasi ini adalah untuk memenuhi 
syarat kelulusan Program Studi Teknik Informatika, Universitas Tarumanagara, 
sekaligus merancang sebuah sistem cerdas yang dapat memilih strategi 
*prompting* terbaik secara dinamis berdasarkan karakteristik input teks.
""")

# --- FOOTER ---
st.markdown("---")
col1, col2, col3 = st.columns([2, 2, 2])

with col1:
    st.markdown("##### 🤖 Sistem Adaptif")
    st.markdown("""
    Proyek skripsi untuk klasifikasi aspek 
    pada ulasan produk smartphone menggunakan 
    LLM dan *prompt engineering* adaptif.
    """)

with col2:
    st.markdown("##### Tautan Cepat")
    st.page_link("Beranda.py", label="Beranda", icon="🏠")
    st.page_link("pages/1_Analisis.py", label="Analisis", icon="🔎")
    st.page_link("pages/2_Petunjuk.py", label="Petunjuk Penggunaan", icon="📖")
    st.page_link("pages/3_Tentang.py", label="Tentang Proyek", icon="ℹ️")

with col3:
    st.markdown("##### Informasi")
    # Anda bisa tambahkan logo FTI jika punya filenya
    # st.image("path/to/logo_fti.png", width=100)
    st.markdown("""
    **Dosen Pembimbing:** Viny Christanti Mawardi, S.Kom., M.Kom.
    
    **Universitas Tarumanagara** Jl. Letjen S. Parman No. 1  
    Jakarta Barat, 11440
    
    © 2025 Matthew Alexander Tjahjadi - 535220117
    """)