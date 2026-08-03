# Data Science — Real World Application Code Examples
# 1. E-commerce: "Customers who bought this also bought" (Simple Recommendation)
import pandas as pd

# Sample purchase data
data = {
    "customer": ["A", "A", "B", "B", "C", "C", "D"],
    "product":  ["Shoes", "Socks", "Shoes", "Cap", "Socks", "Cap", "Shoes"]
}
df = pd.DataFrame(data)

# Find products bought together with "Shoes"
shoe_buyers = df[df["product"] == "Shoes"]["customer"]
related_purchases = df[df["customer"].isin(shoe_buyers) & (df["product"] != "Shoes")]

print("People who bought Shoes also bought:")
print(related_purchases["product"].value_counts())



## 2. Bank Fraud Detection (Simple Rule-Based Flagging)
import pandas as pd

transactions = pd.DataFrame({
    "customer": ["Ravi", "Ravi", "Ravi", "Meena"],
    "amount": [500, 800, 25000, 600],
    "location": ["Mangalore", "Mangalore", "Dubai", "Bangalore"]
})

# Flag unusually high transactions (simple threshold-based fraud check)
avg_spend = transactions.groupby("customer")["amount"].transform("mean")
transactions["flag"] = transactions["amount"] > (avg_spend * 3)
print(transactions)


## 3. Weather Prediction (Simple Linear Regression)
from sklearn.linear_model import LinearRegression
import numpy as np

# Days vs Temperature (sample historical data)
days = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
temperature = np.array([30, 31, 33, 34, 36])

model = LinearRegression()
model.fit(days, temperature)

# Predict temperature for day 6
predicted = model.predict([[6]])
print("Predicted temperature for day 6:", predicted[0])



## 4. Netflix-style Viewing Pattern Analysis (EDA Example)
import pandas as pd

viewing_data = pd.DataFrame({
    "user": ["A", "B", "C", "D", "E"],
    "genre": ["Comedy", "Thriller", "Comedy", "Drama", "Thriller"],
    "watch_time_min": [45, 90, 30, 120, 75],
    "day_type": ["Weekday", "Weekend", "Weekday", "Weekend", "Weekend"]
})

# Most popular genre
print("Most watched genre:")
print(viewing_data["genre"].value_counts())

# Average watch time by day type
print("\nAverage watch time by day type:")
print(viewing_data.groupby("day_type")["watch_time_min"].mean())


## 5. Ola/Uber Surge Pricing (Simple Demand-Based Pricing Logic)
import pandas as pd

demand_data = pd.DataFrame({
    "hour": [8, 9, 13, 18, 19, 22],
    "riders_waiting": [50, 80, 20, 90, 100, 30],
    "cars_available": [40, 35, 25, 30, 25, 40]
})

# Simple surge multiplier logic: more demand than supply -> price increases
demand_data["surge_multiplier"] = (
    demand_data["riders_waiting"] / demand_data["cars_available"]
).round(2)

print(demand_data)


## 6. Hospital Patient Data Cleaning (Data Wrangling Example)
import pandas as pd
import numpy as np

patients = pd.DataFrame({
    "name": ["Ravi", "Meena", "Anil", "Suma"],
    "age": [34, np.nan, 45, 29],
    "gender": ["Male", "female", "M", "Female"]
})

print("Before cleaning:")
print(patients)

# Standardize gender values
patients["gender"] = patients["gender"].str.lower().replace({"m": "male", "f": "female"})

# Fill missing age with average age
patients["age"] = patients["age"].fillna(patients["age"].mean())

print("\nAfter cleaning:")
print(patients)

