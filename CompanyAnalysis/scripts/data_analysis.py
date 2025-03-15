import pandas as pd
from config import logger

# (3) definirea și apelarea unor funcții
def get_business_insights(clients, employees, sales, projects):
    logger.info("Generating business insights.")

    # (7) accesarea datelor cu loc și iloc
    sample_client = clients.loc[0, ["CompanyName", "Industry"]]
    sample_employee = employees.iloc[0, 2]  # Accesare prin index numeric

    # (8) modificarea datelor în pachetul pandas
    sales["ProfitMargin"] = (sales["Revenue"] - sales["Costs"]) / sales["Revenue"] * 100

    # (9) utilizarea funcțiilor de grup
    avg_contract_per_industry = clients.groupby("Industry")["ContractValue"].mean()

    # (12) prelucrări statistice, gruparea și agregarea datelor în pachetul pandas
    yearly_revenue = sales.groupby(sales["Month"].dt.year)["Revenue"].sum()

    insights = {
        "Total Clients": clients.shape[0],
        "Avg Contract Value (EUR)": clients["ContractValue"].mean(),
        "Avg Employee Performance": employees["PerformanceScore"].mean(),
        "Avg Revenue Growth (%)": sales["GrowthRate"].mean(),
        "Industry-wise Avg Contract Value": avg_contract_per_industry.to_dict(),
        "Yearly Revenue Trend": yearly_revenue.to_dict()
    }

    logger.info("Business Insights: %s", insights)
    return insights

# (1) utilizarea listelor și a dicționarelor
def analyze_contracts(clients):
    industries = list(clients["Industry"].unique())
    industry_clients = {industry: clients[clients["Industry"] == industry].shape[0] for industry in industries}
    return industries, industry_clients

# (2) utilizarea seturilor și a tuplurilor
def analyze_industries(clients):
    industry_set = set(clients["Industry"])
    industry_counts = clients["Industry"].value_counts()
    top_3_industries = tuple(industry_counts.head(3).index)
    return industry_set, top_3_industries

# (5) utilizarea structurilor repetitive
def average_contracts_by_industry(clients):
    industry_contracts = {}
    for industry in clients["Industry"].unique():
        industry_contracts[industry] = clients[clients["Industry"] == industry]["ContractValue"].mean()
    return industry_contracts

# (13) prelucrarea seturilor de date cu merge / join
def merge_clients_projects(clients, projects):
    merged_data = pd.merge(clients, projects, on="ClientID", how="left")
    return merged_data