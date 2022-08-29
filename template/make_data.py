# -*- coding=utf-8 -*-
# @从此音尘各悄然，春山如黛草如烟
# @Project_Name:project
# @User:34409/月念尘
# @Date :2022/8/29 13:01
# @File : make_data.py
import os
from datetime import date, datetime, timedelta
import math
import requests
import random

k_lst = []
path = os.path.dirname(os.path.abspath(__file__))
with open(path + '\\data.conf', 'r') as f:
    for i in range(3):
        x = f.readline()
        y = x.split('=')[1].strip("\n").strip().strip("''")
        print(y)
        k_lst.append(y)

today = datetime.now() + timedelta(hours=8)
start_date = k_lst[0]
city = k_lst[2]
birthday = k_lst[1]


def get_weather():
    url = "https://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city
    res = requests.get(url).json()
    weather = res['data']['list'][0]
    return weather['weather'], math.floor(weather['temp']), math.floor(weather['high']), math.floor(weather['low'])


def get_count():
    delta = today - datetime.strptime(start_date, "%Y-%m-%d")
    return delta.days


def get_birthday():
    next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
    if next < datetime.now():
        next = next.replace(year=next.year + 1)
    return (next - today).days


def get_words():
    words = requests.get("https://api.shadiao.pro/chp")
    if words.status_code != 200:
        return get_words()
    return words.json()['data']['text']


def get_random_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)


def make_data():
    wea, temperature, highest, lowest = get_weather()
    data = {"city": {"value": city, "color": get_random_color()},
            "date": {"value": today.strftime('%Y年%m月%d日'), "color": get_random_color()},
            "weather": {"value": wea, "color": get_random_color()},
            "temperature": {"value": temperature, "color": get_random_color()},
            "love_days": {"value": get_count(), "color": get_random_color()},
            "birthday_left": {"value": get_birthday(), "color": get_random_color()},
            "words": {"value": get_words(), "color": get_random_color()},
            "highest": {"value": highest, "color": get_random_color()},
            "lowest": {"value": lowest, "color": get_random_color()}}
    return data
