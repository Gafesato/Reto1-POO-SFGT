# Reto1-POO

Este repositorio contiene los cinco retos del reto 1 de la clase de POO.

## Reto 1: Calculadora
**Descripción:** He creado una función calculadora con la estructura `match-case` 
para cada operación, gestionando la división entre cero y ninguna 
operación indicada. Se solicitan los 3 datos y al final se muestra 
al usuario la salida.
```python
def calculadora(a: int, b: int, operacion: str) -> float:
    match operacion:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b == 0:
                return "División entre 0!"
            return a / b
        case _:
            return "Operación no válida"
```
## Reto 2: Verificación de palíndromos
**Descripción:** He creado una función que verifica si una palabra es un palíndromo 
utilizando dos iteradores: uno desde el inicio y otro desde el final. 
En cada iteración se comparan los caracteres correspondientes; si son 
distintos, se devuelve `False`. Si al terminar el bucle no se encuentran 
diferencias, se retorna `True`.

```python
def verificar_palindromo(palabra: str) -> bool:
    """Verifica si una palabra es un palíndromo."""
    iterador_normal: int = 0
    iterador_reverso: int = len(palabra) - 1

    while iterador_reverso >= iterador_normal:
        if palabra[iterador_reverso] != palabra[iterador_normal]:
            return False
        iterador_normal += 1
        iterador_reverso -= 1

    return True
```

## Reto 3: Números primos
**Descripción:** Hice una función que verifica si los números en una lista son primos. 
Para cada número, se evalúan tres casos: si es menor a 2, si es igual 
a 2, o si es mayor a 2, aquí se calcula la raíz cuadrada del número y 
se verifica si tiene divisores dentro del rango [2, raíz]. Si no tiene
divisores, el número es primo y se añade a la lista de salida.
```python
def verificar_primos(lista_numeros: list[int]) -> list[int]:
    """Filtra los números primos de una lista de enteros."""
    lista_primos: list = []
    for numero in lista_numeros:
        if numero < 2:
            continue  # No es primo si es menor que 2
        elif numero == 2:
            lista_primos.append(numero)  # El 2 es primo
        else:
            primo: bool = True
            # Verificar en el rango del número completo es más largo
            # La raíz es buena aproximación matemática
            raiz: float = (numero**0.5) + 1
            for i in range(2, raiz):
                if numero % i == 0:
                    primo = False
                    break
            if primo:
                lista_primos.append(numero)

    return lista_primos
```

## Reto 4: Mayor suma consecutiva
**Descripción:** La función toma una lista de enteros y calcula la mayor suma
entre dos elementos consecutivos de la lista. Si la lista tiene
menos de dos elementos, retorna 0.
```python
def mayor_suma(lista_enteros: list[int]) -> int:
    """Retorna la mayor suma entre dos elementos consecutivos en una lista."""
    if len(lista_enteros) < 2:
        return 0

    mayor: int = 0  # Inicializar con el menor valor posible
    for i in range(len(lista_enteros) - 1):
        suma: int = lista_enteros[i] + lista_enteros[i + 1]
        if suma > mayor:
            mayor = suma

    return mayor
```

## Reto 5: Palabras con caracteres iguales
**Descripción:** La función toma una lista de palabras e identifica aquellas que tienen los mismos
caracteres, devolviendo solo las palabras que cumplen esta condición. Se utiliza
un bucle bidimensional para comparar pares de palabras mediante sus caracteres
ordenados.
```python
def verificar_palabras(lista_palabras: list[str]) -> list[str]:
    """Retorna las palabras con los mismos caracteres en una lista."""
    lista_palabras_iguales: list[str] = []
    n: int = len(lista_palabras)
    for i in range(n):
        for j in range(i + 1, n):
            palabra_a: str = lista_palabras[i]
            palabra_b: str = lista_palabras[j]
            if sorted(palabra_a) == sorted(palabra_b):
                # Añadir palabras si no están ya en la lista
                if palabra_a not in lista_palabras_iguales:
                    lista_palabras_iguales.append(palabra_a)
                if palabra_b not in lista_palabras_iguales:
                    lista_palabras_iguales.append(palabra_b)

    return lista_palabras_iguales
```

