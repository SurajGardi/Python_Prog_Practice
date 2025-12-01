# Task 3: Count vowels in a string
# (using for loop + conditions)

string = input("Enter String to Count Vowels : ").lower()

voewels = "aeiou"
count=0

for s in string:
    if s in voewels:
        count+=1

print(f"Vowels in String Are : {count}")