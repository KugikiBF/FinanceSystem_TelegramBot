# 💰 FinanceBot — Intelligence & Data Analytics

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)

Interface ágil para registros rápidos | Relatórios visuais instantâneos | Persistência em Excel

---

## 📌 Sobre o Projeto

O **FinanceBot** é uma solução de Engenharia de Software focada em resolver a complexidade de apps financeiros tradicionais. Utilizando a API do Telegram, o sistema transforma mensagens de texto informais em dados estruturados para análise de BI.

---

## ⚙️ Arquitetura Técnica

### 🧪 Core Engine
* **Data Parsing:** Algoritmo em Python para extração de `Valor`, `Descrição` e `Categoria` via inputs de texto.
* **Pandas Integration:** O motor do projeto. Realiza o tratamento, filtragem e soma de dados para geração de DataFrames.
* **Automated Viz:** Implementação de `Matplotlib` com backend `Agg` para renderização de gráficos em tempo real no servidor.

---

## 📊 Business Intelligence (BI)

| Comando | Análise Realizada | Visualização |
| :--- | :--- | :--- |
| `/setor` | **Pareto de Gastos** | Gráfico de Pizza dinâmico |
| `/gerais` | **Cash Flow Status** | Comparativo Pago vs. Pendente |
| `/balanco` | **Net Profit** | Indicador de Lucro ou Prejuízo |

---

## 🚀 Setup do Ambiente

```bash
pip install pandas matplotlib pyTelegramBotAPI openpyxl
mkdir static
python bot_telegram.py
