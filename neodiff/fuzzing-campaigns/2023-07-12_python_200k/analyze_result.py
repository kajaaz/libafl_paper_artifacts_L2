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

# Find crashes and count differences
crashes = []
opcode_set = set()
num_batches = len(data)  # Count the number of unique keys (batches)

for entries in data.values():
    for entry in entries:
        vm1 = entry["vm1"]
        vm2 = entry["vm2"]

        if vm1["crash"] or vm2["crash"]:
            crashes.append(entry)

        opcode_set.add(vm1["opcode"])
        opcode_set.add(vm2["opcode"])

# Print the crashes
if crashes:
    print("Crashes found:")
    for crash in crashes:
        print("VM1 Code:", crash["vm1_code"])
        print("VM2 Code:", crash["vm2_code"])
        print("Checksum (VM1):", crash["vm1"]["checksum"])
        print("Checksum (VM2):", crash["vm2"]["checksum"])
        print()

# Print the number of batches
print("Number of batches:", num_batches)

# Print the opcodes involved
print("Opcodes involved:", ", ".join(str(opcode) for opcode in opcode_set))
