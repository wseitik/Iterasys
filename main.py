# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# 1 imports - bibliotecas
# 2 - class - classes
import pytest



# 3 - definitions - definiçoes = metodos

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Oi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.

def somar(numero1, numero2):
    return numero1 + numero2


def subtrair(numero1, numero2):
    return numero1 - numero2


def multiplicar(numero1, numero2):
    return numero1 * numero2


def dividir(numero1, numero2):
    if numero2 != 0:
        return numero1 / numero2
    else:
        return 'Nao dividiras por 0'


# unit test

# teste da função somar


def test_somar_didatico():
    # 1 - Configurar / Preparar
    numero1 = 8  # input
    numero2 = 5  # input
    resultado_esperado = 13  # output

    # 2 - Executar
    resultado_atual = somar(numero1, numero2)

    # 3 Validação
    assert resultado_atual == resultado_esperado

@pytest.mark.parametrize('numero1, numero2, resultado', [
    # valores
    (5, 4, 9),  # test 1
    (3, 2, 5),  # test 2
    (10, 6, 16),  # test 3
])

def test_somar(numero1, numero2, resultado):
    assert somar(numero1, numero2) == resultado


def test_somar_negativo():
    assert somar(-1000, -2000) == -3000


def test_subtrair():
    assert subtrair(4, 5) == -1


def test_multiplicar():
    assert multiplicar(3, 3) == 9


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Wilson')

    resultado = somar(2, 4)
    print('O resultado da soma é: ' + str(resultado))

    resultado = subtrair(10, 2)
    print(f'O resultado da subtração é: {resultado}')

    resultado = multiplicar(2, 8)
    print(f'O resultado da multiplicação é: {resultado}')

    resultado = dividir(4, 0)
    print(f'O resultado da divisão é: {resultado}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
