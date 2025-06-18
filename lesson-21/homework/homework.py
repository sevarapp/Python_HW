import pandas as pd
import matplotlib.pyplot as plt

# Creating the DataFrame
data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}
df1 = pd.DataFrame(data1)

# Exercise 1: Calculate average grade for each student
df1['Average'] = (df1['Math'] + df1['English'] + df1['Science']) / 3

# Exercise 2: Find student with the highest average grade
highest_avg = df1['Average'][0]
top_student_index = 0
for i in range(len(df1)):
    if df1['Average'][i] > highest_avg:
        highest_avg = df1['Average'][i]
        top_student_index = i
top_student = df1.loc[top_student_index]

# Exercise 3: Create a new column 'Total'
df1['Total'] = df1['Math'] + df1['English'] + df1['Science']

# Exercise 4: Bar chart of average grades in each subject
math_avg = df1['Math'].mean()
english_avg = df1['English'].mean()
science_avg = df1['Science'].mean()

plt.bar(['Math', 'English', 'Science'], [math_avg, english_avg, science_avg], color='lightgreen')
plt.title('Average Grade in Each Subject')
plt.ylabel('Average Grade')
plt.show()


# Creating the DataFrame
data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}
df2 = pd.DataFrame(data2)

# Exercise 1: Total sales for each product
total_A = sum(df2['Product_A'])
total_B = sum(df2['Product_B'])
total_C = sum(df2['Product_C'])

# Exercise 2: Find date with highest total sales
df2['Total_Sales'] = df2['Product_A'] + df2['Product_B'] + df2['Product_C']

max_total = df2['Total_Sales'][0]
max_index = 0
for i in range(len(df2)):
    if df2['Total_Sales'][i] > max_total:
        max_total = df2['Total_Sales'][i]
        max_index = i
max_sales_date = df2['Date'][max_index]

# Exercise 3: Percentage change from previous day (manual way)
df2['Product_A_Change'] = [None]
df2['Product_B_Change'] = [None]
df2['Product_C_Change'] = [None]

for i in range(1, len(df2)):
    df2.loc[i, 'Product_A_Change'] = round((df2.loc[i, 'Product_A'] - df2.loc[i-1, 'Product_A']) / df2.loc[i-1, 'Product_A'] * 100, 2)
    df2.loc[i, 'Product_B_Change'] = round((df2.loc[i, 'Product_B'] - df2.loc[i-1, 'Product_B']) / df2.loc[i-1, 'Product_B'] * 100, 2)
    df2.loc[i, 'Product_C_Change'] = round((df2.loc[i, 'Product_C'] - df2.loc[i-1, 'Product_C']) / df2.loc[i-1, 'Product_C'] * 100, 2)

# Exercise 4: Line chart of sales
plt.plot(df2['Date'], df2['Product_A'], label='Product A')
plt.plot(df2['Date'], df2['Product_B'], label='Product B')
plt.plot(df2['Date'], df2['Product_C'], label='Product C')
plt.title('Sales Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Creating the DataFrame
data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}
df3 = pd.DataFrame(data3)

# Exercise 1: Average salary for each department (manual way)
departments = list(set(df3['Department']))
for dept in departments:
    salaries = []
    for i in range(len(df3)):
        if df3['Department'][i] == dept:
            salaries.append(df3['Salary'][i])
    print(f"Average salary in {dept}: {sum(salaries) / len(salaries)}")

# Exercise 2: Most experienced employee
max_exp = df3['Experience (Years)'][0]
exp_index = 0
for i in range(len(df3)):
    if df3['Experience (Years)'][i] > max_exp:
        max_exp = df3['Experience (Years)'][i]
        exp_index = i
most_experienced = df3.loc[exp_index]

# Exercise 3: Salary increase from min salary
min_salary = df3['Salary'].min()
df3['Salary Increase (%)'] = round((df3['Salary'] - min_salary) / min_salary * 100, 2)

# Exercise 4: Bar chart - number of employees per department
department_counts = {}
for dept in df3['Department']:
    if dept not in department_counts:
        department_counts[dept] = 1
    else:
        department_counts[dept] += 1

plt.bar(department_counts.keys(), department_counts.values(), color='lightblue')
plt.title('Employees per Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.show()
# Creating the DataFrame
data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}
df4 = pd.DataFrame(data4)

# Exercise 1: Total revenue
total_revenue = sum(df4['Total_Price'])

# Exercise 2: Most ordered product
product_counts = {'A': 0, 'B': 0, 'C': 0}
for product in df4['Product']:
    product_counts[product] += 1

most_ordered = max(product_counts, key=product_counts.get)

# Exercise 3: Average quantity
average_quantity = sum(df4['Quantity']) / len(df4)

# Exercise 4: Pie chart - product sales distribution
product_sales = {'A': 0, 'B': 0, 'C': 0}
for i in range(len(df4)):
    product = df4['Product'][i]
    price = df4['Total_Price'][i]
    product_sales[product] += price

plt.pie(product_sales.values(), labels=product_sales.keys(), autopct='%1.1f%%', startangle=90)
plt.title('Sales Distribution by Product')
plt.axis('equal')
plt.show()

