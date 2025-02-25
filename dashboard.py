import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Streamlit Dashboard")

# Ladataan Titanic-datasetti
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# Osa datasta
st.write("Hieman dataa:")
st.dataframe(df.head())

# Kaavio matkustajien sukupuolijakaumasta
fig, ax = plt.subplots()
df["Sex"].value_counts().plot(kind="bar", ax=ax, color=["blue", "pink"])
st.pyplot(fig)
 
 # Valintaruutu
show_men = st.checkbox('Näytä vain miehet')

if show_men:
    df = df[df["Sex"] == "male"]

st.dataframe(df.head())

df_age = df.dropna(subset=['Age'])

plt.figure(figsize=(10, 6))
plt.hist(df_age['Age'], bins=30, color='skyblue', edgecolor='black')
plt.title('Matkustajien iän jakauma')
plt.xlabel('Ikä')
plt.ylabel('Lukumäärä')
plt.grid(True)

st.pyplot(plt)