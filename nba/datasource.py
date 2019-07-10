#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

# 球员职业生涯时间
years = [2018, 2019]
for i in range(years[0], years[1]):
    # 赛季
    season = str(i) + '-' + str(i + 1)[-2:]
    # 球员ID
    player_id = '201939'
    # 请求网址
    url = 'https://stats.nba.com/stats/shotchartdetail?AheadBehind=&CFID=33&CFPARAMS=' + season + '&ClutchTime=&Conference=&ContextFilter=&ContextMeasure=FGA&DateFrom=&DateTo=&Division=&EndPeriod=10&EndRange=28800&GROUP_ID=&GameEventID=&GameID=&GameSegment=&GroupID=&GroupMode=&GroupQuantity=5&LastNGames=0&LeagueID=00&Location=&Month=0&OnOff=&OpponentTeamID=0&Outcome=&PORound=0&Period=0&PlayerID=' + player_id + '&PlayerID1=&PlayerID2=&PlayerID3=&PlayerID4=&PlayerID5=&PlayerPosition=&PointDiff=&Position=&RangeType=0&RookieYear=&Season=' + season + '&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StartPeriod=1&StartRange=0&StarterBench=&TeamID=0&VsConference=&VsDivision=&VsPlayerID1=&VsPlayerID2=&VsPlayerID3=&VsPlayerID4=&VsPlayerID5=&VsTeamID='
    # 请求结果
    response = requests.get(url=url, headers=headers)
    result = json.loads(response.text)

    # 获取数据
    for item in result['resultSets'][0]['rowSet']:
        # 是否进球得分
        flag = item[10]
        # 横坐标
        loc_x = str(item[17])
        # 纵坐标
        loc_y = str(item[18])
        with open('curry.csv', 'a+') as f:
            f.write(loc_x + ',' + loc_y + ',' + flag + '\n')

