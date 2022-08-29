# -*- coding=utf-8 -*-
# @从此音尘各悄然，春山如黛草如烟
# @Project_Name:project
# @User:34409/月念尘
# @Date :2022/8/29 12:39
# @File : __init__.py.py
import os


def get_conf():
    conf_list = []
    path = os.path.dirname(os.path.abspath(__file__))
    with open(path + '\\project.conf', 'r') as f:
        for i in range(4):
            x = f.readline()
            conf_list.append(x.split('=')[1].strip('\n').strip("''"))
        # print(conf_list)
    lst = ['app_id', 'app_secret', 'user_id', 'template_id']
    for k, v in zip(lst, conf_list):
        if k == 'app_id':
            app_id = v
        elif k == 'app_secret':
            app_secret = v
        elif k == 'user_id':
            user_ids = []
            user_id = v.strip("""[]""").split(',')
            for i in user_id:
                user_ids.append(i.strip().strip("''"))
            # print(type(user_ids))
        else:
            template_id = v

    return {
        'app_id': app_id,
        'app_secret': app_secret,
        'user_id': user_ids,
        'template_id': template_id
    }

# get_conf()