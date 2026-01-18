try:
    fh=open("sample.txt","rt")
    print("Reading file content:")
    lines=fh.readlines()
    for line in range(len(lines)):
        l=lines[line].rstrip("\n")
        print(f"line{line+1}: {l}")
    fh.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist")
