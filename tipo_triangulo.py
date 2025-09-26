coords = []

for i in range(1,4):
  x = float(input(f"Digite o X da {i}º coordenada: "))
  y = float(input(f"Digite o Y da {i}º coordenada: "))
  coords.append((x, y))

distAB = ((coords[0][0] - coords[1][0])**2 + (coords[0][1] - coords[1][1])**2)**(1/2)
distAC = ((coords[0][0] - coords[2][0])**2 + (coords[0][1] - coords[2][1])**2)**(1/2)
distBC = ((coords[2][0] - coords[1][0])**2 + (coords[2][1] - coords[1][1])**2)**(1/2)

differX = coords[0][0] - coords[1][0]
differY = coords[0][1] - coords[1][1]

try:
  angleOne = (coords[0][1] - coords[1][1])/(coords[0][0] - coords[1][0])
except:
  angleOne = "Undefined"

try:
  angleTwo = (coords[1][1] - coords[2][1])/(coords[1][0] - coords[2][0])
except:
  angleTwo = "Undefined"


if not angleOne == angleTwo:
  if distAB == distAC and distAB == distBC:
    print("Triângulo equilátero")
  elif distAB == distAC or distAB == distBC or distAC == distBC:
    print("Triângulo isósceles")
  else:
    print("Triângulo escaleno")
else:
  print("Não é um triângulo")