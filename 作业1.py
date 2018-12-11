# coding:utf-8
import requests
import json
import matplotlib.pyplot as plt
import pyecharts

if __name__ == '__main__':
    goal_url = "http://192.168.0.149:8081/news/report/dailyinc?days=100"
    # goal_url = "http://192.168.0.110:3030/news/newschart.html"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'Origin': 'http://192.168.0.110:3030', 'Referer': 'http://192.168.0.110:3030/news/newschart.html'}

    my_get = {'login_url': 'http://192.168.0.110:3030/set/loginty.html',
              'ruleForm2.userName': '夏瑜潞',
              'ruleForm2.Password': 'xylabc123',
              'submitForm': '登录',
              }
    r = requests.get(goal_url, data=my_get, headers=headers)
    datas = json.loads(r.text)# 列表
    # print(datas)
    y = []
    x = []
    for each_one in datas:# each_one为字典
        x.append(each_one['date'])# x
        y.append(each_one['count'])# y

    # plt.plot(input_values, squares, linewidth=5)  # linewidth决定绘制线条的粗细
    # plt.title('Square Numbers', fontsize=24)  # 标题
    # plt.xlabel('Vaule', fontsize=14)
    # plt.ylabel('Square of Vaule', fontsize=14)
    #
    # plt.tick_params(axis='both', labelsize=14)  # 刻度加粗
    # plt.show()  # 输出图像

    line = pyecharts.Line("新闻下载量（单位：日）")
    line.add("Count", x, y,  is_datazoom_show=True)
    line.render(path="render1.html")
