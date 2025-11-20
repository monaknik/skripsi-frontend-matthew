import streamlit as st

# Konfigurasi halaman (Judul tab di browser)
st.set_page_config(
    page_title="Beranda - Sistem Prompting Adaptif",
    page_icon="🤖"
)

# Judul Utama
st.title("🤖 Sistem Prompting Adaptif")
st.subheader("Analisis Aspek pada Ulasan Produk Smartphone")

st.markdown("""
Aplikasi web ini dirancang untuk menganalisis ulasan produk smartphone 
secara cerdas. Sistem ini menggunakan *Large Language Model* (LLM) Qwen2 
yang dikombinasikan dengan **Rules Engine Adaptif**. 

Sistem akan secara otomatis memilih strategi *prompting* terbaik 
berdasarkan karakteristik ulasan untuk memberikan hasil ekstraksi aspek 
yang paling akurat.
""")

# Tombol "Mulai Analisis" yang mengarah ke halaman lain
st.page_link("pages/1_Analisis.py", label="Mulai Analisis Ulasan", icon="🚀", use_container_width=True)

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