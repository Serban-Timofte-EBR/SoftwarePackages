from scripts.data_loader import load_data
from scripts.data_cleaner import preprocess_datasets
from scripts.data_analysis import get_business_insights
from scripts.data_visualization import plot_revenue_trend
from scripts.business_prediction import predict_revenue_growth
from scripts.report_generator import generate_report
from config import logger
import datetime

def main():
    logger.info("Starting Company Analysis at %s", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    clients, employees, sales, projects = load_data()

    clients, employees, sales, projects = preprocess_datasets(clients, employees, sales, projects)

    insights = get_business_insights(clients, employees, sales, projects)
    logger.info("Final Insights: %s", insights)

    plot_revenue_trend(sales)

    predicted_revenue, future_months = predict_revenue_growth(sales)
    logger.info("Predicted Revenue for Next 12 Months: %s", predicted_revenue)
    
    generate_report(insights, predicted_revenue, future_months)

if __name__ == "__main__":
    main()