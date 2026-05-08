# Main logic for Fastener Search Application - Handles database queries and data processing for fastener lookups
from database import get_connection

# Fastener Search Function - Looks up a fastener by its 3-letter code and returns its details
def lookup_fastener(code):
    conn = get_connection()
    cursor = conn.cursor()

    # SQL query to find the fastener with the specified code
    cursor.execute("""
    SELECT *
    FROM fasteners
    WHERE code = ?
    """, (code.upper(),))

    result = cursor.fetchone()
    conn.close()

    return result

#Returns the fastener details in JSON format for API responses
def json_code_lookup(code):
    fastener = lookup_fastener(code)
    
    if fastener:
        return dict(fastener)
        
    return None




# TEST CODE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Fastener Search Input
# code = input("Enter 3-letter fastener code: ")
# print(json_code_lookup(code))


# fastener = lookup_fastener(code)
# # Fastener Search Output - Displays the details of the fastener if found, otherwise shows a not found message
# if fastener:
#     print(f"Code: {fastener['code']}")
#     print(f"material: {fastener['material']}")
#     print(f"Name: {fastener['name']}")
#     print(f"Size: {fastener['size']}")
#     print(f"Length: {fastener['length']}")
# else:
#     print("No fastener found for that code.")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~