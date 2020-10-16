## Temática: Juego del palíndromo ganador

Previto y Previta, se enteraron de que trabajan hasta las 15:30 hrs los viernes, y se les ocurrió jugar al juego el palíndromo ganador después del trabajo, en el que generan una palabra al azar S y por turnos van sacando letras de la palabra generada con las que pueden conformar palabras palíndromo, donde finalmente gana quién construye una palabra palíndromo de mayor longitud.

Para eso, primero buscaron en Google para confirmar cómo es una palabra palíndromo, y obtuvieron que una palabra es palíndromo cuando se lee de la misma manera de izquierda a derecha, y de derecha a izquiera.

Cómo por ej: Salas, nidhdin, aabbaa

Previto y Previta muy ñoñamente, construyeron su propio juego y en su primer juego generaron la siguiente palabra:

**a**x**v**a**q**c**v**w**a**v
Luego de 5 vueltas ganó Previta, de la siguiente forma:

> palindromo_ganador(a)
> = palindromo_ganador(av)
> = palindromo_ganador(avq)
> = palindromo_ganador(avqv)
> = palindromo_ganador(avqva)
> = avqva

Previto y Previta, no compartieron su código, y nos dijeron que para ir a pasarla bien a Orrego Luco con ellos debemos primero realizar nuestro propio algoritmo del juego.

### Desafío:

Dado una palabra al azar **S**, debemos construir un algoritmo que simule a Previto **PO** y Previta **PA**,

Por ejemplo:

> N = 856, K = 2, R = super_digit(865856) = super_digit(8 + 6 + 5 + 8 + 5 + 6) = 2

Formato de entrada:

> 856 2

Formato de salida:

> 2

Explicación:

> super_digit(P) = super_digit(8 + 5 + 6 + 8 + 5 +6)
> = super_digit(38)
> = super_digit(3 + 8)
> = super_digit(11)
> = super_digit(1 + 1)
> = super_digit(2)
> = 2

Haz tu mayor esfuerzo y diviértete!
