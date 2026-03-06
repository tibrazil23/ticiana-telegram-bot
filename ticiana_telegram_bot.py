#!/usr/bin/env python3
"""
Bot Telegram para Ticiana Brannco
Oferece informações sobre livros, cursos e programas
"""

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

# Configurar logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Token do bot
TOKEN = "7920578176:AAEZPHLdlSuzFlQfeJyCRgyiTKH7Y8XWFXo"

# URLs dos produtos
URLS = {
    "livro_ia": "https://www.ticianabrannco.com.br/produto/ia-o-autoconhecimento/",
    "ebook_ia": "https://files.manuscdn.com/user_upload_by_module/session_file/310519663033878543/vRjhdNUiyHOAXGUB.pdf",
    "site": "http://www.ticianabrannco.com.br/",
    "instagram": "https://www.instagram.com/ticianabrannco/",
    "livros": "https://www.ticianabrannco.com.br/livros",
    "pausar": "https://www.ticianabrannco.com.br/pausar"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Comando /start - Mensagem de boas-vindas"""
    
    welcome_text = """
🌟 *Bem-vindo ao TiciTalk!* 🌟

Sou o bot da *Ticiana Brannco*, psicóloga, mentora e autora.

Posso te ajudar com:
✨ Autoconhecimento e desenvolvimento pessoal
💚 Saúde mental e bem-estar
🤖 Inteligência Artificial e o futuro do trabalho
📚 Informações sobre meus livros, programas e palestras

Vamos juntos construir um futuro mais consciente e próspero!

*O que você gostaria de saber?*
    """
    
    keyboard = [
        [
            InlineKeyboardButton("📚 Meus Livros", callback_data="livros"),
            InlineKeyboardButton("🎓 Meus Cursos", callback_data="cursos")
        ],
        [
            InlineKeyboardButton("📖 Ebook IA", callback_data="ebook"),
            InlineKeyboardButton("💬 Fale Comigo", callback_data="contato")
        ],
        [
            InlineKeyboardButton("🌐 Meu Site", callback_data="site"),
            InlineKeyboardButton("📱 Instagram", callback_data="instagram")
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        welcome_text,
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Comando /help - Ajuda"""
    
    help_text = """
*Comandos Disponíveis:*

/start - Iniciar o bot
/help - Ver esta ajuda
/livros - Ver meus livros
/cursos - Ver meus cursos
/ebook - Baixar ebook de IA
/contato - Entrar em contato

*Ou simplesmente clique nos botões abaixo!*
    """
    
    await update.message.reply_text(help_text, parse_mode="Markdown")

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Tratar cliques nos botões"""
    
    query = update.callback_query
    await query.answer()
    
    if query.data == "livros":
        await query.edit_message_text(
            text="""
📚 *Meus Livros*

🎯 *Inteligência Artificial & O Autoconhecimento*
Desvendando o Futuro com Sabedoria

Descubra como a IA pode transformar sua vida mantendo sua humanidade e autenticidade.

👉 [Comprar Agora](https://www.ticianabrannco.com.br/produto/ia-o-autoconhecimento/)

---

📖 *Ebook: Seu Assistente Digital*
Truques de IA para Quem Não Tem Tempo

Receitas prontas para usar com as principais IAs do mercado.

👉 [Baixar Ebook - R$ 19,90](https://files.manuscdn.com/user_upload_by_module/session_file/310519663033878543/vRjhdNUiyHOAXGUB.pdf)

---

Quer saber mais sobre algo específico?
            """,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("← Voltar", callback_data="voltar")]
            ])
        )
    
    elif query.data == "cursos":
        await query.edit_message_text(
            text="""
🎓 *Meus Cursos e Programas*

✨ *Programa PAUSAR*
Desenvolvido em parceria com profissionais especializados

Um programa transformador para:
💚 Bem-estar integral
🧠 Desenvolvimento pessoal
🌟 Autoconhecimento profundo

👉 [Saiba Mais](https://www.ticianabrannco.com.br/pausar)

---

🎤 *Palestras e Workshops*
Temas:
• Inteligência Artificial e Humanidade
• Saúde Mental na Liderança
• Comunicação Não Violenta e Mindfulness
• Desenvolvimento Pessoal e Profissional

👉 [Agendar Palestra](https://www.ticianabrannco.com.br/)

---

Quer mais informações?
            """,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("← Voltar", callback_data="voltar")]
            ])
        )
    
    elif query.data == "ebook":
        await query.edit_message_text(
            text="""
📖 *Seu Assistente Digital - Ebook*

🎯 *Truques de IA para Quem Não Tem Tempo*

Descubra como usar Inteligência Artificial para:
⏱️ Economizar tempo
🎯 Obter resultados imediatos
🧠 Manter sua humanidade
💰 Acessar 10+ ferramentas de IA

*Conteúdo:*
📚 5 Capítulos completos
🔗 Links clicáveis para todas as IAs
📝 10 Receitas prontas para usar
📊 Tabela comparativa de ferramentas
✨ Fórmula CPF dos prompts

*Preço: R$ 19,90*

👉 [Baixar Agora](https://files.manuscdn.com/user_upload_by_module/session_file/310519663033878543/vRjhdNUiyHOAXGUB.pdf)

Ou compre em:
🛒 [Hotmart](https://www.hotmart.com)
🛒 [Amazon](https://www.amazon.com)
🛒 [Meu Site](https://www.ticianabrannco.com.br/livros)
            """,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("← Voltar", callback_data="voltar")]
            ])
        )
    
    elif query.data == "contato":
        await query.edit_message_text(
            text="""
💬 *Fale Comigo*

Gostaria de entrar em contato para:
📧 Dúvidas sobre produtos
🤝 Parcerias
🎤 Palestras e workshops
💼 Consultoria

*Canais de Contato:*

📱 [Instagram](https://www.instagram.com/ticianabrannco/)
🌐 [Meu Site](https://www.ticianabrannco.com.br/)
✉️ [Email](mailto:contato@ticianabrannco.com.br)

Estou aqui para ajudar! 💜
            """,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("← Voltar", callback_data="voltar")]
            ])
        )
    
    elif query.data == "site":
        await query.edit_message_text(
            text="""
🌐 *Meu Site*

Visite meu site para:
📚 Conhecer todos os meus trabalhos
📖 Ler artigos e reflexões
🎓 Informações sobre cursos
💬 Entrar em contato

👉 [www.ticianabrannco.com.br](https://www.ticianabrannco.com.br/)

Lá você encontra tudo sobre:
✨ Minha história
🧠 Minha formação
📚 Meus livros
🎓 Meus programas
            """,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("← Voltar", callback_data="voltar")]
            ])
        )
    
    elif query.data == "instagram":
        await query.edit_message_text(
            text="""
📱 *Siga-me no Instagram*

@ticianabrannco

Lá você encontra:
✨ Dicas diárias de bem-estar
🧠 Reflexões sobre desenvolvimento pessoal
🤖 Conteúdo sobre IA e humanidade
💬 Interação direta comigo
📸 Momentos da minha rotina

👉 [@ticianabrannco](https://www.instagram.com/ticianabrannco/)

Vamos nos conectar! 💜
            """,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("← Voltar", callback_data="voltar")]
            ])
        )
    
    elif query.data == "voltar":
        await start(update, context)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Tratar mensagens de texto"""
    
    message_text = update.message.text.lower()
    
    # Respostas automáticas para palavras-chave
    if "oi" in message_text or "olá" in message_text or "opa" in message_text:
        await update.message.reply_text(
            "Olá! 👋 Bem-vindo ao TiciTalk!\n\nUse /start para ver todas as opções disponíveis.",
            parse_mode="Markdown"
        )
    
    elif "livro" in message_text:
        await update.message.reply_text(
            "📚 Quer saber sobre meus livros?\n\nUse /start e clique em 'Meus Livros'",
            parse_mode="Markdown"
        )
    
    elif "curso" in message_text or "programa" in message_text:
        await update.message.reply_text(
            "🎓 Quer conhecer meus cursos?\n\nUse /start e clique em 'Meus Cursos'",
            parse_mode="Markdown"
        )
    
    elif "ebook" in message_text or "ebook ia" in message_text:
        await update.message.reply_text(
            "📖 Quer baixar o ebook 'Seu Assistente Digital'?\n\nUse /start e clique em 'Ebook IA'",
            parse_mode="Markdown"
        )
    
    elif "contato" in message_text or "falar" in message_text:
        await update.message.reply_text(
            "💬 Quer entrar em contato?\n\nUse /start e clique em 'Fale Comigo'",
            parse_mode="Markdown"
        )
    
    else:
        await update.message.reply_text(
            "Desculpe, não entendi muito bem. 🤔\n\nUse /start para ver as opções disponíveis ou /help para ajuda.",
            parse_mode="Markdown"
        )

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log de erros"""
    logger.error(msg="Exception while handling an update:", exc_info=context.error)

def main() -> None:
    """Iniciar o bot"""
    
    # Criar aplicação
    application = Application.builder().token(TOKEN).build()
    
    # Adicionar handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CallbackQueryHandler(button_callback))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Log de erros
    application.add_error_handler(error_handler)
    
    # Iniciar o bot
    print("🤖 Bot iniciado! Pressione Ctrl+C para parar.")
    application.run_polling()

if __name__ == '__main__':
    main()
