def calcular_mdc(a, b):
    if b == 0:
        return a

    return calcular_mdc(b, a % b)


def somar_digitos(numero):
    if numero < 10:
        return numero

    return (numero % 10) + somar_digitos(numero // 10)