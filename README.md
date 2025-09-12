# Logistics-Fulfillment-Optimization-Dashboard
# 🚚 Logistics & Fulfillment Optimization Dashboard

### 📌 Overview
This project analyzes logistics performance using order-level data to uncover bottlenecks in delivery, cancellations, and delays. It includes:
- A **Python analysis script** for deep-dive insights.
- A **Streamlit dashboard** for visualization.

---

### 📊 Dataset
`fulfillment.csv` contains sample order data:
| order_id | city       | delivery_days | on_time | cancelled |
|----------|-----------|---------------|---------|-----------|
| O1       | Bangalore | 3             | 1       | 0 |
| O2       | Delhi     | 6             | 0       | 0 |
| O3       | Mumbai    | 4             | 1       | 0 |

---

### 🖥️ Dashboard Features
- KPI cards (Avg Delivery Days, On-time %, Cancellation %)
- Histogram of delivery timelines
- Top delayed cities (bar chart)

---

### ⚙️ How to Run
1. Clone the repo:
   ```bash
   git clone <your-repo-url>
   cd meesho-fulfillment-dashboard
