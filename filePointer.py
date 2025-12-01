f = open("data.txt", "r")
print(f.tell())
f.seek(0)
print(f.read(5))
