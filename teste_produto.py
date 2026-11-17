from validar_produto import (
    validar_quantidade_fotos,
    validar_estoque,
    validar_tamanho_descricao,
    validar_produto
)
 
def test_validar_quantidade_fotos():
    qtd_fotos = 2
    resultado_esperado = False
 
    resultado_obtido = validar_quantidade_fotos(qtd_fotos)
 
    assert resultado_obtido == resultado_esperado
 
def test_validar_estoque():
    estoque = -5
    resultado_esperado = False
 
    resultado_obtido = validar_estoque(estoque)
 
    assert resultado_obtido == resultado_esperado
 
def test_validar_tamanho_descricao():
    descricao = "a" * 256
    resultado_esperado = False
 
    resultado_obtido = validar_tamanho_descricao(descricao)
 
    assert resultado_obtido == resultado_esperado
 
def test_validar_produto_caminho_feliz():
    qtd_fotos = 4
    estoque = 50
    descricao = "Produto de alta qualidade"
    resultado_esperado = True
 
    resultado_obtido = validar_produto(qtd_fotos, estoque, descricao)
 
    assert resultado_obtido == resultado_esperado