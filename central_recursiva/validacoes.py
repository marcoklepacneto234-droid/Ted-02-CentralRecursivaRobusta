from .excecoes import EntradaInvalida


def validar_mdc(a, b):
    if a <= 0 or b <= 0:
        raise EntradaInvalida


def validar_soma(numero):
    if numero < 0:
        raise EntradaInvalida