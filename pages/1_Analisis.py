import streamlit as st
import pandas as pd
import time
import requests
import re

# ==============================
# KONFIGURASI STREAMLIT
# ==============================
st.set_page_config(
    page_title="Sistem Prompting Adaptif",
    page_icon="📱",
    layout="wide"
)

st.title("📱 Sistem Prompting Adaptif")
st.caption("Analisis aspek ulasan smartphone menggunakan Qwen2-7B-Instruct (via FastAPI)")

FASTAPI_URL = "https://len-unprecipiced-ai.ngrok-free.dev/analisis"  

# ==============================
# FUNGSI PEMBANTU
# ==============================
def bersihkan_teks(teks: str) -> str:
    """Hilangkan emoji dan simbol biar tampilannya clean."""
    return re.sub(r'[^\w\s,.!?-]', '', teks)

def tentukan_kategori_panjang(jumlah_kata: int) -> str:
    if jumlah_kata <= 7:
        return "Sangat Pendek"
    elif jumlah_kata <= 12:
        return "Pendek"
    elif jumlah_kata <= 19:
        return "Sedang"
    elif jumlah_kata <= 32:
        return "Panjang"
    else:
        return "Sangat Panjang"


def analisis_ulasan_api(ulasan: str):
    """Kirim ulasan ke endpoint FastAPI dan kembalikan hasil + waktu proses."""
    start_time = time.time()
    try:
        response = requests.post(FASTAPI_URL, json={"ulasan": ulasan})
        durasi = round(time.time() - start_time, 2)
        data = response.json() if response.status_code == 200 else {}

        aspek = data.get("prediksi", [])
        if isinstance(aspek, dict):  # kalau hasilnya nested
            aspek = aspek.get("prediksi", [])

        jumlah_kata = len(ulasan.split())
        kategori = tentukan_kategori_panjang(jumlah_kata)

        return {
            "Ulasan": bersihkan_teks(ulasan),
            "Aspek Terdeteksi": ", ".join(aspek) if aspek else "-",
            "Jumlah Kata": jumlah_kata,
            "Kategori Panjang": kategori,
            "Durasi (detik)": durasi
        }

    except Exception as e:
        durasi = round(time.time() - start_time, 2)
        return {
            "Ulasan": bersihkan_teks(ulasan),
            "Aspek Terdeteksi": f"Error: {e}",
            "Jumlah Kata": "-",
            "Kategori Panjang": "-",
            "Durasi (detik)": durasi
        }

tab1, tab2 = st.tabs(["Analisis Teks", "Analisis dari CSV"])

# Ulasan satuan
with tab1:
    st.subheader("Masukkan Ulasan")
    ulasan = st.text_area("Ulasan:", "Masukkan Ulasan", height=150)
    if st.button("Analisis Ulasan Ini"):
        if not ulasan.strip():
            st.warning("Mohon isi teks ulasan terlebih dahulu.")
        else:
            with st.spinner("Sedang menganalisis..."):
                hasil = analisis_ulasan_api(ulasan)
                df = pd.DataFrame([hasil])
                df.index = range(1, len(df) + 1)  
                st.success("Analisis selesai!")
                st.dataframe(df, use_container_width=True)

# Ulasan dari CSV
with tab2:
    st.subheader("Analisis Banyak Ulasan dari CSV")
    uploaded_file = st.file_uploader("Upload file CSV dengan kolom `ulasan`/`comment`/`komentar`", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        
        df.columns = df.columns.str.strip().str.lower()
        
        valid_columns = ["ulasan", "comment", "komentar"]
        
        found_col = next((col for col in valid_columns if col in df.columns), None)
        
        if found_col is None:
            st.error("CSV harus memiliki kolom bernama `ulasan`.")

        
        else:
            if found_col != "ulasan":
                df = df.rename(columns={found_col: "ulasan"})
            
            st.success(f"Kolom '{found_col}' ditemukan! Siap dianalisis.")
            st.info(f"Jumlah ulasan terdeteksi: {len(df)}")
            if st.button("Analisis Semua Ulasan"):
                hasil_semua = []
                progress_bar = st.progress(0)
                
                for i, row in df.iterrows():
                    hasil = analisis_ulasan_api(row["ulasan"]) 
                    hasil_semua.append(hasil)
                    progress_bar.progress((i + 1) / len(df))
                
                progress_bar.empty()
                hasil_df = pd.DataFrame(hasil_semua)
                hasil_df.index = range(1, len(hasil_df) + 1)  
                st.success("Semua ulasan berhasil dianalisis!")
                st.dataframe(hasil_df, use_container_width=True)

                # Tombol download hasil
                csv = hasil_df.to_csv(index=False).encode("utf-8")
                st.download_button(
                    label="Download Hasil Analisis CSV",
                    data=csv,
                    file_name="hasil_analisis_aspek.csv",
                    mime="text/csv"
                )

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