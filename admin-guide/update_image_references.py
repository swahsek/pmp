import re

# Define the prefix
prefix = 'temp-auth-partner-'

# Prompt the user to input the file path
file_path = input("Please enter the file path: ")

# Read the content of the file
with open(file_path, 'r') as file:
    content = file.read()

# Define the regex pattern to find all image references
pattern = r'(!\[\]\(./half/media/)([^)]+\.png\))'

# Replace the image references with the new prefix
new_content = re.sub(pattern, r'\1' + prefix + r'\2', content)

# Write the new content back to the file
with open(file_path, 'w') as file:
    file.write(new_content)

print("Image references updated successfully.")