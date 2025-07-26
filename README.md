<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">MERCADO_PAGO_API.GIT</h1></p>
<p align="center">
	<em><code>❯ A robust API for managing Mercado Pago payments, orders, and notifications.</code></em>
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


### 📂 Project Index

\<details open\>
\<summary\>\<b\>\<code\>MERCADO\_PAGO\_API.GIT/\</code\>\</b\>\</summary\>
\<details\> \<summary\>\<b\>**root**\</b\>\</summary\>
\<blockquote\>
\<table\>
\<tr\>
\<td\>\<b\>\<a href='https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/run\_eventlet.py'\>run\_eventlet.py\</a\>\</b\>\</td\>
\<td\>\<code\>❯ The main entry point for running the application with Eventlet, a high-performance networking library.\</code\>\</td\>
\</tr\>
\<tr\>
\<td\>\<b\>\<a href='https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/run\_eventlet.spec'\>run\_eventlet.spec\</a\>\</b\>\</td\>
\<td\>\<code\>❯ PyInstaller specification file for building the `run_eventlet` executable.\</code\>\</td\>
\</tr\>
\<tr\>
\<td\>\<b\>\<a href='https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/fila.json'\>fila.json\</a\>\</b\>\</td\>
\<td\>\<code\>❯ A JSON file used to store the queue of pending payment processing tasks.\</code\>\</td\>
\</tr\>
\<tr\>
\<td\>\<b\>\<a href='https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/app.py'\>app.py\</a\>\</b\>\</td\>
\<td\>\<code\>❯ The core Flask application file, setting up the main application instance and configurations.\</code\>\</td\>
\</tr\>
\<tr\>
\<td\>\<b\>\<a href='https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/pagamentos\_cache.json'\>pagamentos\_cache.json\</a\>\</b\>\</td\>
\<td\>\<code\>❯ A temporary cache file for storing payment information to improve performance.\</code\>\</td\>
\</tr\>
\<tr\>
\<td\>\<b\>\<a href='https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/pagamentos.json'\>pagamentos.json\</a\>\</b\>\</td\>
\<td\>\<code\>❯ A JSON file used as a simple database to persist payment records.\</code\>\</td\>
\</tr\>
\<tr\>
\<td\>\<b\>\<a href='https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/requirements.txt'\>requirements.txt\</a\>\</b\>\</td\>
\<td\>\<code\>❯ Lists all Python dependencies required to run the project.\</code\>\</td\>
\</tr\>
\<tr\>
\<td\>\<b\>\<a href='https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/test\_mp\_token.py'\>test\_mp\_token.py\</a\>\</b\>\</td\>
\<td\>\<code\>❯ A script for testing Mercado Pago API token validity.\</code\>\</td\>
\</tr\>
\<tr\>
\<td\>\<b\>\<a href='https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/estrutura\_projeto.txt'\>estrutura\_projeto.txt\</a\>\</b\>\</td\>
\<td\>\<code\>❯ A text file potentially outlining the project's architectural structure or notes.\</code\>\</td\>
\</tr\>
\</table\>
\</blockquote\>
\</details\>
\<details\> \<summary\>\<b\>ngrok\</b\>\</summary\>
\<blockquote\>
\<table\>
\<tr\>
\<td\>\<b\>\<a href='https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/ngrok/ngrok http 5000.txt'\>ngrok http 5000.txt\</a\>\</b\>\</td\>
\<td\>\<code\>❯ Instructions or a script for exposing the local server (on port 5000) to the internet using ngrok.\</code\>\</td\>
\</tr\>
\<tr\>
\<td\>\<b\>\<a href='https://www.google.com/search?q=https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/ngrok/ngrok.exe'\>ngrok.exe\</a\>\</b\>\</td\>
\<td\>\<code\>❯ The executable for the ngrok tunneling service.\</code\>\</td\>
\</tr\>
\</table\>
\</blockquote\>
\</details\>
\<details\> \<summary\>\<b\>build\</b\>\</summary\>
\<blockquote\>
\<details\>
\<summary\>\<b\>run\_eventlet\</b\>\</summary\>
\<blockquote\>
\<table\>
\<tr\>
\<td\>\<b\>\<a href='https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/build/run\_eventlet/xref-run\_eventlet.html'\>xref-run\_eventlet.html\</a\>\</b\>\</td\>
\<td\>\<code\>❯ Cross-reference HTML report generated by PyInstaller.\</code\>\</td\>
\</tr\>
\<tr\>
\<td\>\<b\>\<a href='https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/build/run\_eventlet/PKG-00.toc'\>PKG-00.toc\</a\>\</b\>\</td\>
\<td\>\<code\>❯ PyInstaller table of contents for bundled packages.\</code\>\</td\>
\</tr\>
\<tr\>
\<td\>\<b\>\<a href='https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/build/run\_eventlet/warn-run\_eventlet.txt'\>warn-run\_eventlet.txt\</a\>\</b\>\</td\>
\<td\>\<code\>❯ Warning log file from the PyInstaller build process.\</code\>\</td\>
\</tr\>
\<tr\>
\<td\>\<b\>\<a href='https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/build/run\_eventlet/Analysis-00.toc'\>Analysis-00.toc\</a\>\</b\>\</td\>
\<td\>\<code\>❯ PyInstaller analysis data table of contents.\</code\>\</td\>
\</tr\>
\<tr\>
\<td\>\<b\>\<a href='https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/build/run\_eventlet/run\_eventlet.pkg'\>run\_eventlet.pkg\</a\>\</b\>\</td\>
\<td\>\<code\>❯ PyInstaller package file containing bundled code and data.\</code\>\</td\>
\</tr\>
\<tr\>
\<td\>\<b\>\<a href='https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/build/run\_eventlet/EXE-00.toc'\>EXE-00.toc\</a\>\</b\>\</td\>
\<td\>\<code\>❯ PyInstaller executable table of contents.\</code\>\</td\>
\</tr\>
\<tr\>
\<td\>\<b\>\<a href='https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/build/run\_eventlet/PYZ-00.pyz'\>PYZ-00.pyz\</a\>\</b\>\</td\>
\<td\>\<code\>❯ PyInstaller archive of compiled Python modules.\</code\>\</td\>
\</tr\>
\<tr\>
\<td\>\<b\>\<a href='https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/build/run\_eventlet/PYZ-00.toc'\>PYZ-00.toc\</a\>\</b\>\</td\>
\<td\>\<code\>❯ PyInstaller table of contents for the PYZ archive.\</code\>\</td\>
\</tr\>
\</table\>
\</blockquote\>
\</details\>
\<details\>
\<summary\>\<b\>run\_waitress\</b\>\</summary\>
\<blockquote\>
\<table\>
\<tr\>
\<td\>\<b\>\<a href='https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/build/run\_waitress/PKG-00.toc'\>PKG-00.toc\</a\>\</b\>\</td\>
\<td\>\<code\>❯ PyInstaller table of contents for bundled packages when built with Waitress.\</code\>\</td\>
\</tr\>
\<tr\>
\<td\>\<b\>\<a href='https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/build/run\_waitress/Analysis-00.toc'\>Analysis-00.toc\</a\>\</b\>\</td\>
\<td\>\<code\>❯ PyInstaller analysis data table of contents when built with Waitress.\</code\>\</td\>
\</tr\>
\<tr\>
\<td\>\<b\>\<a href='https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/build/run\_waitress/EXE-00.toc'\>EXE-00.toc\</a\>\</b\>\</td\>
\<td\>\<code\>❯ PyInstaller executable table of contents when built with Waitress.\</code\>\</td\>
\</tr\>
\<tr\>
\<td\>\<b\>\<a href='https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/build/run\_waitress/run\_waitress.pkg'\>run\_waitress.pkg\</a\>\</b\>\</td\>
\<td\>\<code\>❯ PyInstaller package file containing bundled code and data when built with Waitress.\</code\>\</td\>
\</tr\>
\<tr\>
\<td\>\<b\>\<a href='https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/build/run\_waitress/warn-run\_waitress.txt'\>warn-run\_waitress.txt\</a\>\</b\>\</td\>
\<td\>\<code\>❯ Warning log file from the PyInstaller build process when built with Waitress.\</code\>\</td\>
\</tr\>
\<tr\>
\<td\>\<b\>\<a href='https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/build/run\_waitress/xref-run\_waitress.html'\>xref-run\_waitress.html\</a\>\</b\>\</td\>
\<td\>\<code\>❯ Cross-reference HTML report generated by PyInstaller when built with Waitress.\</code\>\</td\>
\</tr\>
\<tr\>
\<td\>\<b\>\<a href='https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/build/run\_waitress/PYZ-00.pyz'\>PYZ-00.pyz\</a\>\</b\>\</td\>
\<td\>\<code\>❯ PyInstaller archive of compiled Python modules when built with Waitress.\</code\>\</td\>
\</tr\>
\<tr\>
\<td\>\<b\>\<a href='https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/build/run\_waitress/PYZ-00.toc'\>PYZ-00.toc\</a\>\</b\>\</td\>
\<td\>\<code\>❯ PyInstaller table of contents for the PYZ archive when built with Waitress.\</code\>\</td\>
\</tr\>
\</table\>
\</blockquote\>
\</details\>
\</blockquote\>
\</details\>
\<details\> \<summary\>\<b\>websocket\</b\>\</summary\>
\<blockquote\>
\<table\>
\<tr\>
\<td\>\<b\>\<a href='https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/websocket/socket\_events.py'\>socket\_events.py\</a\>\</b\>\</td\>
\<td\>\<code\>❯ Defines the WebSocket event handlers for real-time communication.\</code\>\</td\>
\</tr\>
\</table\>
\</blockquote\>
\</details\>
\<details\> \<summary\>\<b\>routes\</b\>\</summary\>
\<blockquote\>
\<table\>
\<tr\>
\<td\>\<b\>\<a href='https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/routes/pagamentos.py'\>pagamentos.py\</a\>\</b\>\</td\>
\<td\>\<code\>❯ Handles API routes related to payment processing and management.\</code\>\</td\>
\</tr\>
\<tr\>
\<td\>\<b\>\<a href='https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/routes/pedidos.py'\>pedidos.py\</a\>\</b\>\</td\>
\<td\>\<code\>❯ Manages API routes for order creation and retrieval.\</code\>\</td\>
\</tr\>
\</table\>
\</blockquote\>
\</details\>
\<details\> \<summary\>\<b\>utils\</b\>\</summary\>
\<blockquote\>
\<table\>
\<tr\>
\<td\>\<b\>\<a href='https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/utils/validators.py'\>validators.py\</a\>\</b\>\</td\>
\<td\>\<code\>❯ Contains utility functions for data validation across the API.\</code\>\</td\>
\</tr\>
\</table\>
\</blockquote\>
\</details\>
\<details\> \<summary\>\<b\>services\</b\>\</summary\>
\<blockquote\>
\<table\>
\<tr\>
\<td\>\<b\>\<a href='https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/services/fila\_service.py'\>fila\_service.py\</a\>\</b\>\</td\>
\<td\>\<code\>❯ Provides functions for managing the payment processing queue.\</code\>\</td\>
\</tr\>
\<tr\>
\<td\>\<b\>\<a href='https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/services/mercado\_pago.py'\>mercado\_pago.py\</a\>\</b\>\</td\>
\<td\>\<code\>❯ Encapsulates the logic for interacting with the Mercado Pago API.\</code\>\</td\>
\</tr\>
\<tr\>
\<td\>\<b\>\<a href='https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/services/historico\_service.py'\>historico\_service.py\</a\>\</b\>\</td\>
\<td\>\<code\>❯ Manages the storage and retrieval of payment history.\</code\>\</td\>
\</tr\>
\<tr\>
\<td\>\<b\>\<a href='https://github.com/kaiojv2/mercado\_pago\_api.git/blob/master/services/pdf\_service.py'\>pdf\_service.py\</a\>\</b\>\</td\>
\<td\>\<code\>❯ Handles the generation of PDF documents, such as receipts.\</code\>\</td\>
\</tr\>
\</table\>
\</blockquote\>
\</details\>
\</details\>

