# -*- coding: utf-8 -*-
from flask import Flask, redirect, url_for, render_template, request, send_file, send_from_directory, make_response
import requests
import datetime
import json
import random
global false, null, true
false = null = true = ""
app = Flask(__name__)


catgif_list = ["https://cdn2.thecatapi.com/images/MTc3MDkxNw.gif", "https://cdn2.thecatapi.com/images/dbe.gif", "https://cdn2.thecatapi.com/images/da7.gif", 'https://cdn2.thecatapi.com/images/afu.gif', 'https://cdn2.thecatapi.com/images/av7.gif', 'https://cdn2.thecatapi.com/images/8u.gif', 'https://cdn2.thecatapi.com/images/4bj.gif', 'https://cdn2.thecatapi.com/images/4gg.gif', 'https://cdn2.thecatapi.com/images/41e.gif', 'https://cdn2.thecatapi.com/images/4c3.gif', 'https://cdn2.thecatapi.com/images/494.gif',
               'https://cdn2.thecatapi.com/images/db2.gif', 'https://cdn2.thecatapi.com/images/8c.gif', 'https://cdn2.thecatapi.com/images/3v7.gif', 'https://cdn2.thecatapi.com/images/cmr.gif', 'https://cdn2.thecatapi.com/images/4j2.gif', 'https://cdn2.thecatapi.com/images/MTY2MTU0OQ.gif', 'https://cdn2.thecatapi.com/images/7sh.gif', 'https://cdn2.thecatapi.com/images/MTUwNTk4NQ.gif', 'https://cdn2.thecatapi.com/images/4e5.gif', 'https://cdn2.thecatapi.com/images/atb.gif', 'https://cdn2.thecatapi.com/images/3k7.gif', 'https://cdn2.thecatapi.com/images/ace.gif']


@app.route('/', methods=['GET'])
def get_us():
    return render_template('index.html')


@app.route('/usbirth', methods=['GET'])
def birthdata():
    # token = request.form.get("token")
    token = request.headers["token"]
    print(token)
    url = 'https://us.ncuos.com/api/user/list?page_num=1&page_size=1000'
    header = {
        "authorization": token}
    res = requests.get(url, headers=header)
    data = eval(res.text)

    birth_datas = []
    for user in data:
        need_datas = []
        need_datas.append(user["truename"] + str(user["birthday"]))
        need_datas.append(user['qq'])
        need_datas.append(user['desc'])
        need_datas.append(user['photo'])
        birth_datas.append(need_datas)
    yesterday = (datetime.datetime.now()-datetime.timedelta(days=1)
                 ).strftime('today%Y-%m-%d')
    birth_datas.append([yesterday])
    birth_datas.append(need_datas)
    sort_data = list(
        sorted(birth_datas, key=lambda x: int(x[0][-5:].replace('-', ''))))
    # 把扩展一份没有当前日期的data（循环）
    copy_data = sort_data.copy()
    copy_data.remove([yesterday])
    sort_data.extend(copy_data)
    where_yesterday = sort_data.index([yesterday])
    who_birth = sort_data[where_yesterday+1: where_yesterday + 21]
    near_birth = {"near_birth": []}
    for i in who_birth:
        onedata = {}
        onedata["truename"] = i[0][:-10]
        onedata["brithday"] = i[0][-5:]
        onedata["qq"] = i[1]
        onedata["desc"] = i[2]
        if "pig" in i[3]:
            onedata["photo"] = random.choice(catgif_list)
        else:
            onedata["photo"] = i[3]
        near_birth["near_birth"].append(onedata)
    ans = make_response(json.dumps(near_birth).replace("'", '"'))
    ans.headers['Access-Control-Allow-Origin'] = '*'
    ans.headers['Content-Type'] = 'application/json'
    return ans


@app.route('/startimg', methods=['GET'])
def get_start_img():
    return redirect('https://cdn.nlark.com/yuque/0/2019/png/164272/1557981465230-4d0cb247-ecd8-481c-8779-14805ce0bdd6.png')


@app.route('/activeimg', methods=['GET'])
def get_active_img():
    return redirect('https://cdn.nlark.com/yuque/0/2019/png/164272/1558019928710-a84eebb5-3cfa-4497-b110-54e5199902e6.png')


@app.route('/randomimg', methods=['GET'])
def get_random_user_img():
    return redirect('https://uploadbeta.com/api/pictures/random/?key=BingEverydayWallpaperPicture')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3243, debug=true)
