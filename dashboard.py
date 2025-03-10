import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")


st.title("🚲 Bike Sharing Dashboard")
st.write("Analisis Data Penyewaan Sepeda")


@st.cache_data
def load_data():
    df = pd.read_csv("all-data.csv")
    df['dteday'] = pd.to_datetime(df['dteday'])  
    return df

df = load_data()


st.sidebar.header("Filter Data")
selected_date = st.sidebar.date_input("📅 Pilih Tanggal", df['dteday'].min())


filtered_df = df[df['dteday'] == selected_date]


st.subheader(f"📅 Data pada {selected_date}")
st.dataframe(filtered_df)


if st.checkbox("Tampilkan Nama Kolom"):
    st.write("Kolom yang tersedia dalam dataset:")
    st.write(df.columns.tolist())


st.subheader("📊 Tren Penyewaan Sepeda berdasarkan Hari")


if 'weekday_x' in df.columns:
    df['weekday'] = df['weekday_x']
elif 'weekday_y' in df.columns:
    df['weekday'] = df['weekday_y']
else:
    st.error("Kolom 'weekday' tidak ditemukan!")

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=df['weekday'], y=df['cnt_x'], palette='viridis', ax=ax)
ax.set_xlabel("Hari dalam Seminggu")
ax.set_ylabel("Jumlah Penyewa Sepeda")
ax.set_title("Tren Penyewaan Sepeda berdasarkan Hari")

st.pyplot(fig)

st.subheader("⏰ Tren Penyewaan Sepeda berdasarkan Jam")

if 'hr' in df.columns:
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x=df['hr'], y=df['cnt_y'], marker='o', ax=ax)
    ax.set_xlabel("Jam")
    ax.set_ylabel("Jumlah Penyewa Sepeda")
    ax.set_title("Jumlah Penyewa Sepeda Berdasarkan Jam")
    st.pyplot(fig)
else:
    st.error("Kolom 'hr' tidak ditemukan!")


st.subheader("📈 Statistik Data")
st.write(df.describe())

st.write("🚀 Dashboard ini membantu memahami pola penggunaan sepeda berdasarkan hari dan jam tertentu.")
