class Numero:
    def __init__(self, valor):
        self._numero = None
        self.numero = valor
    @property  # Getter
    def numero(self):
        return self._numero

    @numero.setter  # Setter
    def numero(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("El número debe ser un entero positivo.")
        self._numero = value

def gcd(a, b):
    """
    Calcula el Máximo Común Divisor (MCD) de dos números enteros positivos utilizando el algoritmo de Euclides.

    Args:
    a (int): El primer número entero positivo.
    b (int): El segundo número entero positivo.

    Returns:
    int: El MCD de a y b.
    """
    while b != 0:
        a, b = b, a % b
    return a


def solicitar_numero(mensaje):
    """
    Solicita entrada de usuario para un número entero positivo.
    """
    while True:
        try:
            num = int(input(mensaje))
            return Numero(num)  # Retorna una instancia de Numero
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
        except Exception as e:
            print(e)

# Solicitar entrada de usuario para el primer número
num1 = solicitar_numero("Ingrese el primer número entero positivo: ")

# Solicitar entrada de usuario para el segundo número
num2 = solicitar_numero("Ingrese el segundo número entero positivo: ")


# Calcular y mostrar el MCD
print(f"El Máximo Común Divisor de {num1.numero} y {num2.numero} es: {gcd(num1.numero, num2.numero)}")
