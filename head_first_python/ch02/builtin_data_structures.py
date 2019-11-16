some_numbers = [1,5,7,9,12,34,]
for num in some_numbers: 
    print(str(num) + " is one of my numbers")
print("I had " + str(len(some_numbers)) + " numbers")
some_numbers.append(42)
for num in some_numbers:
    print(str(num) + " is one of my numbers")
print("I had " + str(len(some_numbers)) + " numbers")