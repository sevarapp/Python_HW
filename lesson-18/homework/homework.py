# 1. Female Passengers in Class 1 with Ages between 20 and 30
female_class1_20_30 = df[
    (df['Sex'] == 'female') & 
    (df['Pclass'] == 1) & 
    (df['Age'].between(20, 30))
]

# 2. Passengers Who Paid More than $100
fare_above_100 = df[df['Fare'] > 100]

# 3. Passengers Who Survived and Were Alone (SibSp == 0 and Parch == 0)
survived_alone = df[
    (df['Survived'] == 1) & 
    (df['SibSp'] == 0) & 
    (df['Parch'] == 0)
]

# 4. Passengers Embarked from 'C' and Paid More Than $50
embarked_c_fare_above_50 = df[
    (df['Embarked'] == 'C') & 
    (df['Fare'] > 50)
]

# 5. Passengers with Siblings or Spouses AND Parents or Children
siblings_parents = df[
    (df['SibSp'] > 0) & 
    (df['Parch'] > 0)
]

# 6. Passengers Aged 15 or Younger Who Didn't Survive
age_15_under_didnt_survive = df[
    (df['Age'] <= 15) & 
    (df['Survived'] == 0)
]

# 7. Passengers with Cabins and Fare Greater Than $200
cabin_and_fare_above_200 = df[
    df['Cabin'].notna() & 
    (df['Fare'] > 200)
]

# 8. Passengers with Odd-Numbered Passenger IDs
odd_passenger_ids = df[df['PassengerId'] % 2 == 1]

# 9. Passengers with Unique Ticket Numbers
unique_ticket_numbers = df[
    ~df.duplicated('Ticket', keep=False)
]

# 10. Female Passengers with 'Miss' in Their Name and Were in Class 1
miss_in_name_class1 = df[
    df['Name'].str.contains('Miss') & 
    (df['Sex'] == 'female') & 
    (df['Pclass'] == 1)
]

# Optional: display sample results
print(female_class1_20_30.head())

