text=input("Enter text to write to the file: ")
file="output.txt"
with open(file,"wt") as f:
    f.write(text)
    print(f"Data succesfully written to {file}\n")
aptx=input("Enter additional text to append: ")
with open(file,"at") as f:
    f.write(f"\n{aptx}")
    print("Data successfully appended\n")
print(f"Final content of {file}:")
with open(file,"rt") as f:
    print(f.read())