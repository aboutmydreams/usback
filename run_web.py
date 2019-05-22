#-*- coding: utf-8 -*-
from flask import Flask,redirect,url_for,render_template,request,send_file,send_from_directory,make_response
import requests,datetime,json,random
global false, null, true
false = null = true = ""
app = Flask(__name__)

# data = {"xz": [{"realname": "谢岚", "phone": "15079796454"}, {"realname": "梁传煌", "phone": "15770880568"}, {"realname": "汪尚嵘", "phone": "18270790930"}, {"realname": "王德萍", "phone": "17370836172"}, {"realname": "林心怡", "phone": "13870855693"}, {"realname": "肖婧萱", "phone": "18970028205"}, {"realname": "刘文星", "phone": "15216230070"}, {"realname": "田承晗", "phone": ""}, {"realname": "石婷燕", "phone": "15570354032"}], "sj": [{"realname": "张梦琦", "phone": "13007532306"}, {"realname": "黎若璇", "phone": "13330072767"}, {"realname": "谢冠群", "phone": "18146700165"}, {"realname": "杨甜婧", "phone": "13513614476"}, {"realname": "聂辉凡", "phone": "13755600643"}, {"realname": "张凌智", "phone": "13870822686"}, {"realname": "孙翔宇", "phone": "15526679740"}, {"realname": "童欣", "phone": "19939920653"}, {"realname": "赵子琦", "phone": "17756280996"}, {"realname": "黄浿绮", "phone": "13688064740"}, {"realname": "胡昊江", "phone": "13330120968"}, {"realname": "陈秋燕", "phone": "15059637276"}, {"realname": "金雨希", "phone": "17779720419"}], "yf": [{"realname": "吴惠兰", "phone": "13179386885"}, {"realname": "李彪", "phone": "15797896797"}, {"realname": "彭瀚林", "phone": "13330087529"}, {"realname": "林永昌", "phone": "13694909399"}, {"realname": "金长浩", "phone": "18179742907"}, {"realname": "易晟", "phone": "13879170262"}, {"realname": "张义主", "phone": "18270440718"}, {"realname": "王榕", "phone": ""}, {"realname": "汪磊", "phone": "15079845466"}, {"realname": "万伟强", "phone": "13319418531"}, {"realname": "余采佩", "phone": "18279348112"}, {"realname": "王越", "phone": "15079157122"}, {"realname": "郑宇杰", "phone": "18357922710"}, {"realname": "胡悦", "phone": "17779112712"}, {"realname": "李聪", "phone": "14770807180"}, {"realname": "刘致君", "phone": "15170307370"}, {"realname": "付应有", "phone": "15180451089"}, {"realname": "刘逸文", "phone": "15979165190"}, {"realname": "郭昕宇", "phone": "18507035301"}, {"realname": "钟家亮", "phone": "18679171921"}, {"realname": "王旋", "phone": "14779593033"}, {"realname": "叶昕", "phone": "15880088419"}, {"realname": "倪梓淇", "phone": "13677996589"}, {"realname": "贾贺", "phone": "15164925932"}, {"realname": "张纪元", "phone": "13330120016"}, {"realname": "邬振彬", "phone": ""}, {"realname": "吴晋君", "phone": "15879278286"}, {"realname": "杨晨", "phone": "19970721837"}, {"realname": "柯思源", "phone": "18579205749"}, {"realname": "傅诚", "phone": "18365407851"}], "zx": [{"realname": "田国华", "phone": "15679138068"}, {"realname": "张雪敏", "phone": "18270848607"}, {"realname": "周子睿", "phone": "18679751536"}, {"realname": "郭心雨", "phone": "13361617820"}, {"realname": "魏丽娟", "phone": "15797898565"}, {"realname": "石生辉", "phone": "18015749947"}], "yy": [{"realname": "卢娇", "phone": "15797893089"}, {"realname": "王晓涵", "phone": "13207080265"}, {"realname": "张甜甜", "phone": "13767424880"}, {"realname": "何雨芯", "phone": "15182977456"}, {"realname": "王珺", "phone": "13061306255"}, {"realname": "刘颖", "phone": "13617921211"}, {"realname": "熊文颖", "phone": ""}, {"realname": "赵小溪", "phone": "15768612076"}, {"realname": "张译禅", "phone": "15116958611"}, {"realname": "盛驿洁", "phone": "18307034568"}, {"realname": "杨若岚", "phone": "15727636938"}, {"realname": "曾阳婷", "phone": "19979603081"}], "cp": [{"realname": "吴东泽", "phone": "15692004480"}, {"realname": "邓文浩", "phone": "15170567059"}, {"realname": "胡紫韩", "phone": "13755901830"}, {"realname": "朱元哲", "phone": "13576025619"}, {"realname": "张帆", "phone": "18146701211"}, {"realname": "祝雨馨", "phone": "15797894090"}, {"realname": "李欣芝", "phone": "13967617547"}, {"realname": "黄新婕", "phone": "15579181817"}, {"realname": "袁博宇", "phone": "17807061970"}]}

# @app.route('/usphone', methods=['POST'])
# def login2():
#     p1 = request.form['username']
#     p2 = request.form['password']
#     if p1=='ncuhomeusapp' and p2=='wobuzhidao':
#         return str(data).replace("'",'"')


catgif_list = ["https://cdn2.thecatapi.com/images/MTc3MDkxNw.gif","https://cdn2.thecatapi.com/images/dbe.gif","https://cdn2.thecatapi.com/images/da7.gif",'https://cdn2.thecatapi.com/images/afu.gif', 'https://cdn2.thecatapi.com/images/av7.gif', 'https://cdn2.thecatapi.com/images/8u.gif', 'https://cdn2.thecatapi.com/images/4bj.gif', 'https://cdn2.thecatapi.com/images/4gg.gif', 'https://cdn2.thecatapi.com/images/41e.gif', 'https://cdn2.thecatapi.com/images/4c3.gif', 'https://cdn2.thecatapi.com/images/494.gif', 'https://cdn2.thecatapi.com/images/db2.gif', 'https://cdn2.thecatapi.com/images/8c.gif', 'https://cdn2.thecatapi.com/images/3v7.gif', 'https://cdn2.thecatapi.com/images/cmr.gif', 'https://cdn2.thecatapi.com/images/4j2.gif', 'https://cdn2.thecatapi.com/images/MTY2MTU0OQ.gif', 'https://cdn2.thecatapi.com/images/7sh.gif', 'https://cdn2.thecatapi.com/images/MTUwNTk4NQ.gif', 'https://cdn2.thecatapi.com/images/4e5.gif', 'https://cdn2.thecatapi.com/images/atb.gif', 'https://cdn2.thecatapi.com/images/3k7.gif', 'https://cdn2.thecatapi.com/images/ace.gif']

@app.route('/usbirth', methods=['GET'])
def birthdata():
    # token = request.form.get("token")
    token = request.headers["token"]
    print(token)
    url = 'https://us.ncuhomer.cn/api/user/list?page_num=1&page_size=1000'
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
    yesterday = (datetime.datetime.now()-datetime.timedelta(days=1)).strftime('today%Y-%m-%d')
    birth_datas.append([yesterday])
    birth_datas.append(need_datas)
    sort_data = list(sorted(birth_datas, key=lambda x: int(x[0][-5:].replace('-', ''))))
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
    ans = make_response(json.dumps(near_birth).replace("'",'"'))
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
    app.run(host='0.0.0.0',port=3243,debug=true)