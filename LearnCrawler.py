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
def Codes_quote():
    """
    编解码三种方式：quote，urlencode，post
    """
    url = 'https://www.baidu.com/s?wd=周杰伦'
    # 由于编码原因，'周杰伦'不会被搜索到网页
    name = parse.quote('周杰伦')
    url = url[:-3] + name
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'}
    request1 = request.Request(url=url, headers=headers)
    response = request.urlopen(request1)
    content = response.read().decode('utf-8')

def Codes_urlencode():
    url = 'https://www.baidu.com/s?wd=周杰伦&sex=男'
    url_list = url.split('?')
    base_url = url_list[0] + '?'
    dict_url = {}
    for i in url_list[1].split('&'):
        temp_url = i.split('=')
        dict_url[temp_url[0]] = temp_url[1]
    new_url = base_url + parse.urlencode(dict_url)
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'}
    request1 = request.Request(url=new_url, headers=headers)
    response = request.urlopen(request1)
    content = response.read().decode('utf-8')
    print(content)

def Codes_post():
    url = 'https://fanyi.baidu.com/sug'
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'}
    data = {'kw':'spring'}
    data = parse.urlencode(data).encode('utf-8')
    request1 = request.Request(url=url, data=data, headers=headers)
    response = request.urlopen(request1)
    content = response.read().decode('utf-8')
    import json
    print(json.loads(content))

def Codes_post_cookie(): # failed
    url = 'https://fanyi.baidu.com/translate'
    headers = {'cookie':'BAIDUID=C6AF63E8477876EAA5EA2BB48B7FEC2A:FG=1; newlogin=1; PSTM=1751860939; BIDUPSID=0FA7701BA789A49D38DB86C62BE37419; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_WISE_SIDS=62327_62832_63582_63727_63815_63824_63888_63907_63935_63948; H_PS_PSSID=62327_62832_63143_63326_63582_63724_63727_63275_63824_63789_63881_63888_63907_63935_63943_63948_63958_63966; BA_HECTOR=2g21a521aka1ag8l802l0g84a5a1a51k6os7125; BAIDUID_BFESS=C6AF63E8477876EAA5EA2BB48B7FEC2A:FG=1; ZFY=NULBXQD0BGOgBU62ql:BREU3l3qM8S:Bskmk5Mxg3Ey0s:C; delPer=0; PSINO=1; ab_sr=1.0.1_ZGU0NTU4NGE0NTViOTU2YTU0YzA0MDZiNmRlMDIxZWJmNTc0MmIyYzFjNTVlOTA3N2E1MzkyMTkxMGRjZWJjOWFmZTdhODA5ZGQxYzA5ZTgxMzMxNjQ1Mjg1OWY1YjU0NzkyN2ZmZDc2ZmU3OTM0M2M4MGZjYzhhMmYwY2IzMmExMjMxZmJiNGM5NTBhYjNlZGIyMjMxMTU2MDU1OWRjOTUxZTM1NTZmZGNiOTkzMTg4NjJkZWMyNGQ1NGExOGY4ODY3ZDMwZGZkZjk5NWMyNWYxOGUzZTRlN2YwZDE5OWY=; RT="z=1&dm=baidu.com&si=fb308a01-b134-409b-95f6-ae6a94eaae85&ss=mctv0bc4&sl=2&tt=37t&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=eop"',
               'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'}
    data = {"query":"spring","from":"en","to":"zh","reference":"","corpusIds":[],"needPhonetic":True,"domain":"common","milliTimestamp":1751938624083}
    data = parse.urlencode(data).encode('utf-8')
    request1 = request.Request(url=url, data=data, headers=headers)
    response = request.urlopen(request1)
    content = response.read().decode('utf-8')
    print(content)

def Crawl_Douban():
    """
    ajax网页的get爬取
    """
    url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'}
    request1 = request.Request(url=url, headers=headers)
    response = request.urlopen(request1)
    content = response.read().decode('utf-8')
    with open('./douban.json', 'w', encoding='utf-8') as file:
        file.write(content)

def Crawl_Douban_10_pages_with_get():
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'}
    start_page = int(input("start_page="))
    end_page = int(input("end_page="))
    for page in range(start_page, end_page + 1):
        data = parse.urlencode({'start':(page - 1) * 20, 'limit':20})
        url = base_url + data
        request1 = request.Request(url=url, headers=headers)
        response = request.urlopen(request1)
        content = response.read().decode('utf-8')
        with open(f'./CrawlDouban/Douban_{str(page)}.json', 'w', encoding='utf-8') as file:
            file.write(content)


def Crawl_KFC_with_post():
    """
    ajax网页的post爬取
    """
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'}
    start_index = int(input('start_index='))
    end_index = int(input('end_index='))
    name = input('name=')
    for pageIndex in range(start_index, end_index + 1):
        data = {'op':'cname',
                'cname':name,
                'pid':'',
                'pageIndex':pageIndex,
                'pageSize':10}
        data = parse.urlencode(data).encode('utf-8')
        request1 = request.Request(url=url, data=data, headers=headers)
        response = request.urlopen(request1)
        content = response.read().decode('utf-8')
        with open(f'./CrawlText/KFC_position_{str(pageIndex)}.json', 'w', encoding='utf-8') as file:
            file.write(content)

def Cookie_signin():
    """
    如何跳过登录界面爬取数据
    登陆后拿到cookie和referer写入到headers中，再封装到request即可
    """
    pass

def Handler():
    """
    用handler代替urlopen方法来访问url，可以定制更为高级的request（动态cookie和代理）
    """
    url = 'https://www.baidu.com'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'}
    request1 = request.Request(url=url, headers=headers)
    # HTTPHandler(), build_opener(), open()
    # 等效于urlopen
    handler1 = request.HTTPHandler()
    opener = request.build_opener(handler1)
    response = opener.open(request1)

    content = response.read().decode('utf-8')
    print(content)


def replace_ip():
    url = 'https://baidu.com/s?wd=ip'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'}
    request1 = request.Request(url=url, headers=headers)
    # 代理ip：proxy
    proxy = {'http':'202.101.213.191:17124'}
    # 利用proxyHandler(proxies=proxy)实现代理ip
    handler1 = request.ProxyHandler(proxies=proxy)
    opener = request.build_opener(handler1)
    response = opener.open(request1)
    content = response.read().decode('utf-8')
    with open('./daili.html', 'w', encoding='utf-8') as file:
        file.write(content)






replace_ip()








