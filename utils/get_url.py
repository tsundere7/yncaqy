# -*- coding=utf-8 -*-
# @从此音尘各悄然，春山如黛草如烟
# @Project_Name:project
# @User:34409/月念尘
# @Date :2022/8/29 12:38
# @File : get_url.py
import requests
import settings


def make_url():
    url = f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={settings.get_conf()["app_id"]}&secret={settings.get_conf()["app_secret"]}'

    response = requests.get(url)
    access_token = response.json()['access_token']
    print(response.json()['access_token'])
    uri = f'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={access_token}'
    return uri
