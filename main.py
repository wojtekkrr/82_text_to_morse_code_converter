import csv

# Otwarcie pliku CSV w trybie odczytu
with open('morse_code_chart.csv', mode='r') as file:
    # Utworzenie obiektu czytnika CSV
    data = csv.reader(file)

    #Lista z kodem morse'a
    letter_to_morse_code = []
    # Przetwarzanie danych w pętli
    for row in data:
        letter_to_morse_code.append(row)

#Utworzenie dwóch list w pętlach:
#Alfabet:

print(letter_to_morse_code)