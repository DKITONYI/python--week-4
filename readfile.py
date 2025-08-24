with open("input.txt", "r") as infile:
    data = infile.read()

# Capitalize each word for better readability
modified_data = data.title()

with open("output.txt", "w") as outfile:
    outfile.write(modified_data)

print("Modified content written to output.txt")