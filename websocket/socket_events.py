from flask_socketio import join_room

def socketio_config(socketio):
    @socketio.on("entrar_na_sala")
    def handle_entrar_na_sala(data):
        txid = data.get("txid")
        if txid:
            join_room(str(txid))
            print(f"🟢 Cliente entrou na sala: {txid}")
        if not txid:
            print("⚠️ Nenhum TXID fornecido para entrar na sala")
        return
def notificar_pix_pago(txid):
    from app import socketio  # Importa aqui para evitar importação circular
    print(f"📢 Notificando frontend pagamento aprovado para txid: {txid}")
    socketio.emit("pix_pago", {"txid": txid}, room=str(txid))
