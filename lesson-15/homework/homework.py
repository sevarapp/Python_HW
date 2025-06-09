# roster_db.py
import sqlite3

# Connect to a new database (or create it)
conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

# Step 1: Create the Roster table
cursor.execute("DROP TABLE IF EXISTS Roster")  # optional: clean start
cursor.execute("""
CREATE TABLE Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

# Step 2: Insert values
roster_data = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]
cursor.executemany("INSERT INTO Roster VALUES (?, ?, ?)", roster_data)

# Step 3: Update Jadzia Dax to Ezri Dax
cursor.execute("""
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
""")

# Step 4: Query and display Name and Age of Bajorans
cursor.execute("""
SELECT Name, Age FROM Roster
WHERE Species = 'Bajoran'
""")
results = cursor.fetchall()

print("\n--- Bajoran Members ---")
for name, age in results:
    print(f"Name: {name}, Age: {age}")

# Finalize changes
conn.commit()
conn.close()
