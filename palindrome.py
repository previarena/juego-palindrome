def obtener_palindromo_ganador(pozo):  
  if(len(pozo) >14):
    return "No puede ser mayor a 14 caracteres."
  if len(pozo) == 0 or len(pozo) == 2:
    return "EMPATE"
  if len(pozo) == 1 :
    return "PA " + pozo
  PO = ""
  PA =""
  esPO = False
  for c in pozo:
    if esPO:
      esPO = False
      PO = PO + c
    else:
      esPO = True
      PA = PA + c    
  # Escriba su código acá
  palindromoPO = consultaPalindormoDerechaAIzquierda(PO)
  palindromoPA = consultaPalindormoDerechaAIzquierda(PA)
  if(len(palindromoPA)>len(palindromoPO)):
    return "PA " + palindromoPA
  if(len(palindromoPA)<len(palindromoPO)):
    return "PO " + palindromoPO
  return "EMPATE"

def consultaPalindormoDerechaAIzquierda(S):
  aux = S
  if len(S) == 1 or len(S) == 0:
    return S
  subString = S[0]
  if S.count(subString)>1:
    aux = S[1:S.rfind(subString)]
    return subString + consultaPalindormoIzquierdaADerecha(aux) +subString
  aux = S[1:]  
  return consultaPalindormoIzquierdaADerecha(aux)

def consultaPalindormoIzquierdaADerecha(S):
  aux = S
  if len(S) == 1 or len(S) == 0:
    return S
  subString = S[-1:]
  if S.count(subString)>1:
    aux = S[S.find(subString)+1:-1]
    return subString + consultaPalindormoDerechaAIzquierda(aux) +subString
  aux = S[0:-1]  
  return consultaPalindormoDerechaAIzquierda(aux)

# Función principal de inicio
if __name__ == '__main__':
    pozo = input()
    result = obtener_palindromo_ganador(pozo)
    print (result)