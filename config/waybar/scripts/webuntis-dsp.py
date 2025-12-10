import os.path

import webuntis
import datetime
import json
import time

if os.path.exists('webuntis-conf.json'):
    configj = open('webuntis-conf.json', 'r')
else:
    configj = open('webuntis-conf-d.json', 'r')

config = json.load(configj)

s = webuntis.Session(
    server=config['server'],
    username=config['username'],
    password=config['password'],
    school=config['school'],
    useragent=config['useragent']
)

while config['enabled']:

    currentDate = datetime.date.today()
    currentTime = datetime.datetime.now().time()

    s.login()

    klasse = s.klassen().filter(name=config['klasse'])[0]

    table = s.timetable(klasse=klasse, start=currentDate, end=currentDate).to_table()

    if not table:
        print('no classes')
    else:
        for entries in table:
            if entries[0] >= currentTime > datetime.time(6, 0):
                time_str = entries[0].strftime("%H:%M")
                for date, periods in entries[1]:
                    for p in periods:
                        print(f"{time_str} -> {p.subjects}{p.rooms}")
                break

    s.logout()
    time.sleep(5)