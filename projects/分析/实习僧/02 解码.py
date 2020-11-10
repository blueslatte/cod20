import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}


def get_code(url,x,y):
    req = requests.get(url, headers=headers)
    html = req.text
    soup = BeautifulSoup(html, "lxml")
    job = soup.title.text.split("招聘")[0]
    company_name = soup.select('.com_intro .com-name')[0].text.strip()
    salary_text = soup.select(".job_money.cutom_font")[0].text
    # print("工作职位的名称为：{}\n薪金为：{}\n招聘公司的名称为：{}\n".format(job, salary_text, company_name))
    print("该页面的薪金对应为:\n\n{}-{}/天".format(x,y))
    print(f"{salary_text}".encode("utf-8"))
    print("*"*75)

get_code("https://www.shixiseng.com/intern/inn_jqmifpmtcoms?pcm=pc_SearchList",150,150)

get_code("https://www.shixiseng.com/intern/inn_rmugerpitjhv?pcm=pc_SearchList",200,250)
get_code("https://www.shixiseng.com/intern/inn_x0ynqrfd1nqj?pcm=pc_SearchList",300, 400)
get_code("https://www.shixiseng.com/intern/inn_klehmsococfx?pcm=pc_SearchList",80,100)
get_code("https://www.shixiseng.com/intern/inn_gqip2zzz2cwm?pcm=pc_SearchList", 500, 600)
