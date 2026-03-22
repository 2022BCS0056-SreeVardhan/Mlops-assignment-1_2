import os
import pandas as pd

# Get the directory where the script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Define absolute paths relative to the script's location
raw_data_path = os.path.join(SCRIPT_DIR, "../data/raw/telco_churn.csv")
processed_data_path = os.path.join(SCRIPT_DIR, "../data/processed/customers.csv")

df = pd.read_csv(raw_data_path)

# fix TotalCharges issue
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

df = df.dropna(subset=["TotalCharges"])

# rename important columns
df = df.rename(columns={
    "customerID": "customer_id",
    "Contract": "contract_type",
    "MonthlyCharges": "monthly_charges",
    "TotalCharges": "total_charges"
})

# keep useful columns
columns_to_keep = [
    "customer_id",
    "contract_type",
    "tenure",
    "monthly_charges",
    "total_charges",
    "PaymentMethod",
    "PaperlessBilling",
    "SeniorCitizen",
    "Churn"
]

df = df[columns_to_keep]

df.to_csv(processed_data_path, index=False)

print("customers dataset saved")
