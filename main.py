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

#Utworzenie dwóch list przy pomocy pętli:
#Alfabet:
alphabet = []
for row in letter_to_morse_code:
    alphabet.append(row[0])

#Morse Code:
morse_code = []
for row in letter_to_morse_code:
    morse_code.append(row[1])


#Znalezienie danej litery w liście:
def letter_to_morse_code(letter):
    index = 0
    for i in alphabet:
        if i == letter:
            return index
        index += 1


while True:
    letter = input("Podaj zdanie do przetłumaczenia na kod Morse'a").upper()
    try:
        print(f'{letter} - {morse_code[letter_to_morse_code(letter)]}')
    except TypeError:
        print("Zastosowano niedozwolony znak")