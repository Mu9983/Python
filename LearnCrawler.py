"""
python爬虫相关 # 更多笔记http://t.csdnimg.cn/CE1rz
"""
from urllib import request
def define():
    # 定义url
    url = 'http://www.baidu.com'

    # 模拟浏览器向服务器发送请求 response响应
    response = request.urlopen(url)

    # 获取响应中的页面的源码
    content1 = response.read().decode('utf-8')
    # read读出的是二进制编码，需要解码decode
    # 查找<head><meta charset=utf-8>

    print(content1)

def ways():
    response = request.urlopen('http://www.baidu.com')
    # 一个类型六个方法
    # <class 'http.client.HTTPResponse'> read readline readlines getcode geturl getheaders
    type(response)
    # <class 'http.client.HTTPResponse'>

    # 按行读取
    # 依旧需要解码
    content2 = response.readlines()

    # 返回状态码 如果是200，证明逻辑没有错
    response.getcode()

    # 返回url地址
    response.geturl()

    # 获取状态信息
    response.getheaders()
    print(content2)


def download():
    """
    下载
    """
    # 下载网页
    url_page = 'http://www.baidu.com'
    request.urlretrieve(url=url_page, filename='baidu.html')

    # 下载图片
    url_img = 'https://n.sinaimg.cn/sinakd10117/102/w1026h676/20230602/83af-acf3b8ea6db20363aaffa213d488c97a.png'
    request.urlretrieve(url=url_img, filename='Vertin.jpg')

    # 下载视频
    url_video = ''
    request.urlretrieve(url=url_video, filename='')

def Customize_the_request_object():
    """
    定制请求对象
    """
    # url的组成
    # https://www.baidu.com/s?wd=周杰伦
    #  协议       主机      路径 参数 锚点
    # 协议：http/https
    # https = http + ssl/tsl
    # 主机：www.baidu.com
    # 端口号：http：80  https：443  mysql：3306  oracle：1521  redis：6379  mongodb：27017
    url = 'https://www.baidu.com'
    # User Agent: UA反爬
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'}
    # 请求对象定制
    request1 = request.Request(url=url, headers=headers)
    response = request.urlopen(request1)
    content = response.read().decode('utf-8')
    print(content)

from urllib import parse
def Codecs():
    """
    编解码三种方式：quote，urlencode，post
    """
    url = 'https://www.baidu.com/s?wd=周杰伦'
    # 由于编码原因，’周杰伦‘不会被搜索到网页
    name = parse.quote('周杰伦')
    url = url[:-3] + name
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'}
    request1 = request.Request(url=url, headers=headers)
    response = request.urlopen(request1)
    content = response.read().decode('utf-8')
    print(content)


Codecs()

