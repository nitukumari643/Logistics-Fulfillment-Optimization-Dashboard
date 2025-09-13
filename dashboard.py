import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/fulfillment.csv")

st.title("🚚 Logistics & Fulfillment Dashboard")

# KPIs
st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Avg Delivery Days", f"{df['delivery_days'].mean():.2f}")
col2.metric("On-time %", f"{(df['on_time'].mean()*100):.1f}%")
col3.metric("Cancellation %", f"{(df['cancelled'].mean()*100):.1f}%")

# Delivery Time Distribution
st.subheader("Delivery Time Distribution")
fig, ax = plt.subplots()
sns.histplot(df['delivery_days'], bins=10, kde=True, color="skyblue", ax=ax)
st.pyplot(fig)

# Top Cities with Delays
st.subheader("Top Delayed Cities")
delays = df[df['on_time'] == 0].groupby('city').size().sort_values(ascending=False)
st.bar_chart(delays.head(5))
