import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("实习僧.csv")
lens = 0
mid = []
# print(df["money"][2])
# print((re.findall(r"\d+", df["money"][2])[1]))
# print((re.findall(r"\d+", df["money"][2])[0]))
# print(int(re.findall(r"\d+", df["money"][2])[1])+int(re.findall(r"\d+", df["money"][2])[0]))
print(len(df["money"]))
for i in range(len(df["money"])):
    try:
        mid.append(int(re.findall(r"\d+", df["money"][i])[1])+int(re.findall(r"\d+", df["money"][i])[0]))
        lens += 1
    except Exception as e:
        print(e, "----some wrong")
        continue
a = 0 # <100
b = 0 # 100- 200
c = 0 # 200-300
d = 0 # 300 - 400
e = 0 # 400 - 500
f = 0 # 500 -
for i in range(len(mid)):
    if mid[i] < 100:
        a += 1
    elif mid[i] < 200:
        b += 1
    elif mid[i]< 300:
        c += 1
    elif mid[i] < 400:
        d += 1
    elif mid[i] < 500:
        e += 1
    else:
        f += 1
print('a:{}b:{}c:{}d:{}e:{}f:{}'.format(a,b,c,d,e,f))


fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

recipe = ["{}% < 100/d".format(round(a/lens*100,2)),
          "{}% 100 - 200 /d".format(round(b/lens*100,2)),
          "{}% 200 - 300 /d".format(round(c/lens*100,2)),
          "{}% 300 - 400 /d".format(round(d/lens*100,2)),
          "{}% 400 - 500 /d".format(round(e/lens*100,2)),
          "{}% > 500/d".format(round(f/lens*100,2)),]

data = [a, b, c, d, e, f]

wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-10)

bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(recipe[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, **kw)



plt.show()
plt.savefig("./pic.png")
