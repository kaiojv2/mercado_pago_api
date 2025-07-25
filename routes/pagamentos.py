from flask import Blueprint, request, jsonify
from services.mercado_pago import verificar_pagamento_mp, consultar_pagamento
from services.pdf_service import gerar_pdf
from services.historico_service import pagamentos_status, salvar_cache_status, adicionar_historico
from websocket.socket_events import notificar_pix_pago

pagamentos_bp = Blueprint("pagamentos", __name__)

@pagamentos_bp.route("/verificar-pagamento/<int:payment_id>")
def verificar_pagamento(payment_id):
    try:
        status = verificar_pagamento_mp(payment_id)
        return jsonify(status)
    except Exception as e:
        print(f"❌ Erro ao verificar pagamento {payment_id}: {e}")
        return jsonify({"erro": "Erro ao verificar pagamento"}), 500

@pagamentos_bp.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json(force=True)

        if data.get("type") != "payment":
            return "", 200

        pagamento_id = data.get("data", {}).get("id")
        if not pagamento_id:
            print("⚠️ Webhook recebido sem ID do pagamento")
            return "", 200

        pagamento = consultar_pagamento(pagamento_id)
        if not pagamento:
            print(f"⚠️ Pagamento {pagamento_id} não encontrado ao consultar API")
            return "", 200

        if pagamento["status"] == "approved":
            gerar_pdf(
                pagamento_id,
                pagamento["nome"],
                telefone="",
                cpf="",
                endereco="",
                produtos=[],
                valor=pagamento["valor"],
                data_pagamento=pagamento["data"]
            )
            salvar_cache_status()
            notificar_pix_pago(pagamento_id)
            print(f"✅ Pagamento {pagamento_id} aprovado e PDF gerado")
        else:
            print(f"ℹ️ Pagamento {pagamento_id} com status {pagamento['status']}")

        return "", 200

    except Exception as e:
        print(f"❌ Erro no webhook: {e}")
        return "Bad Request", 400
