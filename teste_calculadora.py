import pytest
from calculadora import somar, subtrair, multiplicar, dividir

def test_dividir_caminho_feliz():

    a = 20
    b = 4
    resultado_esperado = 5
    resultado = dividir(a, b)
    #verificar
    assert resultado == resultado_esperado

def test_dividir_limite_zero():
    a = 0
    b = 5
    resultado_esperado = 0
    #EXECUÇÃO
    resultado_obtido = dividir(a, b)
    #verificação
    assert resultado_obtido == resultado_esperado

def test_dividir_excecao_divisao_por_zero():
    a = 10
    b = 0
    #EXECUÇÃO E VERIFICAÇÃO
    with pytest.raises(ValueError) as excecao:
        dividir(a, b)
    assert str(excecao.value) == "Divisão por zero não é permitida."

import pytest
from calculadora import somar, subtrair, multiplicar, dividir

# --- TESTES DE DIVISÃO (já existentes) ---

def test_dividir_caminho_feliz():
    a = 20
    b = 4
    resultado_esperado = 5
    resultado = dividir(a, b)
    #verificar
    assert resultado == resultado_esperado

def test_dividir_limite_zero():
    a = 0
    b = 5
    resultado_esperado = 0
    #EXECUÇÃO
    resultado_obtido = dividir(a, b)
    #verificação
    assert resultado_obtido == resultado_esperado

def test_dividir_excecao_divisao_por_zero():
    a = 10
    b = 0
    #EXECUÇÃO E VERIFICAÇÃO
    with pytest.raises(ValueError) as excecao:
        dividir(a, b)
    assert str(excecao.value) == "Divisão por zero não é permitida."


# --- NOVOS TESTES: SOMAR ---

def test_somar_caminho_feliz():
    a = 10
    b = 10
    resultado_esperado = 20
    resultado = somar(a, b)
    assert resultado == resultado_esperado

def test_somar_valores_negativos():
    a = -5
    b = 3
    resultado_esperado = -2
    resultado = somar(a, b)
    assert resultado == resultado_esperado


# --- NOVOS TESTES: SUBTRAIR ---

def test_subtrair_caminho_feliz():
    a = 10
    b = 5
    resultado_esperado = 5
    resultado = subtrair(a, b)
    assert resultado == resultado_esperado

def test_subtrair_valores_negativos():
    a = -10
    b = -10
    resultado_esperado = 0
    resultado = subtrair(a, b)
    assert resultado == resultado_esperado

def test_subtrair_valores_polos_alternados():
    a = 5
    b = -10
    resultado_esperado = 15  # 5 - (-10) = 5 + 10 = cl15 (conforme a lógica matemática padrão do Python)
    resultado = subtrair(a, b)
    assert resultado == resultado_esperado


# --- NOVOS TESTES: MULTIPLICAR ---

def test_multiplicar_caminho_feliz():
    a = 2
    b = 5
    resultado_esperado = 10
    resultado = multiplicar(a, b)
    assert resultado == resultado_esperado

def test_multiplicar_por_zero():
    a = 10
    b = 0
    resultado_esperado = 0
    resultado = multiplicar(a, b)
    assert resultado == resultado_esperado

def test_multiplicar_elemento_neutro():
    a = 85
    b = 1
    resultado_esperado = 85
    resultado = multiplicar(a, b)
    assert resultado == resultado_esperado