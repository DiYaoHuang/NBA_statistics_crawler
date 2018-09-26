
# coding: utf-8

import requests
import json
from datetime import datetime,timedelta
import pandas as pd
import re

dates = pd.date_range(start='20180101',end='20180630')
gameID = []
count = 0
try:
    for date in range(0,len(dates)):
        url = 'https://tw.global.nba.com/stats2/scores/gamedaystatus.json?gameDate={}-{}-{}&locale=zh_TW&tz=%2B8'.format('%04d'%dates[date].year,'%02d'%dates[date].month,'%02d'%dates[date].day)
        res = requests.get(url)
        length = len(res.json()['payload']['gameDates'][0]['games'])
        for day_of_game in range(0,length):
            game = res.json()['payload']['gameDates'][0]['games'][day_of_game]['gameId']
            url_game_stat = 'https://tw.global.nba.com/stats2/game/snapshot.json?countryCode=TW&gameId={}&locale=zh_TW'.format(game)
            year = re.search('\d{3}(\d{2})\d{5}',url_game_stat).group(1)
            res_game_stat = requests.get(url_game_stat)
            game_stat = res_game_stat.json()['payload']
            with open('../Documents/game_stat/%s-%s.json'%(year,game),'w') as f:
                json.dump(game_stat,f)
            count += 1
except Exception as e:
    print('%s has error '%(game))
    print(e)
print(count)

