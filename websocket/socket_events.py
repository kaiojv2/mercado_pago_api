from flask_socketio import join_room, rooms, emit, disconnect
from flask import request

def socketio_config(socketio):
    @socketio.on("entrar_na_sala")
    def handle_entrar_na_sala(data):
        txid = data.get("txid")
        sid = request.sid  # ID da conexão atual do socket

        if not txid:
            print("⚠️ Nenhum TXID fornecido para entrar na sala")
            return

        sala = str(txid)
        if sala not in rooms(sid):  # rooms(sid) retorna as salas que esse socket já está
            join_room(sala)
            print(f"🟢 Cliente {sid} entrou na sala: {sala}")
        else:
            print(f"🔁 Cliente {sid} já está na sala: {sala}")

def notificar_pix_pago(txid):
    from app import socketio  # Importa aqui para evitar importação circular
    print(f"📢 Notificando frontend pagamento aprovado para txid: {txid}")
    socketio.emit("pix_pago", {"txid": txid}, room=str(txid))
