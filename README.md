# 🛒 GMart Retail Sales Analytics

> End-to-end retail sales analytics project analyzing GMart transaction data using Python, MySQL, and Matplotlib. Covers data cleaning, EDA, outlier detection, database integration, and interactive dashboard visualization.

---

## 📌 Overview

This project performs comprehensive analysis on GMart's retail sales dataset to uncover revenue trends, customer behavior, store performance, and discount impact. The analysis is backed by SQL queries via MySQL integration and visualized through a multi-chart dashboard.

---

## 🛠️ Tech Stack

| Tool | Usage |
|------|-------|
| Python (Pandas, NumPy) | Data cleaning, EDA, transformation |
| Matplotlib | Dashboard visualizations |
| MySQL + SQLAlchemy | Database integration & SQL queries |
| python-dotenv | Secure credential management |

---

## ✨ Key Features

- 🧹 **Data Cleaning** — Null removal, deduplication, outlier filtering, feature engineering
- 📊 **EDA** — Monthly/quarterly trends, store & category analysis, city-wise performance
- 🏙️ **Metro vs Non-Metro Analysis** — Comparative revenue breakdown
- 💳 **Payment Mode Analysis** — Distribution across payment channels
- 👥 **Customer Analysis** — Top spenders, Pareto principle validation
- 💰 **Discount Impact Analysis** — Effect of discount % on average sales
- 🗄️ **MySQL Integration** — Data loaded to DB, SQL queries executed via SQLAlchemy
- 📈 **Visual Dashboard** — 6-chart analytics dashboard saved as PNG
- 🔍 **Outlier Detection** — IQR-based anomaly identification

---

## 📊 Dashboard Visualizations

1. Monthly Sales Trend (Line Chart)
2. Category-wise Revenue (Bar Chart)
3. City-wise Revenue (Bar Chart)
4. Average Sales by Discount % (Bar Chart)
5. Customer Spending Distribution (Histogram)
6. Payment Mode Distribution (Pie Chart)

---

## 💡 Key Insights

- Top product category contributes highest revenue share
- Metro cities (Mumbai, Delhi, Bangalore) outperform non-metro stores
- High discounts (15–20%) negatively impact overall profitability
- Top 20% customers generate majority of total revenue (Pareto Principle)
- A few store IDs consistently underperform across months

---

## 📁 Project Structure

```
gmart-retail-sales-analytics/
│
├── gmart_analysis.py       # Main analysis script
├── Gmart_sales_data.csv    # Dataset (not included — add locally)
├── .env.example            # Environment variable template
├── .gitignore              # Excludes .env and sensitive files
├── requirements.txt        # Dependencies
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/srinagadivyac-gmailcom/gmart-retail-sales-analytics
cd gmart-retail-sales-analytics
```

### 2. Install Dependencies
```bash
pip install pandas matplotlib sqlalchemy mysql-connector-python python-dotenv
```

### 3. Configure Environment Variables
```bash
cp .env.example .env
# Edit .env with your MySQL credentials
```

### 4. Add Dataset
Place `Gmart_sales_data.csv` in the project root folder.

### 5. Run the Analysis
```bash
python gmart_analysis.py
```

---

## 🔒 Security Notes

- Database credentials stored in `.env` file (never committed to GitHub)
- `.gitignore` excludes `.env` and sensitive files
- Use `.env.example` as setup template

---

## 👩‍💻 Author

**Srinaga Divya Chunchula**  
Data Analyst | Python | SQL | Power BI  
📧 srinagadivyac@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/sri-naga-divya-chunchula-955b56288)  
🐙 [GitHub](https://github.com/srinagadivyac-gmailcom)
