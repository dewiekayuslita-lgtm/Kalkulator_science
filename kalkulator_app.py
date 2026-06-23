import streamlit as st
import math

# Konfigurasi Halaman
st.set_page_config(page_title="Kalkulator Saintifik", page_icon="🧮")

st.title("🧮 Kalkulator Saintifik")
st.write("Aplikasi kalkulator berbasis web menggunakan Streamlit.")

# Sidebar untuk navigasi atau informasi tambahan
st.sidebar.header("Informasi")
st.sidebar.info("Kalkulator ini mendukung operasi aritmatika dasar dan fungsi trigonometri (dalam derajat).")

# Pilihan Operasi
menu = ["Penjumlahan", "Pengurangan", "Perkalian", "Pembagian", "Sin", "Cos", "Tan", "Akar Kuadrat", "Pangkat"]
operasi = st.selectbox("Pilih operasi yang diinginkan:", menu)

# Input Data
if operasi in ["Sin", "Cos", "Tan", "Akar Kuadrat"]:
    val = st.number_input("Masukkan angka:", value=0.0)
else:
    col1, col2 = st.columns(2)
    a = col1.number_input("Angka pertama:", value=0.0)
    b = col2.number_input("Angka kedua:", value=0.0)

# Proses Perhitungan
if st.button("Hitung Sekarang"):
    if operasi == "Penjumlahan":
        st.success(f"Hasil: {a + b}")
    elif operasi == "Pengurangan":
        st.success(f"Hasil: {a - b}")
    elif operasi == "Perkalian":
        st.success(f"Hasil: {a * b}")
    elif operasi == "Pembagian":
        if b != 0:
            st.success(f"Hasil: {a / b}")
        else:
            st.error("Error: Pembagian dengan nol tidak dimungkinkan!")
    elif operasi == "Sin":
        st.success(f"Sin({val}°) = {math.sin(math.radians(val)):.4f}")
    elif operasi == "Cos":
        st.success(f"Cos({val}°) = {math.cos(math.radians(val)):.4f}")
    elif operasi == "Tan":
        if abs(val % 180) == 90:
            st.warning("Hasil: Undefined (Asimtot)")
        else:
            st.success(f"Tan({val}°) = {math.tan(math.radians(val)):.4f}")
    elif operasi == "Akar Kuadrat":
        if val >= 0:
            st.success(f"Akar dari {val} = {math.sqrt(val):.4f}")
        else:
            st.error("Error: Angka negatif tidak memiliki akar real!")
    elif operasi == "Pangkat":
        st.success(f"Hasil: {math.pow(a, b)}")
