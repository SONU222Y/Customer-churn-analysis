# 📊 Telco Customer Churn Analysis & Prediction System

An end-to-end data analytics and machine learning project that predicts customer churn and provides business insights using SQL, Python, and Power BI.

---

## 🚀 Project Overview

This project analyzes telecom customer data to identify churn patterns, predict customer behavior, and estimate business risk.

The workflow includes:

* Data Cleaning using SQL
* Data Processing & Machine Learning using Python
* Dashboard Visualization using Power BI

---

## 📸 Screenshots

### 📊 Power BI Dashboard

![images](Dashboard.png)

### 📉 Churn Analysis

![images](Churn_distribution.png)

### 💰 Revenue at Risk

![images](Revenue_at_Risk.png)

### 💰 Segment Level Analysis

![images](Segment_Level_Analysis.png)
---

## 🧠 Key Features

✔ Customer Churn Prediction (Logistic Regression)
✔ Customer Lifetime Value (CLV) Calculation
✔ Revenue at Risk Identification
✔ Customer Segmentation (High / Medium / Low Value)
✔ End-to-End Pipeline (SQL → Python → Power BI)
✔ Business Insights for Decision Making

---

## ⚙️ Tech Stack

* Python (Pandas, NumPy, Scikit-learn)
* MySQL (Database & Data Cleaning)
* SQLAlchemy (Database Connection)
* Power BI (Dashboard Visualization)

---

## 💡 How It Works

### 🔹 Step 1: Data Collection

* Dataset: Telco Customer Churn (Kaggle)

### 🔹 Step 2: Data Cleaning (SQL)

* Created structured database
* Cleaned and formatted raw data

### 🔹 Step 3: Data Processing (Python)

* Converted data types
* Handled missing values
* Feature engineering:

  * Customer Lifetime Value (CLV)
  * Revenue at Risk

### 🔹 Step 4: Machine Learning

* Model: Logistic Regression
* Features:

  * Tenure
  * Monthly Charges
  * Total Charges
* Output:

  * Churn Prediction
  * Churn Probability

### 🔹 Step 5: Data Export

* Generated:

```bash
churn_powerbi.csv
```

### 🔹 Step 6: Visualization (Power BI)

* Interactive dashboard with:

  * Churn distribution
  * Customer segmentation
  * Revenue risk analysis

---

## 📊 Business Insights

* Customers with **low tenure** have higher churn risk
* Higher **monthly charges** increase churn probability
* High-value customers contribute most to **revenue loss risk**
* Segmentation helps in targeted retention strategies

---

## 📊 ML & Business Logic

* Logistic Regression for classification

* StandardScaler for feature normalization

* Train-Test Split for model validation

* CLV Calculation:

```bash
CLV = MonthlyCharges × Tenure
```

* Revenue at Risk:

```bash
Revenue at Risk = CLV × Churn
```

---

## 📂 Project Structure

```bash
.
├── Telco-Customer-Churn.csv   # Original dataset
├── churn_database.sql         # SQL cleaning & database setup
├── app.py                     # Python (ML + feature engineering)
├── churn_powerbi.csv          # Output dataset for Power BI
├── churn_powerbi.pbix         # Power BI dashboard
└── README.md                  # Documentation
```

> Note: This project uses a flat structure for simplicity and easy understanding.

---

## ▶️ How to Run the Project

### Step 1: Clone Repository

```bash
git clone https://github.com/your-username/telco-customer-churn-analysis.git
cd telco-customer-churn-analysis
```

### Step 2: Install Dependencies

```bash
pip install pandas numpy sqlalchemy pymysql scikit-learn
```

### Step 3: Setup MySQL

* Create database:

```sql
CREATE DATABASE customer_churn;
```

* Run SQL file:

```bash
churn_database.sql
```

### Step 4: Update Database Connection

Edit in `app.py`:

```bash
mysql+pymysql://username:password@localhost/customer_churn
```

### Step 5: Run Python Script

```bash
python app.py
```

### Step 6: Open Power BI

* Open file:

```bash
churn_powerbi.pbix
```

---

## 🔮 Future Improvements

* Add advanced models (Random Forest, XGBoost)
* Convert into Streamlit Web App
* Deploy model for real-time predictions

---

## 👨‍💻 Author

Amit Garje
