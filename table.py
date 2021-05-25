import json

def data_save(outfile_name, dic):
    ''' Сохраняет словарь в файл'''
    with open(outfile_name, 'w') as outfile:
        json.dump(dic, outfile)

def data_load(inputfile_name):
    ''' Читает словарь из файла'''
    with open(inputfile_name) as json_file:
        data = json.load(json_file)
    return data

#это класс таблицы
class Table:
    def __init__(self, data):
        '''здесь таблица создается'''
        self.__data = data

    def __str__(self):
        '''переопределяем метод str для таблицы, чтобы можно было перевести ее в текст'''
        available_times = ''
        for index, value in self.__data.items():
            available_times += f"*{index}*: {value} \n".replace("'", "")

        return available_times

    def to_file(self, filename):
        data_save(filename, self.__data)

    @staticmethod
    def from_file(filename):
        '''статический метод, чтобы мы могли создать таблицу из файла Table.from_file('wejfwkefj.json')'''
        return Table(data_load(filename))

