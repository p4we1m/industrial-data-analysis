import os
import pandas as pd
import streamlit as st

# Określenie dynamicznej ścieżki do pliku danych
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "../data/synthetic_machine_data.csv")

# Sprawdzanie, czy plik istnieje
if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"Plik nie został znaleziony: {DATA_PATH}")

# Wczytaj dane
df = pd.read_csv(DATA_PATH)

# Aplikacja Streamlit
st.title("Analiza danych maszyn przemysłowych")
st.line_chart(df[["temperature", "vibration"]])
st.write("Tabela danych")
st.dataframe(df.head())