-----

## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with mercado\_pago\_api.git, ensure your runtime environment meets the following requirements:

  - **Programming Language:** Python 3.8+
  - **Package Manager:** Pip

### ⚙️ Installation

Install mercado\_pago\_api.git using one of the following methods:

**Build from source:**

1.  Clone the `mercado_pago_api.git` repository:

    ```sh
    ❯ git clone [https://github.com/kaiojv2/mercado_pago_api.git](https://github.com/kaiojv2/mercado_pago_api.git)
    ```

2.  Navigate to the project directory:

    ```sh
    ❯ cd mercado_pago_api.git
    ```

3.  Install the project dependencies:

    **Using `pip`**   [\<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge\_style}\&logo=pypi\&logoColor=white" /\>](https://pypi.org/project/pip/)

    ```sh
    ❯ pip install -r requirements.txt
    ```

### 🤖 Usage

To run the Mercado Pago API project, you'll primarily use the `run_eventlet.py` script, which leverages `eventlet` for asynchronous operations. You'll also need to configure your Mercado Pago credentials.

#### 1\. Configure Mercado Pago Credentials

Before running the application, you need to set your Mercado Pago **Public Key** and **Access Token** as environment variables.

  * **`MERCADO_PAGO_PUBLIC_KEY`**: Your Mercado Pago Public Key.
  * **`MERCADO_PAGO_ACCESS_TOKEN`**: Your Mercado Pago Access Token.

