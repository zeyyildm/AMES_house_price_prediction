# 🏡 House Price Prediction Project

This project focuses on predicting house prices using three different machine learning models:

- **Linear Regression**
- **Random Forest Regressor**
- **XGBoost Regressor**

The dataset used is the **Ames Housing Dataset**, which contains detailed information about residential properties.

---

## 📌 Project Workflow

### 1️⃣ Data Cleaning
- Missing values handled for both numeric & categorical columns  
- Outliers visualized  
- Data types corrected  
- Cleaned dataset exported for modeling  

---

### 2️⃣ Feature Preparation
- Split into **X (features)** and **y (SalePrice)**  
- Train / test split  
- Scaling applied to numerical columns using **StandardScaler**  
- Categorical columns encoded using **OneHotEncoder**  
- Final dataset created by combining scaled + encoded features  

---

### 3️⃣ Models Trained
The following models were trained and evaluated:

- ✅ **Linear Regression**  
  Baseline model for comparison.

- 🌲 **Random Forest Regressor**  
  Tree-based ensemble model, performs well on nonlinear data.

- ⚡ **XGBoost Regressor**  
  Boosting-based algorithm offering strong predictive power.

---

## 📊 Evaluation Metrics
Each model was evaluated using:

- **R² Score**
- **MAE (Mean Absolute Error)**
- **MSE (Mean Squared Error)**
- **RMSE (Root Mean Squared Error)**

A comparison table and bar charts were generated to visualize model performance.

---

## 📈 Results Summary
- **XGBoost and Random Forest** performed significantly better than **Linear Regression**
- **XGBoost achieved the best overall metrics**
- **Linear Regression** provided a good baseline but was not sufficient for non-linear relationships

---

## 🚀 Technologies Used
- **Python**
- **Pandas, NumPy**
- **Scikit-learn**
- **XGBoost**
- **Matplotlib, Seaborn**

