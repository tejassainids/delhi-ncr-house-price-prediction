# 🏠 Delhi NCR House Price Predictor

## Project Overview

This project predicts house prices in the Delhi NCR region using **Machine Learning**. A Linear Regression model is trained on housing data to estimate the selling price of a property based on its characteristics.

---

## Objective

To build a regression model that predicts the price of a house using important numerical features.

---

## Dataset Features

* Area (sq ft)
* Number of Bedrooms (BHK)
* Parking

**Target Variable**

* House Price

---

## Project Workflow

1. Import libraries
2. Load dataset
3. Exploratory Data Analysis (EDA)
4. Correlation analysis
5. Feature and target selection
6. Train-test split
7. Train Linear Regression model
8. Generate predictions
9. Evaluate the model
10. Save predictions and trained model

---

## Model Evaluation

The following evaluation metrics were used:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

---

## Output Files

* `predictions.csv`
* `correlation_heatmap.png`
* `area_vs_price.png`
* `bhk_vs_price.png`
* `parking_vs_price.png`
* `residual_plot.png`
* `actual_vs_predicted.png`
* `house_price_model.pkl`

---

## Libraries Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib

---

## Future Improvements

* Include location as a feature.
* Add property age and property type.
* Handle outliers more effectively.
* Compare Linear Regression with Decision Tree, Random Forest, and XGBoost models.

---

## Learning Outcome

This project demonstrates the complete workflow of a Machine Learning regression problem, including data exploration, feature selection, model training, evaluation, visualization, prediction, and model persistence.
