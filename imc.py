weigth = float(input("digite o seu peso"))
height = float(input("digite a sua altura"))

imc = weigth / (height * height)

if imc < 18.5:
  print("Abaixo do peso")
elif imc < 25:
  print("Saudável")
elif imc < 30:
  print("Peso em excesso")
elif imc < 35:
  print("Obesidade grau 1")
elif imc < 40:
  print("Obesidade grau 2")
else:
  print("Obesidade grau 3")