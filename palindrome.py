
def obtener_palindromo_ganador(pozo):
  # Escriba su código acá

  resultadoPO = ejecutar(sorted(obtener_texto(pozo, True)))
  resultadoPA = ejecutar(sorted(obtener_texto(pozo, False)))
  largoPO = len(resultadoPO)
  largoPA = len(resultadoPA)
  
  if largoPO == largoPA:
    print("EMPATE")
    pozo = resultadoPA
  elif largoPO < largoPA :
    print ("Gana PA %s"%resultadoPA)
    pozo = resultadoPA
  else:
    print ("Gana PO %s"%resultadoPO)
    pozo = resultadoPO
  return pozo
 
def ejecutar(texto):
#Ejecuta
  nuevoTexto = ""
  i = 0
  letraSola = ""
  existeSola = True
  while i<(len(texto)-1):
    if( texto[i]== texto[i+1] ):
      nuevoTexto = nuevoTexto + texto[i]
      i=i+1
    elif existeSola:
      letraSola = texto[i]
      existeSola = False
    i = i+1
  valorReversa = reversa(nuevoTexto)
  return "%s%s%s"%(nuevoTexto, letraSola, valorReversa)

def reversa (texto):
  return texto[::-1]

#Obtiene el texto de entrada
def obtener_texto(pozo, esPar):
  a = []
  for i, c in enumerate(pozo):
    par = i%2 == 0
    if esPar :
      if par:
        a.append(c) 
    else :
      if not par :
        a.append(c)
 
  return a
  
# Función principal de inicio
if __name__ == '__main__':
    pozo = input()
    result = obtener_palindromo_ganador(pozo)
    
    print (result)


