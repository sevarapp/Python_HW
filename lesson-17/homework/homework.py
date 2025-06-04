# Homework 1:
import numpy as np
import pandas as pd
data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
print(df)
# 1. Rename column names using function. "First Name" --> "first_name", "Age" --> "age
df.columns = df.columns.str.lower().str.replace(" ", "_")
# 2. Print the first 3 rows of the DataFrame
print(df.head(3))
# 3. Find the mean age of the individuals
print(df['age'].mean())
# 4. Select and print only the 'Name' and 'City' columns
print(df[['first_name','city']])
# 5. Add a new column 'Salary' with random salary values
df['salary'] = np.random.randint(50000, 100000, size=len(df))
print(df)
# 6. Display summary statistics of the DataFrame
print(df.describe())

# Homework 2:
# 1. Create a DataFrame named sales_and_expenses with columns 'Month', 'Sales', and 'Expenses', representing monthly sales and expenses data.
# Use below table.
data={
    'Month':['Jan','Feb','Mar','Apr'],
    'Sales':[5000,6000,7500,8000],
    'Expenses':[3000,3500,4000,4500]
}
sales_and_expenses=pd.DataFrame(data)
print(sales_and_expenses)
# | Month | Sales | Expenses |
# |-------|-------|----------|
# | Jan   | 5000  | 3000     |
# | Feb   | 6000  | 3500     |
# | Mar   | 7500  | 4000     |
# | Apr   | 8000  | 4500     |


# 2. Calculate and display the maximum sales and expenses.
print('Max sales is ' ,sales_and_expenses['Sales'].max())
print('Max expenses is ',sales_and_expenses['Expenses'].max())

# 3. Calculate and display the minimum sales and expenses.
print('Min sales is ' ,sales_and_expenses['Sales'].min())
print('Min expenses is ',sales_and_expenses['Expenses'].min())
# 4. Calculate and display the average sales and expenses.
print('Average sales is ' ,sales_and_expenses['Sales'].mean())
print('Average expenses is ',sales_and_expenses['Expenses'].mean())


# Homework 3:

# 1. Create a DataFrame named expenses with columns 'Category', 'January', 'February', 'March', and 'April', representing monthly expenses for different categories. Use below table.
data1={
    'Category':['Rent','utilities','groceries','entertainment'],
    'January':[1200,200,300,150],
    'February':[1300,220,320,160],
    'March':[1400,240,330,170],
    'April':[1500,250,350,180]
    }
expenses=pd.DataFrame(data1)
print(expenses)
# | Category       | January | February | March | April |
# |----------------|---------|----------|-------|-------|
# | Rent           | 1200    | 1300     | 1400  | 1500  |
# | Utilities      | 200     | 220      | 240   | 250   |
# | Groceries      | 300     | 320      | 330   | 350   |
# | Entertainment  | 150     | 160      | 170   | 180   |


# 2. Calculate and display the maximum expense for each category.
expenses = expenses.set_index('Category')
print('max per',expenses.max(axis=1))
# 3. Calculate and display the minimum expense for each category.
print('minimum per ',expenses.min(axis=1))
# 4. Calculate and display the average expense for each category.
print(expenses.mean(axis=1))

