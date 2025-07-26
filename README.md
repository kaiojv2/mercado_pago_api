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


📂 Project Index
MERCADO_PAGO_API.GIT/
🚀 Getting Started
☑️ Prerequisites
Before getting started with mercado_pago_api.git, ensure your runtime environment meets the following requirements:

Programming Language: Python 3.8+

Package Manager: Pip

⚙️ Installation
Install mercado_pago_api.git using one of the following methods:

Build from source:

Clone the mercado_pago_api.git repository:

Bash

❯ git clone [https://github.com/kaiojv2/mercado_pago_api.git](https://github.com/kaiojv2/mercado_pago_api.git)
Navigate to the project directory:

Bash

❯ cd mercado_pago_api.git
Install the project dependencies:

Using pip   

Bash

❯ pip install -r requirements.txt
🤖 Usage
To run the Mercado Pago API project, you'll primarily use the run_eventlet.py script, which leverages eventlet for asynchronous operations. You'll also need to configure your Mercado Pago credentials.

1. Configure Mercado Pago Credentials
Before running the application, you need to set your Mercado Pago Public Key and Access Token as environment variables.

MERCADO_PAGO_PUBLIC_KEY: Your Mercado Pago Public Key.

MERCADO_PAGO_ACCESS_TOKEN: Your Mercado Pago Access Token.

On Linux/macOS:

Bash

export MERCADO_PAGO_PUBLIC_KEY="YOUR_PUBLIC_KEY"
export MERCADO_PAGO_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
On Windows (Command Prompt):

DOS

set MERCADO_PAGO_PUBLIC_KEY="YOUR_PUBLIC_KEY"
set MERCADO_PAGO_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
On Windows (PowerShell):

PowerShell

$env:MERCADO_PAGO_PUBLIC_KEY="YOUR_PUBLIC_KEY"
$env:MERCADO_PAGO_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
Replace "YOUR_PUBLIC_KEY" and "YOUR_ACCESS_TOKEN" with your actual Mercado Pago credentials.

2. Run the Application
Once your environment variables are set, you can run the application:

Using python with run_eventlet.py   

Bash

❯ python run_eventlet.py
This command will start the Flask application with eventlet as the WSGI server, typically on http://127.0.0.1:5000.

3. Exposing Your Local Server (Optional, for Webhooks)
If you need to receive webhooks from Mercado Pago (e.g., for payment notifications), your local server needs to be accessible from the internet. You can use ngrok for this purpose.

Download ngrok: If you don't have it, download ngrok from ngrok.com.

Unzip ngrok: Extract the ngrok.exe (or ngrok for Linux/macOS) to a convenient location, or directly into the ngrok folder within this project.

Run ngrok: In a new terminal, navigate to your mercado_pago_api.git directory and then into the ngrok directory, and run:

Bash

❯ cd ngrok
❯ ./ngrok http 5000
This will provide you with a public URL (e.g., https://xxxxxx.ngrok-free.app). You can then configure this URL in your Mercado Pago application settings for webhooks.

🧪 Testing
Run the test suite using the following command:
Using pytest   

Bash

❯ pytest
📌 Project Roadmap
[X] Task 1: Implement feature one.

[ ] Task 2: Implement feature two.

[ ] Task 3: Implement feature three.

🔰 Contributing
💬 Join the Discussions: Share your insights, provide feedback, or ask questions.

🐛 Report Issues: Submit bugs found or log feature requests for the mercado_pago_api.git project.

💡 Submit Pull Requests: Review open PRs, and submit your own PRs.

Contributing Guidelines
Contributor Graph
🎗 License
This project is protected under the MIT License. For more details, refer to the LICENSE file.

🙌 Acknowledgments
Mercado Pago Developers Site: For comprehensive API documentation and guides.

Flask Community: For the robust web framework.

Eventlet: For enabling efficient asynchronous operations.

PyInstaller: For simplifying application distribution.
