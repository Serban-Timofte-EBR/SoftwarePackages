import pandas as pd

clients = pd.read_csv("../data/Clients_Dataset.csv")
employees = pd.read_csv("../data/Employees_Dataser.csv")
sales = pd.read_csv("data/Sales_Dataser.csv")
projects = pd.read_csv("data/Current_Projects_Dataser.csv")

print("Clients Info:", clients.info())
print("Employees Info:", employees.info())
print("Sales Info:", sales.info())
print("Projects Info:", projects.info())

print(clients.head())
print(employees.head())
print(sales.head())
print(projects.head())