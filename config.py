import os

API_SECRET_KEY = ""
PASTA_PDF = "notas_pedidos"

if not os.path.exists(PASTA_PDF):
    os.makedirs(PASTA_PDF)