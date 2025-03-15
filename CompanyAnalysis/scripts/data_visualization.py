import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from config import logger

def plot_revenue_trend(sales):
    logger.info("Generating improved revenue trend visualization.")

    try:
        # (14) reprezentare grafică a datelor cu pachetul matplotlib
        sales["Month"] = pd.to_datetime(sales["Month"])
        sales["Year"] = sales["Month"].dt.year
        yearly_sales = sales.groupby("Year").agg({"Revenue": "sum", "Costs": "sum"}).reset_index()

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(yearly_sales["Year"], yearly_sales["Revenue"], marker="o", linestyle="-", color="blue", label="Revenue")
        ax.plot(yearly_sales["Year"], yearly_sales["Costs"], marker="o", linestyle="-", color="red", label="Costs")

        ax.set_title("Revenue vs Costs Over Time", fontsize=14)
        ax.set_xlabel("Year", fontsize=12)
        ax.set_ylabel("Amount (€)", fontsize=12)
        ax.legend()
        ax.grid(True)

        plt.xticks(rotation=45)
        plt.show()

        logger.info("Improved visualization generated successfully.")

    except Exception as e:
        logger.error("Error generating improved visualization: %s", str(e))