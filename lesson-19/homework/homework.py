import pandas as pd

# Load the dataset
df = pd.read_csv('task/customer_orders.csv')  # Adjust path if needed

# Task 1: Filter customers with at least 20 orders
order_counts = df.groupby('CustomerID').size()
customers_20_plus_orders = order_counts[order_counts >= 20].index
filtered_customers = df[df['CustomerID'].isin(customers_20_plus_orders)]

# Task 2: Identify customers with average price per unit > $120
avg_price_per_customer = df.groupby('CustomerID')['Price'].mean()
customers_avg_price_gt_120 = avg_price_per_customer[avg_price_per_customer > 120].index
high_avg_price_customers = df[df['CustomerID'].isin(customers_avg_price_gt_120)]

# Task 3: Total quantity and price per product, filter products with total quantity < 5
product_totals = df.groupby('Product').agg(
    Total_Quantity=('Quantity', 'sum'),
    Total_Price=('Price', 'sum')
)
filtered_products = product_totals[product_totals['Total_Quantity'] >= 5]

# Optional: Save results to CSV files
filtered_customers.to_csv('customers_with_20_or_more_orders.csv', index=False)
high_avg_price_customers.to_csv('customers_avg_price_gt_120.csv', index=False)
filtered_products.to_csv('products_with_quantity_gte_5.csv')

# Display outputs (optional)
print("Customers with >= 20 orders:\n", filtered_customers.head())
print("\nCustomers with avg price > $120:\n", high_avg_price_customers.head())
print("\nProducts with total quantity >= 5:\n", filtered_products)

