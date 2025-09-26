texto = input("Digite uma palavra ou frase: ")

texto = texto.upper()
n = len(texto)
palindromo = True

for i in range(n):
    j = n - 1 - i
    if i >= j:
        break
    if texto[i] != texto[j]:
        palindromo = False
        break

if palindromo:
    print("É palíndromo")
else:
    print("Não é palíndromo")