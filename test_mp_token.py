import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("MP_ACCESS_TOKEN")
if not TOKEN:
    print("❌ MP_ACCESS_TOKEN não encontrado no .env")
    exit(1)

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

url = "https://api.mercadopago.com/v1/payments/search"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("✅ Conexão com Mercado Pago OK!")
    print("Exemplo de pagamentos recentes (primeiros 2):")
    pagamentos = response.json()
    for p in pagamentos.get('results', [])[:2]:
        print(f" - ID: {p['id']}, Status: {p['status']}, Valor: {p['transaction_amount']}")
else:
    print(f"❌ Erro ao acessar Mercado Pago: {response.status_code}")
    print(response.text)
