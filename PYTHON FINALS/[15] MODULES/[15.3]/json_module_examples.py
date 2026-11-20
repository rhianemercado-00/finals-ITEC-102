# JSON Module Examples

import json

# Example 1: Converting Python objects to JSON
print("Example 1: Python to JSON Conversion")

# Simple data types
data_int = 42
data_str = "Hello"
data_bool = True

data_list = [1, 2, 3, "four", True]
data_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": False
}

print(f"Integer to JSON: {json.dumps(data_int)}")
print(f"String to JSON: {json.dumps(data_str)}")
print(f"Boolean to JSON: {json.dumps(data_bool)}")
print(f"List to JSON: {json.dumps(data_list)}")

# Pretty printing dict
print("Dictionary to JSON (pretty printed):")
print(json.dumps(data_dict, indent=2))

# Example 2: Converting JSON to Python objects
print("\nExample 2: JSON to Python Conversion")

json_string = '{"name": "Bob", "age": 25, "skills": ["Python", "JavaScript"]}'
python_obj = json.loads(json_string)

print(f"JSON string: {json_string}")
print(f"Converted to Python object: {python_obj}")
print(f"Name: {python_obj['name']}")
print(f"First skill: {python_obj['skills'][0]}")

# Example 3: Working with complex nested data
print("\nExample 3: Complex Nested Data")

company_data = {
    "company": "TechCorp",
    "employees": [
        {
            "id": 1,
            "name": "Alice",
            "department": "Engineering",
            "salary": 75000,
            "skills": ["Python", "Django", "PostgreSQL"]
        },
        {
            "id": 2,
            "name": "Bob",
            "department": "Marketing",
            "salary": 65000,
            "skills": ["SEO", "Content Marketing"]
        }
    ],
    "founded": 2010
}

# Convert to JSON
json_data = json.dumps(company_data, indent=2)
print("Company data in JSON format:")
print(json_data)

# Example 4: Reading and writing JSON files
print("\nExample 4: JSON File Operations")

# Write data to file
with open("data.json", "w") as file:
    json.dump(company_data, file, indent=2)

print("Data written to data.json")

# Read data from file
with open("data.json", "r") as file:
    loaded_data = json.load(file)
    
print("Data loaded from data.json:")
print(f"Company: {loaded_data['company']}")
print(f"Number of employees: {len(loaded_data['employees'])}")

# Example 5: Handling JSON errors
print("\nExample 5: Error Handling")

invalid_json = '{name: "Alice", age: 30}'  # Missing quotes

try:
    result = json.loads(invalid_json)
    print(result)
except json.JSONDecodeError as e:
    print(f"JSON decode error: {e}")
    print(f"Error at position: {e.pos}")

# Example 6: Custom serialization
print("\nExample 6: Custom Serialization")

# With custom separators
compact_json = json.dumps(data_dict, separators=(',', ':'))
print(f"Compact JSON: {compact_json}")

# Sorted keys
sorted_json = json.dumps(data_dict, sort_keys=True, indent=2)
print("With sorted keys:")
print(sorted_json)

# Example 7: Working with arrays and nested structures
print("\nExample 7: Array Operations")

products = [
    {"id": 1, "name": "Laptop", "price": 999.99, "in_stock": True},
    {"id": 2, "name": "Mouse", "price": 29.99, "in_stock": True},
    {"id": 3, "name": "Keyboard", "price": 79.99, "in_stock": False}
]

# Save products to file
with open("products.json", "w") as file:
    json.dump(products, file, indent=2)

# Load and process
with open("products.json", "r") as file:
    loaded_products = json.load(file)
    
in_stock_count = sum(1 for product in loaded_products if product["in_stock"])
    total_value = sum(product["price"] for product in loaded_products)
    
print(f"Products in stock: {in_stock_count}")
print(f"Total value of all products: ${total_value:.2f}")

# Example 8: Pretty printing with ensure_ascii
print("\nExample 8: Unicode Handling")

unicode_data = {
    "greeting": "Hello 世界",
    "emoji": "😀😃😄",
    "currency": "Price: €100, ¥10000"
}

# With ensure_ascii=True (default)
ascii_json = json.dumps(unicode_data, ensure_ascii=True)
print(f"With ASCII encoding: {ascii_json}")

# With ensure_ascii=False
unicode_json = json.dumps(unicode_data, ensure_ascii=False, indent=2)
print("With Unicode preservation:")
print(unicode_json)