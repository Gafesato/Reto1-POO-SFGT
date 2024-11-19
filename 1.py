# @Samuel Fernando Garzón Toro
# Reto 1

"""
He creado una función calculadora con la estructura `match-case` 
para cada operación, gestionando la división entre cero y ninguna 
operación indicada. Se solicitan los 3 datos y al final se muestra 
al usuario la salida.
"""

def calculadora(a: int, b: int, operacion: str) -> float | str:
    """Realiza una operación básica entre dos números."""
    match operacion:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b == 0:
                return "¡División entre 0!"
            return a / b
        case _:
            return "Operación no válida."


print("Bienvenido a la calculadora!")
a: int = int(input("Primer número: "))
b: int = int(input("Segundo número: "))
operacion: str = input("Operación (+, -, *, /): ")
resultado = calculadora(a, b, operacion)
print(f"({a}, {b}, '{operacion}') -> {resultado}")
