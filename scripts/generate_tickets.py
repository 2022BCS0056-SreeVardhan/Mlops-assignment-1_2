import os
import pandas as pd
import random
from datetime import datetime, timedelta

# Get the directory where the script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Define absolute paths relative to the script's location
customers_path = os.path.join(SCRIPT_DIR, "../data/processed/customers.csv")
tickets_path = os.path.join(SCRIPT_DIR, "../data/processed/tickets.csv")

customers = pd.read_csv(customers_path)

complaint_types = ["complaint"]
other_types = ["technical","billing","service_request","general"]

tickets = []

for _, row in customers.iterrows():

    cid = row["customer_id"]
    churn = row["Churn"]

    if churn == "Yes":
        ticket_count = random.randint(4,10)
        complaint_prob = 0.5
        negative_prob = 0.6
    else:
        ticket_count = random.randint(0,3)
        complaint_prob = 0.1
        negative_prob = 0.2

    for _ in range(ticket_count):

        if random.random() < complaint_prob:
            ticket_type = "complaint"
        else:
            ticket_type = random.choice(other_types)

        if random.random() < negative_prob:
            sentiment = "negative"
        else:
            sentiment = random.choice(["neutral","positive"])

        ticket = {
            "ticket_id": f"T{random.randint(10000,99999)}",
            "customer_id": cid,
            "ticket_type": ticket_type,
            "sentiment": sentiment,
            "created_at": datetime.now() - timedelta(days=random.randint(1,90))
        }

        tickets.append(ticket)

tickets_df = pd.DataFrame(tickets)

tickets_df.to_csv(tickets_path, index=False)
