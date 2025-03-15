import pandas as pd
from config import logger

# (3) definirea și apelarea unor funcții
def clean_data(df, name):
    logger.info("Cleaning dataset: %s", name)

    # (10) tratarea valorilor lipsă
    missing_values_before = df.isnull().sum().sum()
    df.dropna(inplace=True)  # Eliminare valori lipsă
    missing_values_after = df.isnull().sum().sum()

    logger.info("Missing values in %s: Before=%d, After=%d", name, missing_values_before, missing_values_after)
    return df

def preprocess_datasets(clients, employees, sales, projects):
    # (3) definirea și apelarea unor funcții
    # (4) utilizarea structurilor condiționale
    clients["ContractStartDate"] = pd.to_datetime(clients["ContractStartDate"])
    sales["Month"] = pd.to_datetime(sales["Month"])

    # (11) ștergerea de coloane și înregistrări (exemplu: eliminarea duplicatelor)
    clients.drop_duplicates(inplace=True)

    clients = clean_data(clients, "Clients")
    employees = clean_data(employees, "Employees")
    sales = clean_data(sales, "Sales")
    projects = clean_data(projects, "Projects")

    logger.info("Data cleaning complete.")
    return clients, employees, sales, projects