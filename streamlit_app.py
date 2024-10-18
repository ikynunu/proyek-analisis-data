import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fungsi untuk membuat dataframe
def create_pollutant_mean_df(df, df_name, pollutant):
    df_name = df.groupby(by='station').agg({pollutant:'mean'}).sort_values(by=pollutant, ascending=False).reset_index()
    df_name.rename(columns={
    'station':'Distrik',
    pollutant:'Rata-Rata Konsentrasi'
    }, inplace=True)

    return df_name

def create_pollutant_all_df(df):
    pollutant_all_df = all_df[['TEMP', 'PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']]
    pollutant_all_df.rename(columns={
    'TEMP':'Temperatur'
    }, inplace=True)

    return pollutant_all_df

def create_pollutant_hourly_df(df):
    pollutant_hour_df = df.groupby(by='hour').agg({
    "PM2.5":'mean',
    "PM10":'mean',
    "NO2":'mean',
    "SO2":'mean',
    "CO":'mean',
    "O3":'mean'
    }).reset_index()
    
    return pollutant_hour_df

# Pembuatan dataframe
all_df = pd.read_csv('dataset.csv')

pollutant_pm25 = create_pollutant_mean_df(all_df, 'pollutant_pm25', 'PM2.5')
pollutant_pm10 = create_pollutant_mean_df(all_df, 'pollutant_pm10', 'PM10')
pollutant_so2 = create_pollutant_mean_df(all_df, 'pollutant_so2', 'SO2')
pollutant_no2 = create_pollutant_mean_df(all_df, 'pollutant_no2', 'NO2')
pollutant_co = create_pollutant_mean_df(all_df, 'pollutant_co', 'CO')
pollutant_o3 = create_pollutant_mean_df(all_df, 'pollutant_o3', 'O3')
pollutant_all_df = create_pollutant_all_df(all_df)
pollutant_hour_df = create_pollutant_hourly_df(all_df)

# Antarmuka Dashboard
st.title('Air Quality')
st.caption("Rizky Nugraha | ikynunu021@gmail.com")

st.header('Gambaran')
st.write('Dataset yang digunakan pada dashboard ini adalah dataset kualitas udara. Dataset ini memiliki 420.768 baris data dari 12 dokumen CSV yang telah dibersihkan dan digabungkan. Dataset ini telah melalui proses pembersihan dan _exploratory data analysis_.')
st.write("Dataset kualitas udara ini memiliki tujuh belas kolom yang dapat dilihat contoh data teratasnya sebagai berikut:")
st.write(all_df.head(10))

st.header('Konsentrasi Polutan Paling Tinggi')
st.write('Dengan menggunakan visualisasi diagram batang, dapat dilihat stasiun dengan konsentrasi polutan paling tinggi. Visualisasi ini menampilkan lima stasiun teratas dengan konsentrasi polutan paling tinggi.')
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['Polutan PM2.5', 'Polutan PM10', 'Polutan SO2', 'Polutan NO2', 'Polutan CO', 'Polutan O3'])

