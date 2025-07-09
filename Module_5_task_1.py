try:
    with open(r'C:\Users\Saura\Desktop\VSCODE\Tutedude\sample_1.txt', 'r') as file:
        # Read the content of the file
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found. Please check the file path.")
