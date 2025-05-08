import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.set_page_config(page_title="Company Dashboard", layout="wide")
st.title("Company Data Explorer (Streamlit Edition)")

datasets = {
    "Clients": "output/clients.csv",
    "Employees": "output/employees.csv",
    "Sales": "output/sales.csv",
    "Projects": "output/projects.csv"
}

dataset_choice = st.selectbox("Alege un set de date", list(datasets.keys()))

if os.path.exists(datasets[dataset_choice]):
    df = pd.read_csv(datasets[dataset_choice])
    st.subheader(f"Primele 5 înregistrări din {dataset_choice}")
    st.dataframe(df.head())

    numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns.tolist()
    if numeric_cols:
        selected_col = st.selectbox("Alege o coloana numerica pentru analiza", numeric_cols)

        st.subheader("Boxplot")
        fig1, ax1 = plt.subplots()
        sns.boxplot(y=df[selected_col], ax=ax1)
        st.pyplot(fig1)

        st.subheader("Histograma")
        fig2, ax2 = plt.subplots()
        sns.histplot(df[selected_col], kde=True, ax=ax2)
        st.pyplot(fig2)

        cat_cols = df.select_dtypes(include=["object"]).columns.tolist()
        if cat_cols:
            cat_col = st.selectbox("Alege o coloana categorică (opționala)", cat_cols)
            st.subheader(f"Barplot: Medie {selected_col} pe {cat_col}")
            top_df = df.groupby(cat_col)[selected_col].mean().sort_values(ascending=False).head(20).reset_index()
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.barplot(data=top_df, x=cat_col, y=selected_col, ax=ax)
            ax.set_title(f"Top 20 medii {selected_col} pe {cat_col}")
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
            st.pyplot(fig)
    else:
        st.warning("Nu exista coloane numerice în acest set de date.")
else:
    st.error("Fisierul CSV nu a fost gasit. Rulează `main.py` pentru a-l genera.")