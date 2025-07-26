# 🧾 Sistema de Pedidos com Pix + PDF - Backend Flask

Este projeto é um backend em **Python/Flask** que se conecta a um **app Flutter Web** para processar pedidos de uma lanchonete. Ele suporta pagamentos via **Pix (Mercado Pago)**, **Cartão** ou **Dinheiro**, gera **PDFs personalizados** e envia atualizações em tempo real usando **WebSocket**.

---

## ✅ Funcionalidades

- 🔐 Proteção da API com chave secreta
- 💳 Pagamentos:
  - Pix com geração de QR Code e cópia e cola
  - Cartão ou Dinheiro (PDF gerado diretamente)
- 📡 Comunicação em tempo real com WebSocket
- 🧾 Geração automática de PDFs após pagamento
- 🗃️ Fila de pedidos local em `fila.json`
- 🕓 Histórico de pagamentos salvo em `pagamentos.json`
- 💥 Tratamento de erros com logs
- 🔌 Fácil integração com frontend Flutter via HTTP e Socket.IO

---

## 📂 Estrutura do Projeto

backend/
│
├── app.py # Ponto de entrada do Flask
├── run_eventlet.py # Executa com suporte a WebSocket
├── .env # Variáveis de ambiente
├── requirements.txt # Pacotes necessários
├── fila.json # Armazena pedidos pendentes
├── pagamentos.json # Histórico de pagamentos
│
├── routes/
│ ├── pedidos.py # Endpoint para criar pedido
│ └── pagamentos.py # Verificação de status do Pix
│
├── services/
│ ├── mercado_pago.py # Integração com API do Mercado Pago
│ ├── pdf_service.py # Geração de PDFs dos pedidos
│ ├── fila_service.py # Controle da fila de pedidos
│ ├── historico_service.py # Controle e cache de pagamentos
│
├── socket/
│ └── socket_events.py # Envia atualizações para o frontend
│
└── utils/
└── validators.py # Validação dos dados recebidos



## ⚙️ Instalação e Execução

### 1. Clone o repositório


git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo

2. Crie e ative o ambiente virtual
bash
Copiar
Editar
python -m venv venv
venv\Scripts\activate  # No Windows

4. Instale as dependências
bash
Copiar
Editar
pip install -r requirements.txt

6. Configure o .env
Crie um arquivo .env na raiz do projeto com:

ini
Copiar
Editar
MERCADO_PAGO_TOKEN=SEU_TOKEN_AQUI
CHAVE_SECRETA=SUA_CHAVE_SECRETA
PASTA_PDFS=./pdfs
Obs: Crie a pasta pdfs/ se ainda não existir.

5. Inicie o servidor com suporte a WebSocket
bash
Copiar
Editar
python run_eventlet.py
O servidor estará rodando em:

arduino
Copiar
Editar
http://localhost:5000
🔁 Fluxo de Funcionamento
Para pagamento via Pix:
O Flutter envia um POST para /criar-pedido com os dados do cliente, itens e pagamento.

O backend cria uma cobrança Pix via Mercado Pago.

Retorna QR Code e código "copia e cola" via WebSocket.

Monitora o status da cobrança.

Ao ser confirmado, o backend:

Gera um PDF do pedido

Atualiza a fila e histórico

Envia confirmação ao Flutter via WebSocket

Para pagamento Cartão/Dinheiro:
Flutter envia o pedido com método "cartao" ou "dinheiro".

O backend gera o PDF direto (sem esperar confirmação).

Pedido entra na fila.

🧪 Testando com cURL (Exemplo)
bash
Copiar
Editar
curl -X POST http://localhost:5000/criar-pedido \
-H "Content-Type: application/json" \
-d "{
  \"nome\": \"João Silva\",
  \"telefone\": \"(11) 91234-5678\",
  \"endereco\": \"Rua A, 123\",
  \"cpf\": \"12345678900\",
  \"metodo_pagamento\": \"pix\",
  \"itens\": [
    {\"nome\": \"Hamburguer\", \"quantidade\": 2, \"preco\": 15.00},
    {\"nome\": \"Refrigerante\", \"quantidade\": 1, \"preco\": 5.00}
  ],
  \"chave_secreta\": \"SUA_CHAVE_SECRETA\"
}"
💬 Comunicação em Tempo Real
O frontend se conecta via Socket.IO

Canal padrão: /

Eventos:

status_pagamento → usado para atualizar a interface

confirmado → indica que o Pix foi pago

erro → em caso de falha no pagamento

🧠 Dicas
Use ngrok se quiser expor o servidor para testes externos:

bash
Copiar
Editar
ngrok http 5000
Teste o PDF gerado na pasta definida em PASTA_PDFS

Os arquivos .json mantêm o estado entre execuções

❗ Requisitos
Python 3.10 ou superior

Conta no Mercado Pago

Token Pix com permissões de cobrança

Instalar dependências com pip

📌 To-Do Futuro
 Impressão automática local

 Painel de administração dos pedidos

 Suporte a múltiplas lojas ou caixas

📄 Licença
Este projeto é livre para uso pessoal e educacional.

👤 Autor
Kaio Costa
Desenvolvedor Full Stack
