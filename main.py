from central_recursiva.operacoes import calcular_mdc, somar_digitos
from central_recursiva.validacoes import validar_mdc, validar_soma
from central_recursiva.excecoes import OperacaoInvalida, EntradaInvalida


def processar_operacao(linha):
    partes = linha.split()

    if not partes:
        raise EntradaInvalida

    operacao = partes[0]

    if operacao == "M":
        if len(partes) != 3:
            raise EntradaInvalida

        try:
            a = int(partes[1])
            b = int(partes[2])
        except ValueError:
            raise EntradaInvalida

        validar_mdc(a, b)

        return f"MDC = {calcular_mdc(a, b)}"

    elif operacao == "S":
        if len(partes) != 2:
            raise EntradaInvalida

        try:
            numero = int(partes[1])
        except ValueError:
            raise EntradaInvalida

        validar_soma(numero)

        return f"SOMA = {somar_digitos(numero)}"

    else:
        raise OperacaoInvalida


def main():
    try:
        q = int(input())

        for _ in range(q):
            linha = input()

            try:
                resultado = processar_operacao(linha)
                print(resultado)

            except EntradaInvalida:
                print("ERRO: EntradaInvalida")

            except OperacaoInvalida:
                print("ERRO: OperacaoInvalida")

            finally:
                pass

    except ValueError:
        print("ERRO: EntradaInvalida")

    finally:
        pass


if __name__ == "__main__":
    main()