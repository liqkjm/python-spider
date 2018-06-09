#2018-2-4
import urllib.request
import parser
import time
import json
#url   定义真实网址  统一资源定位符
# 单引号 双引号 三引号 的区别
# 对于字符串，单引号和双引号 没有区别
# 三引号可以保留文本格式
while True:
    time.sleep(5)
    url = "https://api.live.bilibili.com/ajax/msg"
    #要调教的数据
    form = {'roomid':'5279',
    'token':'',
    'csrf_token':'52fd6503ccd3ff0a39591bcedd7a1203'
    }
    #python2    可以直接使用request的post方法
    #python3    urllib.request.Request（）用于向服务端发送请求，就如 http 协议客户端想服务端发送请求
    #           而 urllib.request.urlopen（）则相当于服务器返回的响应
    # str转bytes叫encode，bytes转str叫decode
    data = urllib.parse.urlencode(form)
    data = data.encode('utf-8')
    req = urllib.request.Request(url , data)
    res = urllib.request.urlopen(req)

    html = res.read().decode('UTF-8')

    html = json.loads(html)
    try:
        context = list(map(lambda ii:html['data']['room'][ii]['text'],range(10)))
        f = open('F:\李清健的文件\python\爬虫\B站弹幕\output.txt', 'a')
        f.write(str(context)+'\n')
    except Exception as e:
        print("写入失败")
    else:
        print("写入成功")
        f.close()