colors = ["#408ABF", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

with tab1:
    fig1, ax = plt.subplots(figsize=(18, 6))
    sns.barplot(x='Rata-Rata Konsentrasi', y='Distrik', data=pollutant_pm25.head(5), palette=colors)
    ax.set_ylabel(None)
    ax.tick_params(axis='y', labelsize=15)
    ax.tick_params(axis='x', labelsize=15)

    st.pyplot(fig1)

with tab2:
    fig, ax = plt.subplots(figsize=(18, 6))
    sns.barplot(x='Rata-Rata Konsentrasi', y='Distrik', data=pollutant_pm10.head(5), palette=colors)
    ax.set_ylabel(None)
    ax.tick_params(axis='y', labelsize=15)
    ax.tick_params(axis='x', labelsize=15)

    st.pyplot(fig)

with tab3:
    fig, ax = plt.subplots(figsize=(18, 6))
    sns.barplot(x='Rata-Rata Konsentrasi', y='Distrik', data=pollutant_so2.head(5), palette=colors)
    ax.set_ylabel(None)
    ax.tick_params(axis='y', labelsize=15)
    ax.tick_params(axis='x', labelsize=15)

    st.pyplot(fig)

with tab4:
    fig, ax = plt.subplots(figsize=(18, 6))
    sns.barplot(x='Rata-Rata Konsentrasi', y='Distrik', data=pollutant_no2.head(5), palette=colors)
    ax.set_ylabel(None)
    ax.tick_params(axis='y', labelsize=15)
    ax.tick_params(axis='x', labelsize=15)

    st.pyplot(fig)

with tab5:
    fig, ax = plt.subplots(figsize=(18, 6))
    sns.barplot(x='Rata-Rata Konsentrasi', y='Distrik', data=pollutant_co.head(5), palette=colors)
    ax.set_ylabel(None)
    ax.tick_params(axis='y', labelsize=15)
    ax.tick_params(axis='x', labelsize=15)

    st.pyplot(fig)

with tab6:
    fig, ax = plt.subplots(figsize=(18, 6))
    sns.barplot(x='Rata-Rata Konsentrasi', y='Distrik', data=pollutant_o3.head(5), palette=colors)
    ax.set_ylabel(None)
    ax.tick_params(axis='y', labelsize=15)
    ax.tick_params(axis='x', labelsize=15)

    st.pyplot(fig)

st.header('Korelasi Polutan PM2.5 dengan Polutan Lain')
st.write('Dengan menggunakan visualisasi diagram _scatter plot_, dapat dilihat keterkaitan antara polutan PM2.5 dengan polutan lain. Keterkaitan kuat terlihat antara polutan PM2.5 dengan polutan PM10 dan CO. Keterkaitan lemah terlihat antara polutan PM2.5 dengan polutan SO2, NO2, dan O3.')
fig, ax = plt.subplots(nrows=3, ncols=2, figsize=(18,18))

sns.scatterplot(x='PM2.5', y='PM2.5', data=pollutant_all_df, ax=ax[0][0], s=10)
ax[0][0].set_title("Polutan PM2.5", loc="center", fontsize=15)

sns.scatterplot(x='PM2.5', y='PM10', data=pollutant_all_df, ax=ax[0][1], s=10)
ax[0][1].set_title("Polutan PM10", loc="center", fontsize=15)

sns.scatterplot(x='PM2.5', y='SO2', data=pollutant_all_df, ax=ax[1][0], s=10)
ax[1][0].set_title("Polutan SO2", loc="center", fontsize=15)

sns.scatterplot(x='PM2.5', y='NO2', data=pollutant_all_df, ax=ax[1][1], s=10)
ax[1][1].set_title("Polutan NO2", loc="center", fontsize=15)

sns.scatterplot(x='PM2.5', y='CO', data=pollutant_all_df, ax=ax[2][0], s=10)
ax[2][0].set_title("Polutan CO", loc="center", fontsize=15)

sns.scatterplot(x='PM2.5', y='O3', data=pollutant_all_df, ax=ax[2][1], s=10)
ax[2][1].set_title("Polutan O3", loc="center", fontsize=15)

st.pyplot(fig)

st.header('Rata-Rata Konsentrasi Polutan per Jam')
st.write('Dengan menggunakan visualisasi diagram garis, dapat dilihat pergerakan konsentrasi polutan masing-masing pada setiap jam. Dapat dilihat bahwa sebagian besar polutan (PM2.5, PM10, NO2, dan CO) memuncak pada waktu malam hari, polutan SO2 memuncak pada waktu siang hari, dan polutan O3 memuncak pada waktu sore hari.')
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['Polutan PM2.5', 'Polutan PM10', 'Polutan SO2', 'Polutan NO2', 'Polutan CO', 'Polutan O3'])

with tab1:
    fig, ax = plt.subplots(figsize=(18, 6))
    ax.plot(
        pollutant_hour_df['hour'],
        pollutant_hour_df['PM2.5'],
        marker='o',
        linewidth=2
    )
    ax.tick_params(axis='y', labelsize=15)
    ax.tick_params(axis='x', labelsize=15)
    plt.xticks(pollutant_hour_df['hour'])

    st.pyplot(fig)
    
with tab2:
    fig, ax = plt.subplots(figsize=(18, 6))
    ax.plot(
        pollutant_hour_df['hour'],
        pollutant_hour_df['PM10'],
        marker='o',
        linewidth=2
    )
    ax.tick_params(axis='y', labelsize=15)
    ax.tick_params(axis='x', labelsize=15)
    plt.xticks(pollutant_hour_df['hour'])

    st.pyplot(fig)
 
with tab3:
    fig, ax = plt.subplots(figsize=(18, 6))
    ax.plot(
        pollutant_hour_df['hour'],
        pollutant_hour_df['SO2'],
        marker='o',
        linewidth=2
    )
    ax.tick_params(axis='y', labelsize=15)
    ax.tick_params(axis='x', labelsize=15)
    plt.xticks(pollutant_hour_df['hour'])

    st.pyplot(fig)
 
with tab4:
    fig, ax = plt.subplots(figsize=(18, 6))
    ax.plot(
        pollutant_hour_df['hour'],
        pollutant_hour_df['NO2'],
        marker='o',
        linewidth=2
    )
    ax.tick_params(axis='y', labelsize=15)
    ax.tick_params(axis='x', labelsize=15)
    plt.xticks(pollutant_hour_df['hour'])

    st.pyplot(fig)
 
with tab5:
    fig, ax = plt.subplots(figsize=(18, 6))
    ax.plot(
        pollutant_hour_df['hour'],
        pollutant_hour_df['CO'],
        marker='o',
        linewidth=2
    )
    ax.tick_params(axis='y', labelsize=15)
    ax.tick_params(axis='x', labelsize=15)
    plt.xticks(pollutant_hour_df['hour'])

    st.pyplot(fig)
 
with tab6:
    fig, ax = plt.subplots(figsize=(18, 6))
    ax.plot(
        pollutant_hour_df['hour'],
        pollutant_hour_df['O3'],
        marker='o',
        linewidth=2
    )
    ax.tick_params(axis='y', labelsize=15)
    ax.tick_params(axis='x', labelsize=15)
    plt.xticks(pollutant_hour_df['hour'])

    st.pyplot(fig)
 
