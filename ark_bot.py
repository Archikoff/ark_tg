import json
import requests as rq
from bs4 import BeautifulSoup as bs


def parser():
    exams = rq.get('https://eteenindus.mnt.ee/public/vabadSoidueksamiajad.xhtml')
    content = exams.content
    html = content
    soup = bs(html, features="lxml")
    table = soup.find(id='eksami_ajad:kategooriaBEksamiAjad_data')

    tds = list(map(lambda td: td.get_text(), table.find_all('td')))
    ext_data = dict()
    for i in range(0, len(tds), 5):
        ext_data[tds[i]] = tds[i+2:i+5]
    return ext_data