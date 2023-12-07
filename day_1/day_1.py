# Load data
with open("day_1/data.txt", "r") as f:
    data = f.read().split("\n")

counter = 0
num_list = ["1","2","3","4","5","6","7","8","9"]

# lines = nth line in data
for lines in data:
    for letter in lines:
        if letter in num_list:
          counter = counter + 10*int(letter)
          break
    
    
    revlines = (lines[::-1])
    for letter2 in revlines:
        if letter2 in num_list:
          counter = counter + int(letter2)
          break

print(counter)