**On Linux/macOS:**

```bash
export MERCADO_PAGO_PUBLIC_KEY="YOUR_PUBLIC_KEY"
export MERCADO_PAGO_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
```

**On Windows (Command Prompt):**

```cmd
set MERCADO_PAGO_PUBLIC_KEY="YOUR_PUBLIC_KEY"
set MERCADO_PAGO_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
```

**On Windows (PowerShell):**

```powershell
$env:MERCADO_PAGO_PUBLIC_KEY="YOUR_PUBLIC_KEY"
$env:MERCADO_PAGO_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
```

Replace `"YOUR_PUBLIC_KEY"` and `"YOUR_ACCESS_TOKEN"` with your actual Mercado Pago credentials.

#### 2\. Run the Application

Once your environment variables are set, you can run the application:

**Using `python` with `run_eventlet.py`**   [\<img align="center" src="https://img.shields.io/badge/Python-3776AB.svg?style={badge\_style}\&logo=python\&logoColor=white" /\>](https://www.python.org/)

```sh
❯ python run_eventlet.py
```

This command will start the Flask application with `eventlet` as the WSGI server, typically on `http://127.0.0.1:5000`.

#### 3\. Exposing Your Local Server (Optional, for Webhooks)

If you need to receive webhooks from Mercado Pago (e.g., for payment notifications), your local server needs to be accessible from the internet. You can use **ngrok** for this purpose.

1.  **Download ngrok:** If you don't have it, download ngrok from [ngrok.com](https://ngrok.com/download).
2.  **Unzip ngrok:** Extract the `ngrok.exe` (or `ngrok` for Linux/macOS) to a convenient location, or directly into the `ngrok` folder within this project.
3.  **Run ngrok:** In a new terminal, navigate to your `mercado_pago_api.git` directory and then into the `ngrok` directory, and run:
    ```sh
    ❯ cd ngrok
    ❯ ./ngrok http 5000
    ```
    This will provide you with a public URL (e.g., `https://xxxxxx.ngrok-free.app`). You can then configure this URL in your Mercado Pago application settings for webhooks.

### 🧪 Testing

Run the test suite using the following command:
**Using `pytest`**   [\<img align="center" src="https://img.shields.io/badge/Pytest-0A595B.svg?style={badge\_style}\&logo=pytest\&logoColor=white" /\>](https://docs.pytest.org/en/stable/)

```sh
❯ pytest
```

-----

## 📌 Project Roadmap

  - [X] **`Task 1`**: \<strike\>Implement feature one.\</strike\>
  - [ ] **`Task 2`**: Implement feature two.
  - [ ] **`Task 3`**: Implement feature three.

-----

## 🔰 Contributing

  - **💬 [Join the Discussions](https://github.com/kaiojv2/mercado_pago_api.git/discussions)**: Share your insights, provide feedback, or ask questions.
  - **🐛 [Report Issues](https://github.com/kaiojv2/mercado_pago_api.git/issues)**: Submit bugs found or log feature requests for the `mercado_pago_api.git` project.
  - **💡 [Submit Pull Requests](https://github.com/kaiojv2/mercado_pago_api.git/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

\<details closed\>
\<summary\>Contributing Guidelines\</summary\>

1.  **Fork the Repository**: Start by forking the project repository to your GitHub account.
2.  **Clone Locally**: Clone the forked repository to your local machine using a git client.
    ```sh
    git clone [https://github.com/kaiojv2/mercado_pago_api.git](https://github.com/kaiojv2/mercado_pago_api.git)
    ```
3.  **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
    ```sh
    git checkout -b new-feature-x
    ```
4.  **Make Your Changes**: Develop and test your changes locally.
5.  **Commit Your Changes**: Commit with a clear message describing your updates.
    ```sh
    git commit -m 'Implemented new feature x.'
    ```
6.  **Push to GitHub**: Push the changes to your forked repository.
    ```sh
    git push origin new-feature-x
    ```
7.  **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8.  **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution\!

\</details\>

\<details closed\>
\<summary\>Contributor Graph\</summary\>
\<br\>
\<p align="left"\>
\<a href="https://github.com{/kaiojv2/mercado\_pago\_api.git/}graphs/contributors"\>
\<img src="https://contrib.rocks/image?repo=kaiojv2/mercado\_pago\_api.git"\>
\</a\>
\</p\>
\</details\>

-----

## 🎗 License

This project is protected under the [MIT License](https://choosealicense.com/licenses/mit). For more details, refer to the [LICENSE](https://choosealicense.com/licenses/mit/) file.

-----

## 🙌 Acknowledgments

  - **Mercado Pago Developers Site**: For comprehensive API documentation and guides.
  - **Flask Community**: For the robust web framework.
  - **Eventlet**: For enabling efficient asynchronous operations.
  - **PyInstaller**: For simplifying application distribution.

-----

```
```
