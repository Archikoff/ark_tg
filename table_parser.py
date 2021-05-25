import requests as rq
from table import Table
from bs4 import BeautifulSoup as bs

def from_url(table_url):
    ''' функция считывает таблицу с сайта eteenindus.mnt.ee и парсит
    Function to return parsed HTML table data
    using requests, BeautifulSoup
    Возвращает словарь, соответствующий таблице.
    '''
    exams = rq.get(table_url)
    content = exams.content
    soup = bs(content, features="lxml")
    table = soup.find(id='eksami_ajad:kategooriaBEksamiAjad_data')
    tds = list(map(lambda td: td.get_text(), table.find_all('td')))
    ext_data = dict()
    for i in range(0, len(tds), 5):
        ext_data[tds[i]] = tds[i+2:i+5]
    return Table(ext_data)
