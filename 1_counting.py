import numpy as np
import os
import pandas as pd
urls = [
"http://www.google.com/a.txt",
"http://www.google.com.tw/a.txt",
"http://www.google.com/download/c.jpg",
"http://www.google.co.jp/a.txt",
"http://www.google.com/b.txt",
"https://facebook.com/movie/b.txt",
"http://yahoo.com/123/000/c.jpg",
"http://gliacloud.com/haha.png",
]


#print(os.path.basename("http://gliacloud.com/haha.png"))


fileList = [os.path.basename(x) for x in urls]

df = pd.DataFrame(fileList)


dfg = df.groupby([0]).size().sort_values(ascending=False).head(3)

for d in dfg.index:
    print(d, dfg[d])

