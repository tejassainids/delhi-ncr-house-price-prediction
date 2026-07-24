# 🏠 Delhi NCR House Price Prediction

An end-to-end Machine Learning project that predicts residential property prices in the Delhi NCR region using multiple regression algorithms.

The project demonstrates the complete ML workflow:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Visualization
- Feature Selection
- Linear Regression (Baseline Model)
- Decision Tree Regression
- Hyperparameter Tuning
- Model Evaluation
- User Prediction
- Streamlit Frontend

---

# 📌 Dataset

**Dataset:** Delhi NCR Housing Dataset 2025

**Source:**
https://www.kaggle.com/datasets/aabhas2351/delhi-ncr-housing-dataset-2025

**License:** CC0 1.0 (Public Domain)

---

# 🎯 Features Used

### Input Features

- Area (sq ft)
- Number of Bedrooms (BHK)
- Parking Spaces

### Target Variable

- House Price

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Joblib
- Streamlit

---

# 📊 Exploratory Data Analysis

Performed extensive EDA using:

- Correlation Heatmap
- Area vs Price
- BHK vs Price
- Parking vs Price

---

# 📷 EDA Visualizations

## Correlation Heatmap

![Correlation Heatmap](outputs/plots/correlation_heatmap.png)

---

## Area vs Price

![Area vs Price](outputs/plots/area_vs_price.png)

---

## BHK vs Price

![BHK vs Price](outputs/plots/bhk_vs_price.png)

---

## Parking vs Price

![Parking vs Price](outputs/plots/parking_vs_price.png)

---

# 🤖 Machine Learning Models

## 1️⃣ Linear Regression

Used as the baseline regression model.

### Evaluation Metrics

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

### Visualizations

#### Actual vs Predicted

![Actual vs Predicted LR](outputs/plots/actual_vs_predicted_lr.png)

#### Residual Plot

![Residual Plot LR](outputs/plots/residual_plot_lr.png)

---

## 2️⃣ Decision Tree Regression

Implemented Decision Tree Regression to capture non-linear relationships in housing prices.

### Hyperparameter Tuning

Compared multiple tree depths and selected the best-performing model.

Best parameter:

```text
max_depth = 5
```

### Evaluation Metrics

- MAE
- RMSE
- R² Score

### Visualizations

#### Actual vs Predicted

![Actual vs Predicted DT](outputs/plots/actual_vs_predicted_dt.png)

#### Residual Plot

![Residual Plot DT](outputs/plots/residual_plot_dt.png)

---

# 🌐 Streamlit Frontend

A simple interactive web application was built using Streamlit.

Users can enter:

- Area
- BHK
- Parking Spaces

and instantly receive an estimated property price.

## Home Page

![Home](outputs/screenshots/home.png)

---

## Prediction Example

![Prediction](outputs/screenshots/prediction.png)

---

## Another Prediction Example

![Prediction 2](outputs/screenshots/prediction2.png)

---

# 📁 Project Structure

```text
Delhi NCR House Price Prediction/

│
├── app.py
├── README.md
├── LICENSE
├── requirements.txt
│
├── data/
│
├── models/
│   ├── linear_regression_model.pkl
│   └── decision_tree_model.pkl
│
├── notebooks/
│   ├── 01_EDA_Linear_Regression.ipynb
│   └── 02_Decision_Tree.ipynb
│
├── outputs/
│   ├── plots/
│   ├── predictions/
│   └── screenshots/
│
└── .gitignore
```

---

# 🚀 How to Run

Clone the repository

```bash
git clone https://github.com/tejassainids/delhi-ncr-house-price-prediction.git
```

Move into the project

```bash
cd delhi-ncr-house-price-prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 📚 Learning Outcomes

This project helped reinforce:

- Exploratory Data Analysis
- Feature Selection
- Linear Regression
- Decision Tree Regression
- Hyperparameter Tuning
- MAE, MSE, RMSE and R²
- Residual Analysis
- Saving & Loading ML Models
- Streamlit Deployment
- Git & GitHub Workflow

---

# 💡 Future Improvements

- Random Forest Regression
- XGBoost
- Feature Importance
- Cross Validation
- Model Comparison Dashboard
- Cloud Deployment

---

# 👨‍💻 Author

**Tejas Saini**

B.Tech Data Science Student

GitHub:
https://github.com/tejassainids

---
