from lxml import etree
import json
import re
html = etree.parse('./01.txt', etree.HTMLParser())
scr = html.xpath('//script/text()')
str1 = scr[3]
print(str1)
output = ''
for i in str1:
    output += i
pattern = re.compile(r' {.*?};')
result1 = pattern.findall(output)
strin = result1[0]
strin = str(strin)[:len(strin)-1]
mes_to_json = json.loads(strin, strict=False)

print('*'*150)

# for i in mes_to_json['mods']['itemlist']['data']['auctions']:
#     print(type(i))

# for i in mes_to_json['mods']['itemlist']['data']['auctions'][0]:
#     print(i)
#
#
# for k in mes_to_json['mods']['itemlist']['data']['auctions'][0]:
#     print(k , mes_to_json['mods']['itemlist']['data']['auctions'][0][k])
#
# print(mes_to_json['mods']['itemlist']['data']['auctions'][0]['title'])
# print(mes_to_json['mods']['itemlist']['data']['auctions'][0]['raw_title'])
# print(mes_to_json['mods']['itemlist']['data']['auctions'][0]['pic_url'])
# print(mes_to_json['mods']['itemlist']['data']['auctions'][0]['detail_url'])
# print(mes_to_json['mods']['itemlist']['data']['auctions'][0]['view_price'])
# print(mes_to_json['mods']['itemlist']['data']['auctions'][0]['view_fee'])
# print(mes_to_json['mods']['itemlist']['data']['auctions'][0]['item_loc'])
# print(mes_to_json['mods']['itemlist']['data']['auctions'][0]['view_sales'])
# print(mes_to_json['mods']['itemlist']['data']['auctions'][0]['nick'])
# print(mes_to_json['mods']['itemlist']['data']['auctions'][0]['icon'])
# print(mes_to_json['mods']['itemlist']['data']['auctions'][0]['shopLink'])
# print(mes_to_json['mods']['itemlist']['data']['auctions'][0]['comment_url'])


def analysis_page(text,data):
    data = []
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
    for i in len(mes_to_json['mods']['itemlist']['data']['auctions']):
        data.append({'title':mes_to_json['mods']['itemlist']['data']['auctions'][i]['title'],
        'raw_title':mes_to_json['mods']['itemlist']['data']['auctions'][i]['raw_title'],
        'pic_url':mes_to_json['mods']['itemlist']['data']['auctions'][i]['pic_url'],
        'title':mes_to_json['mods']['itemlist']['data']['auctions'][i]['title'],
        'detail_url':mes_to_json['mods']['itemlist']['data']['auctions'][i]['detail_url'],
        'view_price':mes_to_json['mods']['itemlist']['data']['auctions'][i]['view_price'],
        'view_fee':mes_to_json['mods']['itemlist']['data']['auctions'][i]['view_fee'],
        'item_loc':mes_to_json['mods']['itemlist']['data']['auctions'][i]['item_loc'],
        'view_sales':mes_to_json['mods']['itemlist']['data']['auctions'][i]['view_sales'],
        'nick':mes_to_json['mods']['itemlist']['data']['auctions'][i]['nick'],
        'view_sales':mes_to_json['mods']['itemlist']['data']['auctions'][i]['view_sales'],
        'icon':mes_to_json['mods']['itemlist']['data']['auctions'][i]['icon'],
        'shopLink':mes_to_json['mods']['itemlist']['data']['auctions'][i]['shopLink'],
        'comment_url':mes_to_json['mods']['itemlist']['data']['auctions'][i]['comment_url']})
