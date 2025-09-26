import random

choice = input("""
Digite '1' para Isósceles
Digite '2' para Equilátero
Digite '3' para Escaleno

Qual tipo de triângulo você deseja? """)

coords = []

for i in range(1,3):
  x = random.randint(-10, 10)
  y = random.randint(-10, 10)  
  coords.append((x, y))

medioAB = ((coords[0][0] + coords[1][0])/2, (coords[0][1] + coords[1][1])/2)

if choice == "1":
  if not (coords[0][1] == coords[1][1]) and not (coords[0][0] == coords[1][0]):
    mAB = (coords[0][1] - coords[1][1])/(coords[0][0] - coords[1][0])
    b = medioAB[1] + (1/mAB) * medioAB[0]

  if coords[0][1] == coords[1][1]:
    coords.append((medioAB[0], random.randint(-10,10)))
  elif coords[0][0] == coords[1][0]:
    coords.append((random.randint(-10,10), medioAB[1]))
  else:
    x = random.randint(-10, 10)
    y = -(1/mAB) * x + b

    coords.append((x, y))
elif choice == "2":
  difX = coords[0][0] - coords[1][0]
  difY = coords[0][1] - coords[1][1]

  distAB = ((difX)**2 + (difY)**2)**(1/2)

  height = (distAB * 3**(1/2))/2

  uniqueValueX = -difY/distAB
  uniqueValueY = difX/distAB

  randomChoice = random.randint(1, 2)

  if randomChoice == 1:
    uniqueValueX = height * uniqueValueX
    uniqueValueY = height * uniqueValueY
  else:
    uniqueValueX = -height * uniqueValueX
    uniqueValueY = -height * uniqueValueY

  coords.append((medioAB[0] + uniqueValueX, medioAB[1] + uniqueValueY))
elif choice == "3":
  while True:
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    
    distAB = ((coords[0][0] - coords[1][0])**2 + (coords[0][1] - coords[1][1])**2)**(1/2)
    distAC = ((coords[0][0] - x)**2 + (coords[0][1] - y)**2)**(1/2)
    distBC = ((x - coords[1][0])**2 + (y - coords[1][1])**2)**(1/2)

    if not distAB == distAC and not distAB == distBC and not distAC == distBC:
      coords.append((x, y))
      break
    
print("\nAs seguintes coordenadas correspodem a um trinângulo do tipo que você escolheu: ")

for i in coords:
  print(i)