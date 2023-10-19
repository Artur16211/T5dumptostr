import re
import sys
import fileinput

# the input is the message.txt in the same folder of the py
# Read the content of the "message.txt" file
# with open("message.txt", "r") as file:
# input_string = file.read()

# get the file drag and drop to the py
file_dump = sys.argv[1]

with open(file_dump, "r") as file_dump:
    input_string = file_dump.read()

# input
cuba = input("Enter the pattern: ")

# Define a regular expression pattern to match CUBA_ followed by non-space characters
pattern = rf'{cuba}_[^\s]+'

# Use re.finditer to find all matching patterns in the input string
matches = re.finditer(pattern, input_string)

# Initialize the index to start searching for LANG_ENGLISH
start_index = 0

# Create the desired output for each match
output_strings = []
for match in matches:
    start, end = match.span()
    english1 = input_string[start_index:start].strip()
    # remove the ÿ from english1
    english_text = english1.replace("ÿ", "").replace("Ã¿", "")
    output_string_b = f"REFERENCE\t{match.group(0).replace(f'{cuba}_', '')}\nLANG_ENGLISH\t\"{english_text}\"\n"
    # replace "REFERENCE       " with "REFERENCE			"
    output_string = re.sub(r'REFERENCE\s+', 'REFERENCE\t\t\t',
                           re.sub(r'LANG_ENGLISH\s+', 'LANG_ENGLISH\t\t', output_string_b))
    output_strings.append(output_string)
    start_index = end

# Write the output strings to "output.txt" file
with open("output.txt", "w") as output_file:
    for output_string in output_strings:
        output_file.write(output_string)
