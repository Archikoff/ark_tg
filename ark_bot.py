import telebot
import tg_bot_conf
import table_parser

TOKEN = tg_bot_conf.bot_auth
CHATID = tg_bot_conf.chat_id
DATA_FILE = 'data.json'
TABLE_URL = 'https://eteenindus.mnt.ee/public/vabadSoidueksamiajad.xhtml'



#энтри поинт функция
def main():
    # вот здесь надо вызов сделать
    table = table_parser.from_url(TABLE_URL)
    table.to_file(DATA_FILE)

    tele_bot = telebot.TeleBot(TOKEN)
    tele_bot.send_message(CHATID, table, parse_mode='Markdown')

# проверяем является ли исполняемым
if __name__ == "__main__":
    main()
