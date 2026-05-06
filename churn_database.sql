CREATE DATABASE customer_churn;
USE customer_churn;

CREATE TABLE customers (
    customerID VARCHAR(50),
    gender VARCHAR(10),
    SeniorCitizen INT,
    Partner VARCHAR(10),
    Dependents VARCHAR(10),
    tenure INT,
    PhoneService VARCHAR(10),
    MultipleLines VARCHAR(30),
    InternetService VARCHAR(30),
    OnlineSecurity VARCHAR(30),
    OnlineBackup VARCHAR(30),
    DeviceProtection VARCHAR(30),
    TechSupport VARCHAR(30),
    StreamingTV VARCHAR(30),
    StreamingMovies VARCHAR(30),
    Contract VARCHAR(30),
    PaperlessBilling VARCHAR(10),
    PaymentMethod VARCHAR(50),
    MonthlyCharges FLOAT,
    TotalCharges FLOAT,
    Churn VARCHAR(10)
);

SELECT *
FROM customers
WHERE TotalCharges IS NULL OR TotalCharges = '';

UPDATE customers
SET TotalCharges = MonthlyCharges * tenure
WHERE TotalCharges IS NULL OR TotalCharges = '';

ALTER TABLE customers
ADD COLUMN ChurnFlag INT;

UPDATE customers
SET ChurnFlag = CASE
    WHEN Churn = 'Yes' THEN 1
    ELSE 0
END;

SELECT customerID, tenure, MonthlyCharges, TotalCharges, ChurnFlag
FROM customers
LIMIT 10;




