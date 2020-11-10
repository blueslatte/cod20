import json

file_name="data.json"
with open(file_name) as f:
    data = json.load(f)
print(data)
# url = "https://s.taobao.com/search?q={kw}&s={page}"
# kw = "电脑"
# page = 20
# for i in range(page):
#     page = i
#     url = url.format(kw=kw, page=page)
#     print(i)
#     print(url)
#     print(url)