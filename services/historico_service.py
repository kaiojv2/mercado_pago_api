import json
import os

CAMINHO_HISTORICO = "pagamentos.json"        # arquivo com lista histórica de pedidos
CAMINHO_CACHE = "pagamentos_cache.json"      # arquivo com cache dos status atuais dos pagamentos

# Cache em memória dos status dos pagamentos
pagamentos_status = {}

def salvar_cache_status():
    """
    Salva o conteúdo do cache pagamentos_status no arquivo CAMINHO_CACHE.
    """
    try:
        with open(CAMINHO_CACHE, "w", encoding="utf-8") as f:
            json.dump(pagamentos_status, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Erro ao salvar cache de status: {e}")

def carregar_cache_status():
    """
    Carrega o cache pagamentos_status do arquivo CAMINHO_CACHE para memória.
    """
    global pagamentos_status
    if os.path.exists(CAMINHO_CACHE):
        try:
            with open(CAMINHO_CACHE, "r", encoding="utf-8") as f:
                pagamentos_status = json.load(f)
                if not isinstance(pagamentos_status, dict):
                    pagamentos_status = {}
        except Exception as e:
            print(f"Erro ao carregar cache de status: {e}")
            pagamentos_status = {}

def adicionar_historico(pedido):
    """
    Adiciona um pedido individual ao arquivo de histórico (lista de pedidos).
    """
    historico = []
    if os.path.exists(CAMINHO_HISTORICO):
        try:
            with open(CAMINHO_HISTORICO, "r", encoding="utf-8") as f:
                historico = json.load(f)
                if not isinstance(historico, list):
                    historico = []
        except json.JSONDecodeError:
            historico = []

    historico.append(pedido)

    try:
        with open(CAMINHO_HISTORICO, "w", encoding="utf-8") as f:
            json.dump(historico, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Erro ao salvar histórico de pedidos: {e}")
