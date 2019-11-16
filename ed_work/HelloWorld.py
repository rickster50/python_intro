print("Hello People: ")
amount = float(input("Principal:"))
interestRate = float(input("IR:"))
years = int(input("Number of Years:"))
total = (amount * pow(1+ (interestRate/100), years))
interest = total - amount
print("\nInterest = %0.2f" %interest)