# 读写文件实例
with open ('test.txt','a') as f:
    f.write(' 234567')

with open ('test.txt','r') as f:
    print(f.read())

import csv

with open('test.csv','w') as f:
    w=csv.writer(f,delimiter=',')
    w.writerow(['one','two','three'])
    w.writerow(('four','five','six'))

with open('test.csv','r') as f:
    r=csv.reader(f,delimiter=',')

    for row in r:
        print(row)

