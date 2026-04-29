# Fastener Search App
from database import get_connection

# Fastener Search Function - Looks up a fastener by its 3-letter code and returns its details
def lookup_fastener(code):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT code, material, size, length, name
    FROM fasteners
    WHERE code = ?
    """, (code.upper(),))

    result = cursor.fetchone()
    conn.close()

    return result

#Fastener Search Input
code = input("Enter 3-letter fastener code: ")

fastener = lookup_fastener(code)

# Fastener Search Output - Displays the details of the fastener if found, otherwise shows a not found message
if fastener:
    print(f"Code: {fastener['code']}")
    print(f"material: {fastener['material']}")
    print(f"Name: {fastener['name']}")
    print(f"Size: {fastener['size']}")
    print(f"Length: {fastener['length']}")
else:
    print("No fastener found for that code.")