is_quadrilateral = True

coords = []

for i in range(1,5):
  x = float(input(f"Digite o valor do X da {i}º coordenada: "))
  y = float(input(f"Digite o valor do Y da {i}º coordenada: "))
  coords.append((x, y))

triangleOne = [coords[0], coords[1], coords[2]]
triangleTwo = [coords[0], coords[1], coords[3]]
triangleThree = [coords[0], coords[2], coords[3]]
triangleFour = [coords[1], coords[2], coords[3]]

triangles = [triangleOne, triangleTwo, triangleThree, triangleFour]

for i in triangles:
  try:
    angleOne = (i[0][1] - i[1][1])/(i[0][0] - i[1][0])
  except:
    angleOne = "Undefined"

  try:
    angleTwo = (i[1][1] - i[2][1])/(i[1][0] - i[2][0])
  except:
    angleTwo = "Undefined"

  if angleOne == angleTwo:
    is_quadrilateral = False
    msg = "Não é um quadrilátero"
    break

if is_quadrilateral:
  distAB = ((coords[0][0] - coords[1][0])**2 + (coords[0][1] - coords[1][1])**2)**(1/2)
  distAC = ((coords[0][0] - coords[2][0])**2 + (coords[0][1] - coords[2][1])**2)**(1/2)
  distAD = ((coords[0][0] - coords[3][0])**2 + (coords[0][1] - coords[3][1])**2)**(1/2)
  distBC = ((coords[1][0] - coords[2][0])**2 + (coords[1][1] - coords[2][1])**2)**(1/2)
  distBD = ((coords[1][0] - coords[3][0])**2 + (coords[1][1] - coords[3][1])**2)**(1/2)
  distCD = ((coords[2][0] - coords[3][0])**2 + (coords[2][1] - coords[3][1])**2)**(1/2)

  dist = [distAB, distAC, distAD, distBC, distBD, distCD]
  msg = "É um quadrilátero"

  for i in dist:
    if dist.count(i) == 4:
      msg = "É um quadrado"
      break

    if not dist.count(i) == 2:
      msg = "É um quadrilátero, mas não é um retãngulo nem um quadrado"
      break

    msg = "É um retângulo"

print(msg)
