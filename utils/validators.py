def validar_pedido(dados):
    produtos = dados.get("produtos", [])
    total = float(dados.get("total", 0))
    if not produtos or len(produtos) == 0:
        return "O pedido deve conter ao menos um produto."
    if total <= 0:
        return "O valor total deve ser maior que zero."
    return None