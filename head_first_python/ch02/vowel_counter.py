vowels = ["a","e","i","o","u"]
text = input("Enter your text: ")
found = []
for character in text:
    if character in vowels:
        if character not in found:
            found.append(character)
found.sort()            
print("I found "+str(len(found)) + " vowels\nthey are" + str(found))

for character in text[2:6:]:    
    print(str(character))

