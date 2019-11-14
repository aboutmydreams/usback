# encoding:utf-8
import random
import json
import requests
import datetime

global false, null, true
false = null = true = ""


def userdata(token):
    url = 'http://usv2.ncuos.com/api/user/list?page_num=1&page_size=1000'
    header = {
        'authorization': token, }
    res = requests.get(url, headers=header)
    data = eval(res.text)
    return data


def phone():
    us_phone_data = userdata(token)
    # a = ["xz", "sj", "yf", "zx", "yy", "cp"]

    # alldata = {"xz": [], "sj": [], "yf": [], "zx": [], "yy": [], "cp": []}
    # for i in us_phone_data:
    #     dic = {}
    #     dic["realname"] = i["truename"]
    #     department = i["department"]
    #     dic["phone"] = i["phone"]
    #     if department == a[0]:
    #         alldata["xz"].append(dic)
    #     elif department == a[1]:
    #         alldata["sj"].append(dic)
    #     elif department == a[2]:
    #         alldata["yf"].append(dic)
    #     elif department == a[3]:
    #         alldata["zx"].append(dic)
    #     elif department == a[4]:
    #         alldata["yy"].append(dic)
    #     else:
    #         alldata["cp"].append(dic)

    # b = json.dumps(alldata)
    # c = json.loads(b)
    # print(b)
    # d = str(alldata).replace("'", '"')
    # print(d)
    # f = open("usphone.json",'w')
    # f.write(d)

    datas = []
    for i in us_phone_data:
        dic = {}
        dic["realname"] = i["truename"]
        dic["phone"] = i["phone"]
        datas.append(dic)

    easydata = str(datas).replace("'", '"')
    return easydata


def birthdata(token):
    url = 'http://usv2.ncuos.com/api/user/list?page_num=1&page_size=1000'
    header = {
        'authorization': token}
    res = requests.get(url, headers=header)
    data = eval(res.text)
    birth_datas = []
    for user in data:
        need_datas = []
        need_datas.append(user["truename"] + user["birthday"])
        need_datas.append(user['qq'])
        need_datas.append(user['desc'])
        need_datas.append(user['photo'])
        birth_datas.append(need_datas)
    yesterday = (datetime.datetime.now()-datetime.timedelta(days=1)).strftime('today%Y-%m-%d')
    birth_datas.append([yesterday])
    birth_datas.append(need_datas)
    sort_data = list(sorted(birth_datas, key=lambda x: int(x[0][-5:].replace('-', ''))))
    # 把扩展一份没有当前日期的data（循环）
    copy_data = sort_data.copy()
    copy_data.remove([yesterday])
    sort_data.extend(copy_data)
    where_yesterday = sort_data.index([yesterday])
    who_birth = sort_data[where_yesterday+1: where_yesterday + 15]
    # if sort_data[where_yesterday - 1][]
    # who_birth.insert(0, sort_data[where_yesterday - 1])
    near_birth = {"near_birth": []}
    for i in who_birth:
        onedata = {}
        onedata["truename"] = i[0][:-10]
        onedata["brithday"] = i[0][-5:]
        onedata["qq"] = i[1]
        onedata["desc"] = i[2]
        onedata["phone"] = i[3]
        near_birth["near_birth"].append(onedata)

    return near_birth


token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyZW1lbWJlcl9tZSI6dHJ1ZSwiZXhwIjoyMTYxNTYyODE4LCJ1c2VyX2lkIjoyMDh9.Wej_BsG1Wl9CkT3 - 4AjHcM1Sgj16Y_6M6QPk63L9fm8'
# birthdata(token)
# phone_data = phone()
print(birthdata(token))

print(phone())

