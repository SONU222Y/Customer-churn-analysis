import pandas as pd
import numpy as np
from sqlalchemy import create_engine

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


engine = create_engine(
    "mysql+pymysql://root:Root%40123@localhost/customer_churn"
)

query = "SELECT * FROM customers"
df = pd.read_sql(query, engine)


df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

df["TotalCharges"] = df["TotalCharges"].fillna(df["MonthlyCharges"] * df["tenure"])

df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})




features = [
    "tenure",
    "MonthlyCharges",
    "TotalCharges"
]

X = df[features].values
y = df["Churn"]
#print(X)

#from sklearn.model_selection import train_test_split
#from sklearn.preprocessing import StandardScaler
#from sklearn.linear_model import LogisticRegression

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)



scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

df["churn_probability"] = model.predict_proba(X)[:, 1]

#from sklearn.metrics import accuracy_score

print("Accuracy:", accuracy_score(y_test, y_pred))

#print (df["TotalCharges"].describe())
#df.info()
#print(df.head())

df["CLV"] = df["MonthlyCharges"] * df["tenure"]

df["revenue_at_risk"] = df["CLV"] * df["Churn"]


def segment(row):
    if row["CLV"] > df["CLV"].quantile(0.75):
        return "High Value"
    elif row["CLV"] > df["CLV"].quantile(0.40):
        return "Medium Value"
    else:
        return "Low Value"

df["segment"] = df.apply(segment, axis=1)


df.to_csv("churn_powerbi.csv", index=False)

