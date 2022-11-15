from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup

# Get it on https://my.telegram.org/apps
TELEGRAM_API_ID = ''
TELEGRAM_API_HASH = ''
TELEGRAM_API_TOKEN = ''

answers = {
    'Pergunta 1': 'Resposta 1',
    'Pergunta 2': 'Resposta 2',
    'Pergunta 3': 'Resposta 3',
    'Qual o preço do <PRODUTO>?': 'O produto custa R$0,00'
}

app = Client(
    'leodopython_bot',
    api_id=TELEGRAM_API_ID,
    api_hash=TELEGRAM_API_HASH,
    bot_token=TELEGRAM_API_TOKEN
)

@app.on_message(filters.command('start'))
async def start_command(client, message):
    await message.reply(
        'Qual sua dúvida?',
        reply_markup=ReplyKeyboardMarkup(
            [
                ['Pergunta 1'],
                ['Pergunta 2'],
                ['Pergunta 3'],
                ['Qual o preço do <PRODUTO>?']
            ],
            resize_keyboard=True
        )
    )

@app.on_message()
async def message(client, message):
    if message.text in answers.keys():
        r = answers[message.text]
        await message.reply(r)

app.run()