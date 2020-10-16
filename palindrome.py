from collections import Counter 

def obtener_palindromo_ganador(pozo):
  string_j1 = ""
  string_j2= ""
  i = 0
  
  while i < len(pozo):
    string_j1 += pozo[i]
    string_j2 += pozo[i+1] if i <= len(pozo) - 2 else ""
    i += 2

  palindromo_j1 = generar_palindromo(string_j1)
  palindromo_j2 = generar_palindromo(string_j2)

  if not palindromo_j1 and palindromo_j2:
    result= f"PO {palindromo_j2}"
  elif not palindromo_j2 and palindromo_j1:
    result = f"PA {palindromo_j1}"
  elif palindromo_j1 and palindromo_j2:
    # Ambos tienen un palindromo
    if len(palindromo_j1) > len(palindromo_j2):
      result = f"PA {palindromo_j1}"
    elif len(string_j2) > len(string_j1):
      result = f"PO {palindromo_j2}"
    else:
      result = "EMPATE"
      #print(f"PA: {palindromo_j1}")
      #print(f"PO: {palindromo_j2}")
  else:
    # cuando ninguno es palíndromo que chucha hacemos?
    result = "NO HAY PALINDROMO: EMPATE"

  return result

def generar_palindromo(s):
  contador = Counter(s)
  palindromo = ""
  mitad_1 = ""
  mitad_2 = ""
  medio = []
  for letra in contador.keys():
    if contador[letra] < 2:
      # letra sin repetir
     medio.append(letra)
     continue
    elif contador[letra] % 2 != 0:
      # se repita la letra en una cantidad impar
      medio.append(letra)

    cantidad_repetida = contador[letra] - contador[letra] % 2    
    mitad_cantidad=cantidad_repetida//2
    mitad_1 += letra * mitad_cantidad
    mitad_2 += letra * mitad_cantidad

  palindromo += mitad_1 + (medio[0] if len(medio)>0 else '') + mitad_2[::-1]
  
  return palindromo

# Función principal de inicio
if __name__ == '__main__':
  pozo = False
  while(pozo is False or len(pozo) >= 15):
    print("Ingrese una palabra de menos de 15 caracteres:")
    pozo = input()
  result = obtener_palindromo_ganador(pozo)
  print (result)


