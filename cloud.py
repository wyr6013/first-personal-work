import jieba
import json


comments_list=open('comments_list.txt', 'r',errors='ignore').read()

words=jieba.lcut(comments_list)
wordCollect={}
for i in words:
    if len(i)==1:
        continue
    else:
        wordCollect[i]=wordCollect.get(i,0)+1
items=list(wordCollect.items())
items.sort(key=lambda x: x[1],reverse=True)
#统计词频
countList=[]
for i in range(len(items)):
    countDict={}
    word,count=items[i]
    if count>=10:
        countDict['name']=word
        countDict['value']=count
        countList.append(countDict)
print(countList)
data={}
data['data']=countList
print(data)
with open('comments.json', 'w',errors='ignore') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
#写入json
