# Count frequency of items using dictionary
# Like:
# {"apple": 3, "mango": 5}

d = {"apple": 3, "mango": 5}

freq = 0
for v in d.values():
    freq+=v

print(freq)
