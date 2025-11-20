import streamlit as st

st.set_page_config(
    page_title="Petunjuk - Sistem Adaptif",
    page_icon="📖"
)

st.title("📖 Petunjuk Penggunaan")

st.markdown("""
Ikuti langkah-langkah sederhana di bawah ini untuk mulai menganalisis 
aspek dari ulasan produk.
""")

# Tombol untuk mengunduh Manual Book Anda (jika ada)
# with open("path/to/Manual_Book.pdf", "rb") as file:
#     st.download_button(
#         label="Unduh Manual Book (PDF)",
#         data=file,
#         file_name="Manual_Book_Sistem_Adaptif.pdf",
#         mime="application/pdf"
#     )

st.subheader("Cara Penggunaan")
st.markdown("""
1.  Buka halaman **Analisis** melalui menu navigasi di samping.
2.  Aplikasi memiliki dua mode: "Analisis Teks" (untuk satu ulasan) dan "Analisis dari CSV" (untuk banyak ulasan).
3.  **Untuk Analisis Teks:**
    * Masukkan satu ulasan ke dalam kotak teks.
    * Klik tombol "Analisis Ulasan Ini".
    * Tunggu beberapa saat. Hasil akan muncul dalam bentuk tabel.
4.  **Untuk Analisis dari CSV:**
    * Siapkan file `.csv` yang memiliki kolom bernama **`ulasan`**.
    * Unggah file tersebut menggunakan tombol "Browse files".
    * Klik tombol "Analisis Semua Ulasan".
    * Sebuah *progress bar* akan menunjukkan kemajuan.
    * Setelah selesai, tabel hasil akan muncul beserta tombol "Download Hasil Analisis CSV".
""")

# st.subheader("Pertanyaan Umum (FAQ)")
# st.markdown("""
# **T: Berapa lama proses analisis berlangsung?** J: Tergantung. Untuk satu ulasan, biasanya memakan waktu antara 5 hingga 30 detik, karena sistem adaptif mungkin memilih *prompt* CoT yang lebih kompleks (dan lebih lambat) untuk ulasan yang panjang. Untuk analisis CSV, waktu akan dikalikan dengan jumlah baris.

# **T: Mengapa hasilnya terkadang berbeda?** J: Sistem ini menggunakan LLM yang mungkin memiliki variabilitas. Namun, pengaturan di *backend* dibuat sekonsisten mungkin (`do_sample=False`) untuk memastikan hasil yang dapat direproduksi.

# **T: Teknologi apa yang digunakan di backend?** J: Sistem ini ditenagai oleh model Qwen2-7B-Instruct yang berjalan di Google Colab, yang dihubungkan ke aplikasi Streamlit ini melalui *tunnel* Ngrok.
# """)

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