import requests
import os
import uuid
from services.historico_service import pagamentos_status, salvar_cache_status, adicionar_historico
from dotenv import load_dotenv


load_dotenv()


BASE = "https://api.mercadopago.com"
HEADERS = {
    "Authorization": f"Bearer {os.getenv('MP_ACCESS_TOKEN')}",
    "Content-Type": "application/json"
}

def criar_cobranca_pix(numero, nome, email, valor):
    payload = {
        "transaction_amount": valor,
        "payment_method_id": "pix",
        "description": f"Pedido #{numero}",
        "payer": {
            "email": email,
            "first_name": nome,
            "last_name": ""  # Opcional
        }
    }

    headers_local = HEADERS.copy()
    headers_local["X-Idempotency-Key"] = str(uuid.uuid4())

    try:
        r = requests.post(f"{BASE}/v1/payments", json=payload, headers=headers_local)
        if r.status_code != 201:
            return {"erro": r.text}

        data = r.json()

        pagamentos_status[str(data["id"])] = data["status"]
        salvar_cache_status()

        pedido = {
            "numero": numero,
            "nome": nome,
            "email": email,
            "valor": valor,
            "txid": str(data["id"]),
            "status": data["status"]
        }
        adicionar_historico(pedido)

        imagem_com_prefixo = "data:image/png;base64," + data["point_of_interaction"]["transaction_data"]["qr_code_base64"]

        print("📲 Retorno do criar_cobranca_pix:", {
            "imagem_qrcode_base64": imagem_com_prefixo,
            "chave_copia_cola": data["point_of_interaction"]["transaction_data"]["qr_code"],
            "txid": str(data["id"]),
            "status": data["status"]
        })

        return {
            "imagem_qrcode_base64": imagem_com_prefixo,
            "chave_copia_cola": data["point_of_interaction"]["transaction_data"]["qr_code"],
            "txid": str(data["id"]),
            "status": data["status"]
        }

    except requests.RequestException as e:
        return {"erro": f"Erro na requisição: {str(e)}"}
    
def verificar_pagamento_mp(payment_id):
    # Retorna rápido se o status já estiver aprovado no cache local
    if pagamentos_status.get(str(payment_id)) == "approved":
        return {"status": "approved"}

    try:
        r = requests.get(f"{BASE}/v1/payments/{payment_id}", headers=HEADERS)
        if r.status_code == 200:
            data = r.json()
            pagamentos_status[str(payment_id)] = data["status"]
            salvar_cache_status()
            return {"status": data["status"]}
        else:
            return {"erro": r.text}
    except requests.RequestException as e:
        return {"erro": f"Erro na requisição: {str(e)}"}

def consultar_pagamento(payment_id):
    try:
        r = requests.get(f"{BASE}/v1/payments/{payment_id}", headers=HEADERS)
        if r.status_code == 200:
            p = r.json()
            return {
                "status": p["status"],
                "valor": p["transaction_amount"],
                "nome": p.get("payer", {}).get("first_name", ""),
                "data": p.get("date_approved", "")
            }
        else:
            return None
    except requests.RequestException:
        return None
