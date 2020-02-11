#validation

try:
    userGuess = int(input("Pleas enter a number: "))

except ValueError:
    print("Unfortunately that number is not valid")
