# Task 2: Write, Append, and Read from a file

# Step 1: Write user input
user_input = input("Enter something to write into the file: ")
with open('output.txt', 'w') as file:
    file.write(user_input + '\n')

# Step 2: Append additional data
with open('output.txt', 'a') as file:
    file.write("This is appended data.\n")

# Step 3: Read and print final content
print("\nFinal content of 'output.txt':")
with open('output.txt', 'r') as file:
    for line in file:
        print(line.strip())
# Step 4: Read and print the content of the file
with open('output.txt', 'r') as file:
    content = file.read()
    print("\nContent of 'output.txt':")
    print(content)