import re

# Open and read the file
with open('list.txt', 'r') as readfile:
    # Read the file content
    content = readfile.read()
    # Split the content first by '+' then by newlines
    data = [re.split(r'\n', part) for part in re.split(r'\s+', content)]



print(data)

