import jieba
import jieba.analyse
import sqlite3
from snownlp import SnowNLP

conn = sqlite3.connect(r'..\db.sqlite3')
cursor = conn.cursor()
jieba.analyse.set_stop_words("stop_words.txt")
f = open(r"fashion.txt", 'rb').read()
f1 = open(r"fashion.txt",'r', encoding='utf-8')
text = f1.readlines()
text =  ''.join(text).strip('\n')
text_snow = SnowNLP(text)
sum = text_snow.summary(5)
summary = '，'.join(sum)
summary = summary + '。'
tags = jieba.analyse.extract_tags(f, topK=20, withWeight=True)
for tag in tags:
    cursor.execute('insert into dashboard_in_extract_tags (name,rank) values (?,?)', (tag[0], tag[1]))
    print("tag: %s\t\t weight: %f" % (tag[0],tag[1]))
print('=' * 40)
tags2 = jieba.analyse.textrank(f, topK=20, withWeight=True)
print(tags2)
for tag2 in tags2:
    cursor.execute('insert into dashboard_in_textrank (name,rank) values (?,?)', (tag2[0], tag2[1]))
    print("tag: %s\t\t weight: %f" % (tag2[0],tag2[1]))
cursor.execute("delete from dashboard_latest")
cursor.execute("update sqlite_sequence SET seq = 0 where name ='dashboard_latest'")
cursor.execute(" insert into dashboard_latest (date,summary) values(datetime( 'now' , 'localtime' ),?)",(summary,))
conn.commit()