from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from config import PASTA_PDF
import os

def gerar_pdf(pedido_numero, nome_cliente, telefone, cpf, endereco, produtos, valor, tipo_pagamento, data_pagamento=None):
    # Garante que a pasta existe
    if not os.path.exists(PASTA_PDF):
        os.makedirs(PASTA_PDF)
    
    filename = os.path.join(PASTA_PDF, f"pedido_{pedido_numero}.pdf")
    c = canvas.Canvas(filename, pagesize=letter)

    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 780, f"Nota Fiscal - Pedido #{pedido_numero}")

    c.setFont("Helvetica", 12)
    c.drawString(100, 750, f"Cliente: {nome_cliente}")
    c.drawString(100, 735, f"Telefone: {telefone}")

    # Mostrar CPF somente se for PIX
    if tipo_pagamento.lower() == "pix" and cpf:
        c.drawString(100, 720, f"CPF: {cpf}")
        linha_endereco = 705
    else:
        linha_endereco = 720  # sobe endereço se não mostrar CPF
    
    c.drawString(100, linha_endereco, f"Endereço: {endereco}")

    c.drawString(100, linha_endereco - 25, f"Tipo de pagamento: {tipo_pagamento.capitalize()}")

    c.drawString(100, linha_endereco - 50, "Produtos:")

    altura = linha_endereco - 65
    max_produtos = 25  # limitar quantidade para não sair da página

    for i, p in enumerate(produtos):
        if i >= max_produtos:
            c.drawString(110, altura, "... mais produtos não exibidos ...")
            break
        c.drawString(110, altura, f"- {p}")
        altura -= 15

    c.drawString(100, altura - 10, f"Total: R$ {valor:.2f}")

    if data_pagamento:
        c.drawString(100, altura - 30, f"Data do pagamento: {data_pagamento}")

    c.save()
    print(f"📄 PDF gerado: {filename}")
