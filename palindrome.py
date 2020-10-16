# GRUPO: ZEUS - Integrantes: ROrtiz, FSoto, YPerez
# retorna la cantidad de repeticiones para una letra dentro de una cadena de texto
def numeroDeOcurrencias(cadena, letra):
  return cadena.count(letra)
# Metodo que genera 2 arreglos para contener las letras repetidas y las que no. Obteniendo como resultado la combinatoria mayor de palabras palindromos.
def obtenerPalindromo(cadena):
  letrasPalindromo = ""
  letrasInpar = ""
  for letra in cadena:
    ocurrencia = numeroDeOcurrencias(cadena, letra)
    if(ocurrencia%2 == 0):
      letrasPalindromo = letrasPalindromo + letra
    else:
      letrasInpar = letrasInpar + letra
  palindromoMayor = ""
  if (len(letrasPalindromo) == 0):
    return ""
  elif (len(letrasPalindromo) > 0 and len(letrasInpar) > 0):
    mitadString = int(len(letrasPalindromo)/2)
    palindromoMayor = letrasPalindromo[:mitadString] + letrasInpar[0] + letrasPalindromo[mitadString:]
    return palindromoMayor
  else:
    return letrasPalindromo
# realiza la comparativa de dos participantes, para el resultado final
def obtenerPalindromoGanador(cadenaA, cadenaB):
  largoA = len(cadenaA)
  largoB = len(cadenaB)
  if largoA > largoB:
    return "PA "+ cadenaA
  elif largoA == largoB:
    return "empate"
  else :
    return "PO "+ cadenaB
#verifica que la cadena contenga digito
def checkCadenaCorrecta(cadena):
  for letra in cadena:
    if letra.isdigit():
      return False
  return True
# Separa cadenas para dos jugadores
def defineTurnos(cadena):
  PA = ""
  PO = ""
  i = 0
  for x in cadena:
    if(i%2 == 0):
      PA = PA+x
    else :
      PO = PO+x
    i += 1
  turnos = (PA,PO)
  return turnos
# Función principal de inicio
if __name__ == '__main__':
  maxLen = 15
  check = True
  pozo = ""
  while(check):
    pozo = input()
    if(len(pozo) > maxLen or not checkCadenaCorrecta(pozo)):
      print("Palabra incorrecta")
    else:
      check=False
  pozo = pozo.lower()
  turnos = defineTurnos(pozo)
  cadenaPA = turnos[0]
  cadenaPO = turnos[1]
  palindromoMayorPA = obtenerPalindromo(cadenaPA)
  palindromoMayotPO = obtenerPalindromo(cadenaPO)
  print(obtenerPalindromoGanador(palindromoMayorPA, palindromoMayotPO))
