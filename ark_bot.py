import json
import requests as rq
from bs4 import BeautifulSoup as bs
import telebot
import tg_bot_conf

TOKEN = tg_bot_conf.bot_auth
CHATID = tg_bot_conf.chat_id

def parser():
    '''Function to return parsed HTML table data
    using requests, BeautifulSoup'''
    exams = rq.get('https://eteenindus.mnt.ee/public/vabadSoidueksamiajad.xhtml')
    content = exams.content
    html = content
    soup = bs(html, features="lxml")
    table = soup.find(id='eksami_ajad:kategooriaBEksamiAjad_data')
    tds = list(map(lambda td: td.get_text(), table.find_all('td')))
    ext_data = dict()
    for i in range(0, len(tds), 5):
        ext_data[tds[i]] = tds[i+2:i+5]
    with open('data.json', 'w') as outfile:
        json.dump(ext_data, outfile)
    return ext_data

if __name__ == '__main__':parser()



available_times = ''

with open('data.json') as json_file:
    data = json.load(json_file)
    for index, value in data.items():
        available_times += f"*{index}*: {value} \n".replace("'", "")


tb = telebot.TeleBot(TOKEN)
# tb.send_message(chatid, message)
tb.send_message(CHATID, available_times, parse_mode = 'Markdown')
