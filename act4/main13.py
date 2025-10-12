txt_data = "I like pizza!"

file_path = "output.txt"

with open(file_path, "w") as file:
    file.write(txt_data)
    print(f"Txt file '{file_path}' was created")