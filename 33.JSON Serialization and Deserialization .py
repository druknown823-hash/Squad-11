# Import the built-in json module
import json 

# --- 1. Python Object (Dictionary) to be Serialized ---

# Define a Python dictionary (the object we want to convert to a JSON string)
python_dict = {
    "name": "Jane Doe",
    "age": 30,
    "is_student": False,
    "courses": ["History", "Math", "Science"],
    "details": {
        "id": 101,
        "is_active": True
    }
}

print("--- Step 1: Python Object (Serialization Input) ---")
print(f"Type: {type(python_dict)}") # Shows it is a Python dict
print(f"Data: {python_dict}")
print("-" * 40)


# --- 2. Serialization (Python to JSON String) ---

# Use json.dumps() to convert the Python object into a JSON formatted string
# 'indent=4' makes the JSON string nicely readable (pretty printed)
json_string = json.dumps(python_dict, indent=4) 

print("--- Step 2: JSON String Output ---")
print(f"Type: {type(json_string)}") # Shows it is a Python string
print("JSON Data:")
print(json_string) # The data now looks like JavaScript/JSON syntax
print("-" * 40)


# --- 3. Deserialization (JSON String back to Python Object) ---

# Use json.loads() to parse the JSON string back into a Python object (a dictionary)
python_object_restored = json.loads(json_string) 

print("--- Step 3: Restored Python Object (Deserialization Output) ---")
print(f"Type: {type(python_object_restored)}") # Shows it is back to a Python dict
print(f"Data: {python_object_restored}")

# Demonstrate that we can now work with the object as a Python dict
print(f"\nAccessing restored data: Name is {python_object_restored['name']}")