# 🚲 Bike Sharing Dashboard

Dashboard ini dibuat untuk menganalisis data penyewaan sepeda berdasarkan berbagai faktor seperti hari, jam, dan kondisi cuaca.

## 📌 Fitur Dashboard:
- **Filter Data Berdasarkan Tanggal** 📆
- **Visualisasi Penyewaan Sepeda Berdasarkan Hari & Jam** 📊
- **Statistik Data Penyewaan Sepeda** 🔍

## 🚀 Cara Menjalankan

1. Pastikan sudah menginstal **Python** dan **Streamlit**.
2. Jalankan perintah berikut di terminal:

   ```bash
   pip install streamlit pandas matplotlib seaborn
   streamlit run dashboard.py
   ```

3. Dashboard akan muncul di browser.

## 📊 Dataset

Dataset yang digunakan adalah **all-data.csv** yang berisi informasi penyewaan sepeda berdasarkan berbagai faktor seperti:
- **Tanggal (dteday)**
- **Hari dalam Seminggu (weekday_x)**
- **Jumlah Penyewa Sepeda (cnt_x & cnt_y)**
- **Kondisi Cuaca (weathersit_x)**
- **Suhu, Kelembaban, dan Kecepatan Angin**
