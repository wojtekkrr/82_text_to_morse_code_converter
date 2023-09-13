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

#Komunikaty dla urzytkownika:
print(f'Można korzystać z następujących znaków:\n{alphabet}')
sentence = input("Podaj zdanie do przetłumaczenia na kod Morse'a:\n").upper()

#Rozbicie zdania na litery:
letters = []
for letter in sentence:
    letters.append(letter)

#Tłumaczenie zdania litera po literze na kod Morse'a, wyświetlanie komunikatów:
sentence_in_morse_code = ""
unpermitted_sign = ""
try:
    for letter in letters:
        unpermitted_sign = letter
        sentence_in_morse_code = sentence_in_morse_code + morse_code[letter_to_morse_code(letter)]
except TypeError:
    print(f"Zastosowano niedozwolony znak: {unpermitted_sign}")
else:
    print(f"Podane zdanie przetłumaczone na kod Morse'a:\n{sentence_in_morse_code}")

input("Wciśnij Enter, aby zakończyć...")