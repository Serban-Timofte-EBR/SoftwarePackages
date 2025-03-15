from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import numpy as np
from config import logger

def predict_revenue_growth(sales):
    logger.info("Starting revenue prediction.")

    try:
        sales["Month_Num"] = np.arange(len(sales))

        # (15) utilizarea pachetului scikit-learn (regresie liniară pentru predicție)
        X = sales[["Month_Num"]]
        y = sales["Revenue"]
        model = LinearRegression()
        model.fit(X, y)

        future_months = np.arange(len(sales), len(sales) + 12).reshape(-1, 1)
        predicted_revenue = model.predict(future_months)

        # (16) utilizarea pachetului statmodels (regresie multiplă)
        X_sm = sm.add_constant(X)  # Adăugare intercept pentru regresie multiplă
        model_sm = sm.OLS(y, X_sm).fit()
        summary = model_sm.summary()

        logger.info("Prediction successful.")
        logger.info("Statistical Model Summary:\n%s", summary)

        return predicted_revenue, future_months

    except Exception as e:
        logger.error("Error in revenue prediction: %s", str(e))
        raise