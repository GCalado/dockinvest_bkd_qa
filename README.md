<p align="center">
  <img src="https://files.readme.io/f29a06b-small-210823.Dock.Logo.REFINADO.RGB_Azul.png" alt="Dock Logo" width="200"/>
</p>

# 🚀 Dock Invest - Testes Funcionais Automatizados

Este repositório contém o projeto de **testes funcionais automatizados** para o produto **Dock Invest**.

## 📝 Sobre o Projeto

Dock Invest é a funcionalidade de **Remuneração de Saldo** que permite que clientes Dock (emissores) ofereçam rendimento sobre os saldos mantidos nas contas digitais de seus usuários finais. Os fundos depositados nessas contas podem ser aplicados pela Dock em títulos públicos federais, gerando receita que pode ser compartilhada conforme o modelo de negócio acordado.

Este projeto visa garantir a qualidade e a confiabilidade do Dock Invest, automatizando cenários de testes funcionais críticos para o negócio.

---

## 🛠️ Tecnologias Utilizadas

- <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python" width="22"/> **[Python](https://docs.python.org/3/)**  
  Linguagem principal do projeto.

- <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pytest/pytest-original.svg" alt="Pytest" width="22"/> **[Pytest](https://docs.pytest.org/en/stable/)**  
  Framework para execução dos testes automatizados.

- <img src="_static/requests-sidebar.png" alt="Requests" width="22" style="background:white; border-radius:3px;"/> **[Requests](https://docs.python-requests.org/en/latest/)**  
  Biblioteca para requisições HTTP, utilizada para testar APIs.

- <img src="https://pypi-camo.freetls.fastly.net/c29f3ca2f56e39a8adf88da117ea03579f2eb439/68747470733a2f2f692e696d6775722e636f6d2f3454596961356a2e706e67" alt="pytest-html" width="22"/> **[pytest-html](https://pytest-html.readthedocs.io/en/latest/)**  
  Plugin para geração de relatórios de testes em HTML.

---

## 💻 Como baixar e executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/dockinvest_bkd_qa.git
cd dockinvest_bkd_qa
```

### 2. Crie um ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure variáveis de ambiente (se necessário)

Crie um arquivo `.env` com as configurações necessárias para execução dos testes.

### 5. Execute os testes

```bash
pytest
```

Para gerar um relatório em HTML:

```bash
pytest --html=report.html
```

---

## 📂 Estrutura do Projeto

```
dockinvest_bkd_qa/
│
├── src/                # Código-fonte dos testes
├── tests/              # Casos de teste automatizados
├── requirements.txt    # Dependências do projeto
├── README.md           # Este arquivo
└── ...
```

---

## 📄 Referências

- [Dock Invest](https://developers.dock.tech/docs/remunera%C3%A7%C3%A3o-de-saldo-dock)
- [Python](https://docs.python.org/3/)
- [Pytest](https://docs.pytest.org/en/stable/)
- [Requests](https://docs.python-requests.org/en/latest/)
- [pytest-html](https://pytest-html.readthedocs.io/en/latest/)
- [Docker](https://docs.docker.com/)

---

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.
