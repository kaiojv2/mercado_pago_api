from flask import Blueprint, request, jsonify
from services.pdf_service import gerar_pdf
from services.fila_service import incrementar_fila
from services.mercado_pago import criar_cobranca_pix
from services.historico_service import pagamentos_status, salvar_cache_status, adicionar_historico
from utils.validators import validar_pedido
import os
import traceback

pedidos_bp = Blueprint("pedidos", __name__)

@pedidos_bp.route("/criar-pedido", methods=["POST"])
def criar_pedido():
    try:
        dados = request.json
        print("📦 Dados recebidos do front:", dados)
        
        # Valida chave secreta
        if dados.get("chave_secreta") != os.getenv("API_SECRET_KEY"):
            return jsonify({"erro": "Chave secreta inválida"}), 401

        # Validação geral dos dados do pedido
        erro = validar_pedido(dados)
        if erro:
            return jsonify({"erro": erro}), 400

        # Extrai campos do pedido
        nome = dados.get("nome", "Cliente")
        email = dados.get("email", "sememail@teste.com")
        telefone = dados.get("telefone", "")
        cpf = dados.get("cpf", "")
        endereco = dados.get("endereco", "")
        produtos = dados.get("produtos", [])
        valor = float(dados.get("total", 0))
        metodo = dados.get("pagamento", "pix").lower()

        # Incrementa número da fila (pedido)
        numero = incrementar_fila()

        # Gera PDF (mesmo que falhe o pagamento, para controle interno)
        # gerar_pdf(numero, nome, telefone, cpf, endereco, produtos, valor)

        if metodo == "pix":
            retorno = criar_cobranca_pix(numero, nome, email, valor)
            print("DEBUG - retorno criar_cobranca_pix:", retorno)
            if "erro" in retorno:
                return jsonify(retorno), 500

            # Atualiza cache de status em memória
            pagamentos_status[str(retorno.get("txid"))] = "pending"  # ou "pendente"

            # Salva pedido no histórico
            adicionar_historico({
                "numero": numero,
                "nome": nome,
                "telefone": telefone,
                "cpf": cpf,
                "endereco": endereco,
                "produtos": produtos,
                "valor": valor,
                "metodo": metodo,
                "status": "pending",  # status inicial do pagamento
                "txid": retorno.get("txid"),
            })

            # Persiste cache atualizado no disco
            salvar_cache_status()
            
            print("Retornando para frontend:", retorno)
            return jsonify({"pix": retorno, "pedido_numero": numero})

        # Se pagamento for dinheiro ou cartão
        adicionar_historico({
            "numero": numero,
            "nome": nome,
            "telefone": telefone,
            "cpf": cpf,
            "endereco": endereco,
            "produtos": produtos,
            "valor": valor,
            "metodo": metodo,
            "status": "aprovado",  # confirmação imediata
            "txid": None
        })

        return jsonify({"mensagem": f"Pedido via {metodo} registrado.", "pedido_numero": numero})

    except Exception as e:
        print("❌ Erro ao criar pedido:", str(e))
        traceback.print_exc()
        return jsonify({"erro": "Erro interno ao criar pedido"}), 500
