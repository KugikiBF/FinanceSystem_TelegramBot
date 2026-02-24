💰 FinanceBot: Gestor Financeiro via Telegram
Sistema inteligente de controle financeiro pessoal que une a mobilidade do Telegram com a robustez do Pandas para análise de dados. Desenvolvido para facilitar o registro de gastos diários e oferecer insights visuais imediatos sobre saúde financeira.

🚀 Funcionalidades
Registro Ágil: Lançamentos diretos via chat (Ex: 50 Pizza Lazer).

Lógica Inteligente: O bot diferencia pagamentos "Pagos" de "Pendentes" pela quantidade de palavras no comando.

Relatórios Visuais Dinâmicos:

/setor: Gráfico de pizza com a distribuição percentual de gastos.

/gerais: Gráfico de barras comparando contas pagas vs. pendentes.

/balanco: Visão geral de Lucro vs. Prejuízo do mês.

Gestão de Dados: Armazenamento automático em Excel (.xlsx) com formatação de colunas automática.

Busca e Edição: Comando /buscar para filtrar histórico e /excluir para desfazer o último erro.

🛠️ Tecnologias Utilizadas
Linguagem: Python 3.x

Manipulação de Dados: Pandas

Visualização: Matplotlib (Backend Agg)

Interface de Bot: pyTelegramBotAPI

Persistência: Openpyxl (Excel Integration)

📂 Estrutura do Projeto
main.py: Lógica do bot e handlers do Telegram.

index.py: Classe ControleFinanceiro com as regras de negócio e geração de gráficos.

/static: Pasta onde são gerados os arquivos .png dos relatórios.

🔧 Como Instalar e Rodar
Clone o repositório:

git clone https://github.com/KugikiBF/
FinanceSystem_TelegramBot.git

Instale as bibliotecas necessárias:

pip install pandas matplotlib pyTelegramBotAPI openpyxl

Configure seu Token:
No arquivo main.py, insira o seu Token do BotFather:
bot = telebot.TeleBot("SEU_TOKEN_AQUI")

Inicie o serviço:
python bot_telegram.py

👨‍💻 Connect with me
<p align="left">
<a href="https://www.linkedin.com/in/bruno-felipe-7956bb351/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="Bruno Felipe" height="30" width="40" /></a>
<a href="https://github.com/KugikiBF" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/github.svg" alt="KugikiBF" height="30" width="40" /></a>
</p>
