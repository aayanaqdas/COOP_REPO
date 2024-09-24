def calculator():
    # Get user input for numbers and operation
    operation = input("Velg operasjon (+, -, *, /): ")
    tall1 = int(input("Skriv inn det første tallet: "))
    tall2 = int(input("Skriv inn det andre tallet: "))
    
    # Perform the chosen operation
    if operation == "+":
        result = tall1 + tall2
        print(f'{tall1} + {tall2} = {result}')
    elif operation == "-":
        result = tall1 - tall2
        print(f'{tall1} - {tall2} = {result}')
    elif operation == "*":
        result = tall1 * tall2
        print(f'{tall1} * {tall2} = {result}')
    elif operation == "/":
        if tall2 != 0:  # Avoid division by zero
            result = tall1 / tall2
            print(f'{tall1} / {tall2} = {result}')
        else:
            print("Kan ikke dele med 0")
    else:
        print("Ugyldig operasjon. Vennligst prøv igjen.")