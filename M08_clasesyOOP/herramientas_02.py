

def factorial(self, numero):
    if(type(numero) != int):
        return 'El numero debe ser un entero'
    if(numero < 0):
        return 'El numero debe ser pisitivo'
    if (numero > 1):
        numero = numero * self.__factorial(numero - 1)
    return numero