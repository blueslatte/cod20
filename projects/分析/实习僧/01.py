import requests
from bs4 import BeautifulSoup
import pandas as pd


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/75.0.3770.100 Safari/537.36"}

data_list = []
def detail_url(url):
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    title = soup.title.text
    job = title.split("招聘")[0]
    company_name = soup.select('.com_intro .com-name')[0].text.strip()
    salary = soup.select(".job_money.cutom_font")[0].text.encode("utf-8")
    salary = salary.replace(b'\xef\x82\x9d', b"0")
    salary = salary.replace(b'\xee\xa6\x88', b"1")
    salary = salary.replace(b'\xee\xa8\xb4', b"2")
    salary = salary.replace(b'\xef\x91\xbe', b"3")
    salary = salary.replace(b'\xee\x88\x9d', b"4")
    salary = salary.replace(b'\xef\x97\x80', b"5")
    salary = salary.replace(b'\xee\x85\x9f', b"6")
    salary = salary.replace(b'\xee\x94\x9d', b"7")
    salary = salary.replace(b'\xee\xb1\x8a', b"8")
    salary = salary.replace(b'\xef\x86\xbf', b"9")
    salary = salary.decode()

    data_list.append({"job":job, "money":salary, "company":company_name})
    print("{}\t{}\t{}\t\t{}".format(job, salary, company_name, len(data_list)))




def job_url():
    for i in range(109):
        req = requests.get(
            f'https://www.shixiseng.com/interns?page={i}&keyword=Python&type=intern&area=&months=&days=&degree=&official=&enterprise=&salary=-0&publishTime=&sortType=&city=%E6%B7%B1%E5%9C%B3&internExtend=',
            headers=headers)
        html = req.text
        soup = BeautifulSoup(html, 'lxml')
        offers = soup.select('.intern-wrap.intern-item')
        for offer in offers:
            url = offer.select(" .f-l.intern-detail__job a")[0]['href']
            detail_url(url)


job_url()

fileName = '实习僧.csv'
number = 1

data = pd.DataFrame(data_list)

try:
    if number == 1:
        csv_headers = ['job', 'money','company']
        data.to_csv(fileName, header=csv_headers, index=False, mode='w+', encoding='utf-8')
        print("write down！{}data".format(len(data_list)))
    else:
        data.to_csv(fileName, header=False, index=False, mode='w+', encoding='utf-8')
    number = number + 1
except UnicodeEncodeError:
    print("编码错误, 该数据无法写到文件中, 直接忽略该数据")
