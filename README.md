<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">MERCADO_PAGO_API.GIT</h1></p>
<p align="center">
	<em>`❯ A robust API for managing Mercado Pago payments, orders, and notifications.`</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/kaiojv2/mercado_pago_api.git?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/kaiojv2/mercado_pago_api.git?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/kaiojv2/mercado_pago_api.git?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/kaiojv2/mercado_pago_api.git?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"></p>
<p align="center">
	</p>
<br>

## 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
  - [🧪 Testing](#-testing)
- [📌 Project Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

`❯ The Mercado Pago API project provides a comprehensive solution for integrating with Mercado Pago's payment gateway. It allows for the creation and management of payments, orders, and handles real-time notifications via websockets. The API is designed to be highly modular and efficient, using `eventlet` for asynchronous operations to ensure high performance and responsiveness.`

---

## 👾 Features

`❯` This project offers the following key features:
* **Mercado Pago Integration:** Seamlessly create and manage payments and orders through Mercado Pago.
* **Webhook Handling:** Process real-time payment notifications from Mercado Pago.
* **Order Queue Management:** Utilizes a robust queuing system to handle payment processing efficiently.
* **Payment History:** Maintains a detailed history of all transactions.
* **PDF Generation:** Generate payment receipts or reports in PDF format.
* **WebSocket Notifications:** Real-time updates on payment status changes.
* **Modular Design:** Clearly separated concerns for routes, services, and utilities for easy maintenance and scalability.

---

## 📁 Project Structure

```sh
└── mercado_pago_api.git/
    ├── README.md
    ├── __pycache__
    │   ├── app.cpython-313.pyc
    │   └── config.cpython-313.pyc
    ├── app.py
    ├── build
    │   ├── run_eventlet
    │   └── run_waitress
    ├── dist
    │   └── run_eventlet.exe
    ├── estrutura_projeto.txt
    ├── fila.json
    ├── ngrok
    │   ├── ngrok http 5000.txt
    │   └── ngrok.exe
    ├── pagamentos.json
    ├── pagamentos_cache.json
    ├── requirements.txt
    ├── routes
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── pagamentos.py
    │   └── pedidos.py
    ├── run_eventlet.py
    ├── run_eventlet.spec
    ├── services
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── fila_service.py
    │   ├── historico_service.py
    │   ├── mercado_pago.py
    │   └── pdf_service.py
    ├── test_mp_token.py
    ├── utils
    │   ├── __init__.py
    │   ├── __pycache__
    │   └── validators.py
    └── websocket
        ├── __init__.py
        ├── __pycache__
        └── socket_events.py
