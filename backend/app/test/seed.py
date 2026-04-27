# Seed Data for Testing
from database import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS fasteners (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL,
    location TEXT,
    category TEXT
)
""")

cursor.execute("""
INSERT OR IGNORE INTO fasteners (code, description, location, category)
VALUES 
('ABC', 'Hex bolt, zinc plated, 1/4 in x 2 in', 'Bay 12, Drawer 4', 'Bolt'),
('DEF', 'Wood screw, #8 x 1-1/2 in', 'Bay 14, Drawer 2', 'Screw'),
('GHI', 'Machine screw, stainless steel, #10-24 x 1 in', 'Bay 13, Drawer 6', 'Screw')
""")

conn.commit()
conn.close()

print("Database created and sample data added.")