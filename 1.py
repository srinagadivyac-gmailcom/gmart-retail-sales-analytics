import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

def load_sales_data():

    df = pd.read_csv(r"C:\Users\Lenovo\Downloads\Gmart_sales_data.csv")
    
    return df

def clean_data(df):

    print("=== Data Cleaning & Preprocessing ===")

    df['order_date'] = pd.to_datetime(df['order_date'], format="mixed", dayfirst=True)

    df = df.dropna()

    df = df.drop_duplicates()

    df = df[(df['discount_pct'] >= 0) & (df['discount_pct'] <= 100)]

    df['Month'] = df['order_date'].dt.month
    df['Quarter'] = df['order_date'].dt.quarter
    df['Year'] = df['order_date'].dt.year

    df = df[df['quantity'] > 0]
    df = df[df['unit_price'] > 0]
    df = df[df['total_amount'] > 0]

    original_records = len(df)
    print(f"Original records: {original_records}")
    print(f"Cleaned records: {len(df)}")
    print(f"Data shape: {df.shape}")

    return df

def eda(df):

    print("\nBasic Statistics:")
    print(df[['unit_price', 'quantity', 'discount_pct', 'total_amount']].describe())

    df['order_date'] = pd.to_datetime(df['order_date'], format="mixed", dayfirst=True)
    df['Month'] = df['order_date'].dt.month
    df['Quarter'] = df['order_date'].dt.quarter
    df['Year'] = df['order_date'].dt.year

    # Sales Trend Analysis
    print("\n=== Sales Trend Analysis ===")
    monthly_sales = df.groupby(['Year','Month'])['total_amount'].sum()
    monthly_sale = df.groupby('Month')['total_amount'].sum()
    quarterly_sales = df.groupby('Quarter')['total_amount'].sum()

    print("Monthly Sales:")
    print(monthly_sales)
    print("\nQuarterly Sales:")
    print(quarterly_sales)

    # store-wise Revenue Analysis
    print("\n=== Store-wise Performance ===")
    store_revenue = df.groupby('store_id')['total_amount'].sum().sort_values(ascending=False)
    print(f"Top 5 Stores by Revenue:")
    print(store_revenue.head(5) ) 
    print(f"Bottom 5 Stores by Revenue:")
    print(store_revenue.tail(5) )
   
    # Category-wise Revenue Analysis
    print("\n=== Category-wise Revenue Analysis ===")
    category_revenue = df.groupby('category')['total_amount'].sum().sort_values(ascending=False)
    print("\nRevenue by Category:")
    print(category_revenue)

    # City-wise Performance
    print("\n=== City-wise Performance ===")
    city_revenue = df.groupby('city')['total_amount'].sum().sort_values(ascending=False)
    print("Revenue by City:")
    print(city_revenue)

    # City-wise Performance (metro vs non metro)
    metro_cities = ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Hyderabad' , 'Pune']

    df['city_type'] = df['city'].apply(lambda x: 'Metro' if x in metro_cities else 'Non-Metro')

    metro_analysis =df.groupby('city_type')['total_amount'].sum()
    print("\n=== MetroCity-wise Performance ===")
    print(metro_analysis)

    print("\n=== Payment Mode Contribution ===")
    Pmode = df.groupby('payment_mode')['total_amount'].sum()
    print(Pmode)
    

    # Customer Analysis
    print("\n=== Customer Analysis ===")
    customer_spending = df.groupby('customer_id')['total_amount'].sum().sort_values(ascending=False)
    print(f"Top 10 customers by spending:")
    print(customer_spending.head(10))

    print("\n=== Discoungt Impact on sales ===")
    print(df[df['discount_pct'] != 0].groupby('discount_pct')['total_amount'].mean())

    print("\n=== Category vs Discount Effect ===")
    discount_impact_category =df.groupby('category')['discount_pct'].mean()
    print(discount_impact_category)

    return monthly_sale, category_revenue, city_revenue,discount_impact_category, customer_spending

