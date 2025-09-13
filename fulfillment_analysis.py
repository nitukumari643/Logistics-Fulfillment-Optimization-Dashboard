import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/fulfillment.csv")

# Basic KPIs
print("Average Delivery Time:", round(df['delivery_days'].mean(), 2))
print("On-time Delivery %:", round(df['on_time'].mean() * 100, 2))
print("Cancellation Rate %:", round(df['cancelled'].mean() * 100, 2))

# Cities with highest delays
delay_city = df[df['on_time'] == 0].groupby('city').size().sort_values(ascending=False)
print("\nTop Cities with Delays:")
print(delay_city.head())

# Visualization: Delivery distribution
plt.figure(figsize=(6,4))
sns.histplot(df['delivery_days'], bins=10, kde=True, color="skyblue")
plt.title("Delivery Time Distribution")
plt.xlabel("Delivery Days")
plt.show()

# Visualization: Top 5 delayed cities
plt.figure(figsize=(6,4))
sns.barplot(x=delay_city.index[:5], y=delay_city.values[:5], palette="Reds_r")
plt.title("Top 5 Cities with Delayed Orders")
plt.xlabel("City")
plt.ylabel("Delayed Orders")
plt.show()
