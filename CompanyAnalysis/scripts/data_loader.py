import os
import pandas as pd
from config import DATA_PATH, logger

def load_data():
    logger.info("Loading datasets from %s", DATA_PATH)

    try:
        # (6) importul unei fișier csv sau json în pachetul pandas
        clients = pd.read_csv(os.path.join(DATA_PATH, "Clients_Dataset.csv"))
        employees = pd.read_csv(os.path.join(DATA_PATH, "Employees_Dataset.csv"))
        sales = pd.read_csv(os.path.join(DATA_PATH, "Sales_Dataset.csv"))
        projects = pd.read_csv(os.path.join(DATA_PATH, "Current_Projects_Dataset.csv"))

        logger.info("Datasets successfully loaded.")
        return clients, employees, sales, projects

    except Exception as e:
        logger.error("Error loading datasets: %s", str(e))
        raise