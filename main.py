import re
import sqlite3 as sq
import db_session
from orm_model import Logs
 

db_session.global_init("db.db")


def readConfig(filename):
    with open(filename, 'r', encoding='UTF-8') as f:
        lines = f.readlines()

    lines = [line.rstrip() for line in lines]
        
    _dir = re.findall(r'"(.*)"', lines[0])[0].replace('\\', '/')
    return _dir

def readLogsAndAddToBD(direct):
    with open(direct, 'r', encoding='UTF-8') as f:
        lines = f.readlines()

    lines = [line.rstrip() for line in lines]
        
    logs = []
    pattern = r'(^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) (.*) (.*) \[(\d{2}\/\w*\/\d{4}:\d{2}:\d{2}:\d{2} [+,-]\d{4})\] "(.*)" (\d*) (\d*)'
    db_sess = db_session.create_session()
    for line in lines:
        log = Logs()
        log.h, log.l, log.u, log.t, log.r, log.s, log.b = re.split(pattern, line)[1:-1]
        db_sess.add(log)
    db_sess.commit()
    return 


def main():
    print('h - ip, l - Длинное имя удаленного хоста, u - Удаленный пользователь, t - Время получения запроса, r - Первая строка запроса, s - Финальный статус, b - Размер  ответа в байтах')
    query = list(input('Введите нужные эелементы слитно: '))
    db_sess = db_session.create_session()
    logs = db_sess.query(Logs).all()
    match input('Хотите ли выбрать диапазон времени? (+ или -): '):
        case '-':
            for i in logs:
                print(*eval(", '|', ".join(["i." + query[j] for j in range(len(query))])))
        case '+':
            startTime = input('Введите начальное время (Формат HH:MM:SS): ')
            endTime = input('Введите конечное время (Формат HH:MM:SS): ')            
            for i in logs:
                if int(startTime.replace(":", "")) < int("".join(i.t.split()[0].split(":")[1:4])) < int(endTime.replace(":", "")):
                    print(*eval(", '|', ".join(["i." + query[j] for j in range(len(query))])))

                

if __name__ == "__main__":
    # logsArr = readLogsAndAddToBD(readConfig('Config.txt'))
    main()
