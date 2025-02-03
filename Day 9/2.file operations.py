#reading the entire file(1)
with open("sample.txt","r") as file:
    content=file.read()
    print(content)
 #reading the entire file(2)   
file=open("sample.txt","r")
content=file.read()
print(content)
file.close()

#reading line by line
with open("sample.txt","r") as file:
    for line in file:
        print(line.strip())