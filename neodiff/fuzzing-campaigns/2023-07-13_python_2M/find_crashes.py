import sys
import json

# Check if the JSON file name is provided as a command-line argument
if len(sys.argv) < 2:
    print("Please provide the name of the JSON file to analyze.")
    sys.exit(1)

# Extract the JSON file name from command-line arguments
json_file = sys.argv[1]

# Read the JSON file
with open(json_file, "r") as file:
    data = json.load(file)

# Find crashes
crashes = []
for entry in data.values():
    for item in entry:
        if item["vm1"]["crash"] or item["vm2"]["crash"]:
            crashes.append(item)

# Print the crashes
if crashes:
    print("Crashes found:")
    for crash in crashes:
        print("VM1 Code:", crash["vm1_code"])
        print("VM2 Code:", crash["vm2_code"])
        print("Checksum (VM1):", crash["vm1"]["checksum"])
        print("Checksum (VM2):", crash["vm2"]["checksum"])
        print()
else:
    print("No crashes found.")
