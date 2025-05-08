import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.set_page_config(page_title="Company Dashboard", layout="wide")

st.markdown("<h1 style='text-align: center; color: #5DADE2; margin-bottom: 1rem;'>Company Data Explorer</h1>", unsafe_allow_html=True)
st.markdown("<hr style='margin-top: -20px; margin-bottom: 30px;'>", unsafe_allow_html=True)

datasets = {
    "Clients": "output/clients.csv",
    "Employees": "output/employees.csv",
    "Sales": "output/sales.csv",
    "Projects": "output/projects.csv"
}

dataset_choice = st.selectbox("Select a dataset:", list(datasets.keys()))

if os.path.exists(datasets[dataset_choice]):
    df = pd.read_csv(datasets[dataset_choice])
    st.subheader(f"First 5 records from {dataset_choice}")
    st.dataframe(df.head())

    numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns.tolist()
    if numeric_cols:
        selected_col = st.selectbox("Select a numeric column for analysis", numeric_cols)

        sns.set_style("whitegrid")
        plt.rcParams.update({
            "axes.titlesize": 14,
            "axes.labelsize": 12,
            "xtick.labelsize": 10,
            "ytick.labelsize": 10,
        })

        st.subheader("Boxplot")
        fig1, ax1 = plt.subplots(figsize=(8, 4))
        sns.boxplot(y=df[selected_col], ax=ax1, color="skyblue")
        ax1.set_title(f"Distribution of {selected_col}")
        st.pyplot(fig1)

        st.subheader("Histogram")
        fig2, ax2 = plt.subplots(figsize=(8, 4))
        sns.histplot(df[selected_col], kde=True, ax=ax2, color="lightgreen")
        ax2.set_title(f"Histogram of {selected_col}")
        st.pyplot(fig2)

        cat_cols = df.select_dtypes(include=["object"]).columns.tolist()
        if cat_cols:
            cat_col = st.selectbox("Select a categorical column (optional)", cat_cols)

            st.subheader(f"Barplot: Average {selected_col} by {cat_col}")
            top_df = df.groupby(cat_col)[selected_col].mean().sort_values(ascending=False).head(20).reset_index()

            fig3, ax3 = plt.subplots(figsize=(10, 6))
            sns.barplot(data=top_df, x=cat_col, y=selected_col, ax=ax3, palette="crest", edgecolor="black")
            ax3.set_title(f"Top 20 average {selected_col} by {cat_col}")
            ax3.set_xlabel(cat_col, labelpad=10)
            ax3.set_ylabel(f"Average {selected_col}", labelpad=10)
            ax3.set_xticklabels(ax3.get_xticklabels(), rotation=45, ha="right")
            ax3.grid(axis='y', linestyle='--', linewidth=0.5)
            sns.despine()
            st.pyplot(fig3)
    else:
        st.warning("No numeric columns found in this dataset.")
else:
    st.error("CSV file not found. Run main.py to generate it.")