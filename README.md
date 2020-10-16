## Temática: Juego del palíndromo ganador

Previto y Previta, se enteraron de que trabajan hasta las 15:30 hrs los viernes, y se les ocurrió jugar al juego el palíndromo ganador después del trabajo, en el que generan una palabra al azar S y por turnos van sacando letras de la palabra generada con las que pueden conformar palabras palíndromo, donde finalmente gana quién construye una palabra palíndromo de mayor longitud.

Para eso, primero buscaron en Google para confirmar cómo es una palabra palíndromo, y obtuvieron que una palabra es palíndromo cuando se lee de la misma manera de izquierda a derecha, y de derecha a izquierda.

Cómo por ej: Salas, nidhdin, aabbaa

Previto y Previta muy ñoñamente, construyeron su propio juego y en su primer juego generaron la siguiente palabra:

**a**x**v**a**q**c**v**w**a**v
Luego de 5 vueltas ganó Previta, de la siguiente forma:

> palindromo_ganador(a)
> = palindromo_ganador(av)
> = palindromo_ganador(avq)
> = palindromo_ganador(avqv)
> = palindromo_ganador(avqva)
> = PA avqva

Previto y Previta, no compartieron su código, y nos dijeron que para ir a pasarla bien a Orrego Luco con ellos debemos primero realizar nuestro propio algoritmo del juego.

### Desafío:

Se debe construir un algoritmo que simule un juego de Previto **PO** y Previta **PA**, con los siguientes pasos:

1- Ingresar una palabra **S** de largo N < 15

2- Luego por turnos ir obteniendo las letras una por una de la palabra S generada, de izquierda a derecha, comenzando el turno Previta, luego Previto, y así consecutivamente.

3- Una vez que se obtengan todas las letras de cada jugador ( PO y PA), debemos ver cuál de los dos puede obtener una palabra palíndromo de mayour longitud.

4- Finalmente, se debe entregar el nombre del ganador (PO o PA) y la palabra palíndromo generada.

Por ejemplo:

> S =**a**v**k**f**o**e**i**r**o**t**p**h**k**j, R = palindromo_ganador(akoiopk,vferthj) = PA koiok

Formato de entrada:

> avkfoeirotphkj

Formato de salida:

> PA koiok

Explicación:

> palindromo_ganador(avkfoeirotphkj) =palindromo_ganador(akoiopk,vferthj)
> =palindromo_ganador(koiok,null)
> = PA koiok

Haz tu mayor esfuerzo y diviértete!
