import csv

# Otwarcie pliku CSV w trybie do odczytu
with open('morse_code_chart.csv', mode='r') as file:
    # Utworzenie obiektu czytnika CSV
    data = csv.reader(file)

    # Lista z kodem morse'a
    letter_to_morse_code = []
    # Przetwarzanie danych w pętli
    for row in data:
        letter_to_morse_code.append(row)

# Utworzenie dwóch list przy pomocy pętli:
# Alfabet:
alphabet = []
for row in letter_to_morse_code:
    alphabet.append(row[0])

# Morse Code:
morse_code = []
for row in letter_to_morse_code:
    morse_code.append(row[1])


# Znalezienie danej litery w liście:
def letter_to_morse_code(letter):
    index = 0
    for i in alphabet:
        if i == letter:
            return index
        index += 1


# Rozbicie zdania na litery:
def sentence_to_letters(sentence):
    letters = []
    for letter in sentence:
        letters.append(letter)
    return letters


# Komunikaty dla użytkownika:
print("Tłumacz zdań na kod Morse'a.\n")
print(f'Można korzystać z następujących znaków:\n{alphabet}\n')
sentence = input("Jeśli chcesz wyjść, naciśniej ENTER. Jeśli chcesz tłumaczyć, podaj zdanie i zaakceptuj:\n").upper()

# Tłumaczenie zdania litera po literze na kod Morse'a, wyświetlanie komunikatów:
sentence_in_morse_code = ""
unpermitted_sign = ""

if sentence == "":
    runnning = False
else:
    runnning = True

while runnning:
    sentence_in_morse_code = ""
    unpermitted_sign = ""
    letters = sentence_to_letters(sentence)
    try:
        for letter in letters:
            unpermitted_sign = letter
            sentence_in_morse_code = sentence_in_morse_code + morse_code[letter_to_morse_code(letter)]
    except TypeError:
        print(f"\nZastosowano niedozwolony znak: {unpermitted_sign}\n")
        sentence = input(
            "Jeśli chcesz wyjść, naciśniej ENTER. Jeśli chcesz tłumaczyć, podaj zdanie i zaakceptuj:\n").upper()
        if sentence == "":
            runnning = False
    else:
        print(f"\nPodane zdanie przetłumaczone na kod Morse'a:\n{sentence_in_morse_code}\n")
        sentence = input(
            "Jeśli chcesz wyjść, naciśniej ENTER. Jeśli chcesz tłumaczyć, podaj zdanie i zaakceptuj:\n").upper()
        if sentence == "":
            runnning = False
