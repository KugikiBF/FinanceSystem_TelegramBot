from index import ControleFinanceiro
import telebot


bot=telebot.TeleBot("8594534195:AAESzmzrHWaG7Yb-s54wqsclK3iGPYExuGk")
sistema=ControleFinanceiro()


@bot.message_handler(commands=['start', 'help'])
def enviar_boas_vindas(message):
    manual = (
        "💰 *Gestor Financeiro Ativo!*\n\n"
        "✨ *Como registrar:* `Valor Descrição Categoria`\n"
        "💡 _Dica: 3 palavras = Pago | 4 palavras ou mais = Pendente_\n\n"
        "📊 *Relatórios Visual:* \n"
        "/setor - Gastos por categoria (Pizza)\n"
        "/gerais - Status de Pagamento (Barras)\n"
        "/balanco - Lucro vs Prejuízo\n\n"
        "🛠 *Utilidades:*\n"
        "/buscar `termo` - Filtra por descrição\n"
        "/excluir - Remove o último lançamento\n"
        "/help - Mostra esta mensagem"
    )
    bot.reply_to(message, manual, parse_mode='Markdown')
    

@bot.message_handler(commands=['setor'])
def resumo_setor(message):
    bot.send_message(message.chat.id, "📊 Gerando seus relatórios, aguarde...")
    sistema.grafico_setor_telegram()
    with open ('static/pizza.png','rb') as foto:
        bot.send_photo(message.chat.id, foto, caption='💲Gastos por Categoria')
    bot.send_message(message.chat.id, sistema.historico_contas(), parse_mode='Markdown')


@bot.message_handler(commands=['gerais'])
def resumo_gerais(message):
    bot.send_message(message.chat.id, "📊 Gerando seus relatórios, aguarde...")
    sistema.grafico_gerais_telegram()
    with open ('static/gerais.png','rb') as foto:
        bot.send_photo(message.chat.id, foto, caption='💲Gastos Pendentes/Pagos')
    bot.send_message(message.chat.id, sistema.historico_contas(), parse_mode='Markdown')




@bot.message_handler(commands=['balanço','balanco'])
def balanco_mensal(message):
    bot.send_message(message.chat.id, "📊 Gerando seus relatórios, aguarde...")
    sistema.grafico_lucro_telegram()
    with open ('static/lucro.png','rb') as foto:
        bot.send_photo(message.chat.id, foto, caption='💲Balanço Mensal')
    bot.send_message(message.chat.id, sistema.historico_contas(), parse_mode='Markdown')



@bot.message_handler(commands=['buscar'])
def buscar(message):
    divisor = message.text.split()
    if len(divisor) > 1:
        termo = " ".join(divisor[1:])
        res = sistema.buscar(termo)
        bot.reply_to(message, res, parse_mode='Markdown')
    else:
        bot.reply_to(message, "🔍 Digite o que quer buscar.\nEx: `/buscar pizza`", parse_mode='Markdown')

@bot.message_handler(commands=['excluir'])
def excluir(message):
    sistema.excluir_lançamento()
    bot.reply_to(message,"✅Ultimo lançamento excluído com sucesso!")


@bot.message_handler(func=lambda m:True)
def adicionar_gasto(message):
    divisor = message.text.split()
    
    if len(divisor) >= 3:
        try:
            valor_limpo = divisor[0].replace(',', '.')
            valor = float(valor_limpo)
            desc = divisor[1]
            cat = divisor[2].capitalize()
            status="Pago" if len(divisor) == 3 else "Pendente"
            res = sistema.adicionar_lancamento_telegram(valor, desc, cat,status)
            bot.reply_to(message, res)
            
        except ValueError:
            bot.reply_to(message, "❌ Erro: O valor deve ser um número. Ex: 50.00")
        except Exception as e:
            bot.reply_to(message, f"⚠️ Erro inesperado: {e}")
    else:
        bot.reply_to(message, "🤖 Não entendi. Use o formato: `Valor Descrição Categoria` (Ex: 50 Pizza Lazer)")


    


bot.infinity_polling()