liczba = int(input("Podaj liczbę nieujemną: "))
while liczba is None or liczba < 0:
    liczba = int(input("Podaj liczbę nieujemną: "))
suma = liczba

while suma % 13 != 0:
    liczba = int(input("Podaj liczbę: "))
    while liczba < 0:
        liczba = int(input("Liczba musi być nieujemna: "))
    suma = suma + liczba

print(suma)