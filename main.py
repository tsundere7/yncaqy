# -*- coding=utf-8 -*-
# 入口
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage
from utils.get_url import make_url
import settings
from template.make_data import make_data


app_id = settings.get_conf()["app_id"]
app_secret = settings.get_conf()["app_secret"]

user_ids = settings.get_conf()["user_id"]
template_id = settings.get_conf()["template_id"]


if __name__ == '__main__':

    client = WeChatClient(app_id, app_secret)
    wm = WeChatMessage(client)
    count = 0
    url = make_url()
    for user_id in user_ids:
        res = wm.send_template(user_id, template_id, make_data(), url=url)
        count += 1

    print("推送了" + str(count) + "条消息")
