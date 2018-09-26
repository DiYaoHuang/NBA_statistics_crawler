
# coding: utf-8

import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

# get all players list
playerlist = []
url_for_list = 'https://tw.global.nba.com/stats2/league/playerlist.json?locale=zh_TW'
res_for_list = requests.get(url_for_list)
length_for_list = len(res_for_list.json()['payload']['players'])
for count in range(0,length_for_list):
    name = res_for_list.json()['payload']['players'][count]['playerProfile']['code']
    playerlist.append(name)
len(playerlist)

# get all player info
for player in playerlist:
    try:
        url_player = 'https://tw.global.nba.com/stats2/player/stats.json?ds=career&locale=zh_TW&playerCode={}'.format(player)
        res_player = requests.get(url_player)
        player_info = res_player.json()['payload']['player']
        with open('../Documents/player_infor/%s.json'%player,'w') as f:
            json.dump(player_info,f)
    except Exception as e:
        print('%s has error '%(player))
        print(e)

