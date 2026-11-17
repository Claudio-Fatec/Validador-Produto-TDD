def validar_quantidade_fotos(qtd_fotos):
    # Deve ter no mínimo 3 fotos do produto
    return qtd_fotos >= 3

def validar_estoque(estoque):
    # A quantidade de estoque nunca pode ser negativa
    return estoque >= 0

def validar_tamanho_descricao(descricao):
    return len(descricao) <= 255 
        

def validar_produto(qtd_fotos, estoque, descricao):
    if  validar_quantidade_fotos(qtd_fotos) == False:
        return False
    if  validar_estoque(estoque) == False:
        return False
    if  validar_tamanho_descricao(descricao) == False:
        return False
    return True