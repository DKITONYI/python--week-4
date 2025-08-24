

filename = input("Enter the filename: ")

try:
    with open(filename, "r") as file:
        data = file.read()
        print("File content:")
        print(data)
except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: Permission denied.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
