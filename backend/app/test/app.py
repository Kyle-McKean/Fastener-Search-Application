# Fastener Search App - Test
from database import get_connection

def lookup_fastener(code):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT code, description, location, category
    FROM fasteners
    WHERE code = ?
    """, (code.upper(),))

    result = cursor.fetchone()
    conn.close()

    return result

code = input("Enter 3-letter fastener code: ")

fastener = lookup_fastener(code)

if fastener:
    print(f"Code: {fastener['code']}")
    print(f"Description: {fastener['description']}")
    print(f"Location: {fastener['location']}")
    print(f"Category: {fastener['category']}")
else:
    print("No fastener found for that code.")