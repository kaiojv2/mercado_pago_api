import json
import os

ARQUIVO_FILA = "fila.json"

def carregar_fila():
    if os.path.exists(ARQUIVO_FILA):
        try:
            with open(ARQUIVO_FILA, "r") as f:
                fila = json.load(f)
            # Se a chave não existir, inicializa
            if "ultimo_numero" not in fila:
                fila["ultimo_numero"] = 0
        except json.JSONDecodeError:
            # arquivo vazio ou corrompido
            fila = {"ultimo_numero": 0}
    else:
        fila = {"ultimo_numero": 0}
    return fila

fila = carregar_fila()

def salvar_fila():
    with open(ARQUIVO_FILA, "w") as f:
        json.dump(fila, f, indent=2)

def incrementar_fila():
    fila["ultimo_numero"] += 1
    salvar_fila()
    return fila["ultimo_numero"]
