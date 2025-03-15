import os
from config import logger

def generate_report(insights, predicted_revenue, future_months):
    logger.info("Generating report.txt...")

    report_path = os.path.join("reports", "report.txt")
    os.makedirs(os.path.dirname(report_path), exist_ok=True)

    with open(report_path, "w") as file:
        file.write("====================================\n")
        file.write("             COMPANY REPORT         \n")
        file.write("====================================\n\n")

        file.write("Business Insights\n")
        file.write("-----------------\n")
        for key, value in insights.items():
            file.write(f"{key}: {value}\n")

        file.write("\nPredicted Revenue for Next 12 Months\n")
        file.write("-----------------------------------\n")
        for i in range(len(future_months)):
            file.write(f"Month {future_months[i][0]}: {predicted_revenue[i]:,.2f} EUR\n")

        file.write("\nReport generated successfully.\n")

    logger.info("Report successfully generated at %s", report_path)