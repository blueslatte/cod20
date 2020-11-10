from lxml import etree
import username_login
import requests
import json
import re

loginId = '17393176228'
# 改版后增加的参数，后面考虑解密这个参数
umidToken = '9e195513b1b1ddadb79758230665b3df7831db58',
# 淘宝重要参数，从浏览器或抓包工具中复制，可重复使用
ua = '134#B274eXXwXGfl0xUxUXsSd60D3QROwKO9sE/w4/P9KlQXjoUNR9CKrgi8PdJr9LaD9Oph8ZVZE1eqjAVfZYeRAlcF9qGRyhYLB9vWbAX4yMPUUUVV+JdqKXL3ZtwwTq1qijRmNyd3OOH8qkuj+ZROqcHSevowHbL+qguErJdbXgRAqy8U+X28XqcViPXt+TpKqq5QVkerBLoI4x4YNBa5nlQs5rD8ARdDOsQZZCy1gwOcVwJabhNNksyRJJqZRLboJgPhQNuqBL3sxo7bYaYysU+vywRxB8p8VUX9Oajftv6YLQa6xWLIRgOMk/OG3zLF9uY2yltQiQ44QaGQP9KwvFSY5E6X2tgKRW6jLJ9tvLAxFQuMMFnwK8u3yuuABb93AyrAPlBfgn5PkA2BSplwxKJ8EUAYggKqkTaKIUdmyvNL1FqggYbcW2i//U9gAfcQWrKwGrcQBWx/S1ERkpmpcWziFluEU0bNc03zNtYX9pa/q39jM5A5N3QmwhzgZBzertP27/YC3I/nPjQYTsYCHJII3cbZoxGTTLM9D86FmXWQt80XXTs8omdZ6M+K2F8N53w/qDRSwnc43993N5n9Pk2DEE4fG4CEU64q/iyj+EQ4uaR44BMmP0SHMOfdRkDOvmExQUm5EQDoiRcvJEG49eTefHijATAsoZ6gWXjSsJmejZdS7PwQwDTfdT9PRWeGLtujJAeEP4WvI4t1HB8TPYqPs9JhnEa34MsYLx3Gh7tUQZhHyf1p8deGGvYxQX8LBl6MqF4eoMAOznptmxFQoTSECXycvj1FL02gJnDCFBC8XlicICmYF7spszAyzkZ8A4YFCQ8BHp0ugxMwL2q3YtPCzZwavY9Gkb2tQLUMvLaEu2mkaoksSTqaj5xTaRXsA2Is9Ck4GhdnLZY3aVXJQUuMI88aWF9KhLrKixn/pcHqYhV8ACvfqBPBUtyJBoC8aEvfZkHrwIOCjPrVwnyFTe5K/9iLLjHnHG1oTaxPOKyxlzLrw6fBHG8VAvVVrk6nIppBFHHYN0+a6GYT0f4BqVWqCjhpme0sx5dQjk5B/7x+bZAha2vbF1nvKsmcdecgiJKaOvCTCa20rU75dRFJzGqWy8MOYrl17s6fM6OLFRClkRFW'
# 加密后的密码，从浏览器或抓包工具中复制，可重复使用
password2 = '0772cc1affb7de587b55f5287af4012db93562e0bfff62c29ead1dba3988f849ec06c6fd7eaef998ca8a99f101e30e91e9dcc5e8bd8618c4f865701e03cd3ba34c937b8618d02421c16bef0b12ee3ce666693e52fa26a92b6f5139d66e416003e8662c77457f4a3cea6ea809d7a154f675e91f0e7cc1747e75912f8ef1672589'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'
}
ul = username_login.UsernameLogin(loginId, umidToken, ua, password2)
res = ul.get_session()

datas = []


def analysis_page(text, lists):
    # print(text)
    html = etree.HTML(text)
    scr = html.xpath('//script/text()')
    str1 = scr[3]
    output = ''
    for i in str1:
        output += i
    pattern = re.compile(r' {.*?};')
    result1 = pattern.findall(output)
    strin = result1[0]
    strin = str(strin)[:len(strin) - 1]
    mes_to_json = json.loads(strin, strict=False)
    for i in range(len(mes_to_json['mods']['itemlist']['data']['auctions'])):
        lists.append({'title': mes_to_json['mods']['itemlist']['data']['auctions'][i]['title'],
                      'raw_title': mes_to_json['mods']['itemlist']['data']['auctions'][i]['raw_title'],
                      'pic_url': mes_to_json['mods']['itemlist']['data']['auctions'][i]['pic_url'],
                      'detail_url': mes_to_json['mods']['itemlist']['data']['auctions'][i]['detail_url'],
                      'view_price': mes_to_json['mods']['itemlist']['data']['auctions'][i]['view_price'],
                      'view_fee': mes_to_json['mods']['itemlist']['data']['auctions'][i]['view_fee'],
                      'item_loc': mes_to_json['mods']['itemlist']['data']['auctions'][i]['item_loc'],
                      'view_sales': mes_to_json['mods']['itemlist']['data']['auctions'][i]['view_sales'],
                      'nick': mes_to_json['mods']['itemlist']['data']['auctions'][i]['nick'],
                      'icon': mes_to_json['mods']['itemlist']['data']['auctions'][i]['icon'],
                      'shopLink': mes_to_json['mods']['itemlist']['data']['auctions'][i]['shopLink'],
                      'comment_url': mes_to_json['mods']['itemlist']['data']['auctions'][i]['comment_url']})


print("*" * 20)


def spider_paging(kws, page=1):
    proxy = {
        'http': '115.221.241.249:9999'
    }
    url = "https://s.taobao.com/search?q={kw}&s={pg}"
    kw = kws
    for i in range(page):
        pages = i
        urll = url.format(kw=kw, pg=pages)
        print("begin:{}".format(urll))
        response = res.get(urll, headers=headers, proxies=proxy)
        analysis_page(response.text, datas)
        print("ok!")


spider_paging("电脑", 20)
print(len(datas))
json_data = {'data':datas}
with open("data.json", 'w') as f:
    # for i in datas:
    #     f.write('{')
    #     for j in i:
    #         f.write(j)
    #         f.write(":")
    #         f.write(str(i[j]))
    #         f.write(",")
    #     f.write('}')
    #     f.write("\r\n")
    json.dump(json_data, f)


