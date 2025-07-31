import sqlite3

# Create and connect to database
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Run schema
with open('schema.sql', 'r') as f:
    cursor.executescript(f.read())

# Run seed data
with open('seed_data.sql', 'r') as f:
    cursor.executescript(f.read())

conn.commit()
conn.close()
print("✅ Database created and populated.")