def create_visualizations(df, monthly_sales, category_revenue, city_revenue,discount_analysis,customer_spending ):
    print("\n=== Data Visualization ===")

    # Set up the plotting style
    plt.style.use('default')
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    fig.suptitle('GMart Retail Sales Analytics Dashboard', fontsize=16, fontweight='bold')

    # Monthly Sales Trend
    axes[0, 0].plot(monthly_sales.index, monthly_sales.values, marker='o', linewidth=2, markersize=6)
    axes[0, 0].set_title('Monthly Sales Trend', fontweight='bold')
    axes[0, 0].set_xlabel('Month')
    axes[0, 0].set_ylabel('Total Sales Amount (M)')
    axes[0, 0].grid(True, alpha=0.3)

    # Category-wise Revenue
    bars = axes[0, 1].bar(category_revenue.index, category_revenue.values, color='skyblue', alpha=0.8)
    axes[0, 1].set_title('Category-wise Revenue', fontweight='bold')
    axes[0, 1].set_xlabel('Category')
    axes[0, 1].set_ylabel('Revenue (M)')
    axes[0, 1].tick_params(axis='x', rotation=45)
    for bar in bars:
        height = bar.get_height()
        axes[0, 1].text(bar.get_x() + bar.get_width()/2., height + 500,
                       f'${height:,.0f}', ha='center', va='bottom', fontsize=8)

    # City-wise Revenue
    bars = axes[0, 2].bar(city_revenue.index, city_revenue.values, color='lightgreen', alpha=0.8)
    axes[0, 2].set_title('City-wise Revenue', fontweight='bold')
    axes[0, 2].set_xlabel('City')
    axes[0, 2].set_ylabel('Revenue (M)')
    axes[0, 2].tick_params(axis='x', rotation=45)
    for bar in bars:
        height = bar.get_height()
        axes[0, 2].text(bar.get_x() + bar.get_width()/2., height + 500,
                       f'${height:,.0f}', ha='center', va='bottom', fontsize=8)

    # Discount vs Revenue Analysis
    axes[1, 0].bar(discount_analysis.index.astype(str), discount_analysis.values, color='orange', alpha=0.8)
    axes[1, 0].set_title('Average Sales by Discount Percentage', fontweight='bold')
    axes[1, 0].set_xlabel('Discount Percentage')
    axes[1, 0].set_ylabel('Average Sales Amount')

    # Customer Spending Distribution
    axes[1, 1].hist(customer_spending.values, bins=30, color='purple', alpha=0.7, edgecolor='black')
    axes[1, 1].set_title('Customer Spending Distribution', fontweight='bold')
    axes[1, 1].set_xlabel('Total Spending')
    axes[1, 1].set_ylabel('Number of Customers')
    axes[1, 1].axvline(customer_spending.mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: ${customer_spending.mean():.0f}')
    axes[1, 1].legend()

    # Payment Mode Distribution
    payment_dist = df['payment_mode'].value_counts()
    axes[1, 2].pie(payment_dist.values, labels=payment_dist.index, autopct='%1.1f%%', startangle=90)
    axes[1, 2].set_title('Payment Mode Distribution', fontweight='bold')

    plt.tight_layout()
    plt.savefig('gmart_sales_analytics.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("Dashboard saved as 'gmart_sales_analytics.png'")

def database_integration(df):
    print("\n=== Database Integration ===")

    # ---- SQLAlchemy Engine ----
    engine = create_engine(
        "mysql+mysqlconnector://root:Nagadivya%401212@localhost/dataanalysisproject"
    )

    # Load Data
    df.to_sql(
        name="transactions",
        con=engine,
        if_exists="replace",
        index=False
    )

    print("Data loaded into MySQL successfully.")

    # SQL Queries
    queries = {
        "Store-wise Revenue": """
            SELECT store_id, SUM(total_amount) AS revenue
            FROM transactions
            GROUP BY store_id
            ORDER BY revenue DESC;
        """,

        "Top Customers": """
            SELECT customer_id, SUM(total_amount) AS total_spent
            FROM transactions
            GROUP BY customer_id
            ORDER BY total_spent DESC
            LIMIT 10;
        """,

        "Monthly Sales": """
            SELECT 
                YEAR(order_date) AS year,
                MONTH(order_date) AS month,
                SUM(total_amount) AS monthly_revenue
            FROM transactions
            GROUP BY YEAR(order_date), MONTH(order_date)
            ORDER BY year, month;
        """
    }

    for title, query in queries.items():
        print(f"\n{title}:")
        result = pd.read_sql_query(query, engine)
        print(result)


def generate_insights(df, category_revenue, city_revenue, customer_spending):
    
    print("\n=== Key Insights & Findings ===")

    total_revenue = df['total_amount'].sum()

    # Category Insight
    top_category = category_revenue.index[0]
    top_category_share = (category_revenue.iloc[0] / total_revenue) * 100

    print("\n Category contributes the highest revenue.")
    print(f" ->Category: {top_category}")
    print(f" ->evenue Share: {top_category_share:.2f}%")

    # City Insight
    top_city = city_revenue.index[0]
    top_city_revenue = city_revenue.iloc[0]

    print(f"\n GMart stores in {top_city} outperform other cities.")
    print(f" ->Revenue from {top_city}: {top_city_revenue:,.2f}")

    # Discount Insight
    high_discount_sales = df[df['discount_pct'] >= 15]['total_amount'].sum()
    high_discount_percentage = (high_discount_sales / total_revenue) * 100

    print(f"\n High discounts (15–20%) reduce overall profitability.")
    print(f" ->Revenue under high discounts: {high_discount_percentage:.2f}% of total sales")

    #Store Performance Insight
    store_revenue = df.groupby('store_id')['total_amount'].sum()
    underperforming_stores = store_revenue.sort_values().head(5).index.tolist()

    print(f"\n A few stores consistently underperform across months.")
    print(f" -> Underperforming Store IDs: {underperforming_stores}")

    #Customer Insight (Pareto Principle)
    top_20_percent = int(len(customer_spending) * 0.2)
    top_customers_revenue = customer_spending.head(top_20_percent).sum()
    pareto_percentage = (top_customers_revenue / total_revenue) * 100

    print(f"\n A small percentage of customers generate most of the revenue (Pareto Principle).")
    print(f" -> Top 20% customers contribute {pareto_percentage:.2f}% of total revenue")

    # Return insights (useful for reports / dashboards)
    # return {
    #     "total_revenue": total_revenue,
    #     "top_category": top_category,
    #     "top_category_share_pct": round(top_category_share, 2),
    #     "top_city": top_city,
    #     "high_discount_revenue_pct": round(high_discount_percentage, 2),
    #     "pareto_revenue_pct": round(pareto_percentage, 2),
    #     "underperforming_stores": underperforming_stores
    # }

def detect_outliers(df):
    print("\n=== Outlier Detection ===")

    Q1 = df['total_amount'].quantile(0.25)
    Q3 = df['total_amount'].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[
        (df['total_amount'] < lower_bound) |
        (df['total_amount'] > upper_bound)
    ]

    print(f"Total transactions: {len(df)}")
    print(f"Outlier transactions: {len(outliers)}")
    print(f"Outlier percentage: {(len(outliers)/len(df))*100:.2f}%")


def main():
    print("GMart Retail Sales Analytics Project")
    print("=" * 50)

    # Load data
    df = load_sales_data()

    # Clean data
    df_cleaned = clean_data(df)

    # EDA
    monthly_sales, category_revenue, city_revenue,discount_analysis, customer_spending = eda(df_cleaned)

    # Outlier Detection
    detect_outliers(df_cleaned)

    # Database Integration
    database_integration(df_cleaned)

    # Insights
    generate_insights(df_cleaned,category_revenue, city_revenue, customer_spending)

    #Dashboard
    create_visualizations(df_cleaned, monthly_sales, category_revenue, city_revenue,discount_analysis, customer_spending)

    # Business Recommendations pendings

    print("\n" + "=" * 50)

if __name__ == "__main__":
    main()