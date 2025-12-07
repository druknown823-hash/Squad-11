# Import the built-in pickle module
import pickle 

# --- 1. Python Object to be Serialized ---

# Define a complex Python object (a list containing a dictionary and an integer)
python_object_to_save = [
    "Example Data", 
    42, 
    {
        "status": "ready",
        "timestamp": "2025-12-08"
    }
]

file_name = "data.pkl" # Define the filename to save the pickled data

print("--- Step 1: Original Python Object ---")
print(f"Data: {python_object_to_save}") 
print("-" * 40)


# --- 2. Serialization (Pickling to a File) ---

# Open the file in WRITE-BINARY mode ('wb')
try:
    with open(file_name, 'wb') as file: 
        # Use pickle.dump() to write the object's byte stream to the file
        pickle.dump(python_object_to_save, file) 
    print(f"Serialization successful! Object saved to '{file_name}'.")

except Exception as e:
    print(f"An error occurred during pickling: {e}")
    exit()


# --- 3. Deserialization (Unpickling from the File) ---

# Start a variable to hold the restored object
restored_object = None

# Open the same file in READ-BINARY mode ('rb')
try:
    with open(file_name, 'rb') as file:
        # Use pickle.load() to read the byte stream and rebuild the Python object
        restored_object = pickle.load(file) 
    print("\n--- Step 3: Restored Python Object ---")
    print("Deserialization successful! Object loaded back from file.")

except FileNotFoundError:
    print(f"ERROR: Could not find the file '{file_name}'.")
except Exception as e:
    print(f"An error occurred during unpickling: {e}")


# --- 4. Verification ---

if restored_object is not None:
    print(f"\nType of restored object: {type(restored_object)}")
    print(f"Restored Data: {restored_object}") 
    
    # Check if the restored object is identical to the original
    if restored_object == python_object_to_save:
        print("Verification: The restored object matches the original data.")
    else:
        print("Verification: Data mismatch!")