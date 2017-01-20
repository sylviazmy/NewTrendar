from snownlp import SnowNLP
import jieba
import jieba.analyse
import sqlite3
import re
jieba.load_userdict("mydict.txt")


conn = sqlite3.connect(r'C:\Users\I321338\PycharmProjects\Trendar\db.sqlite3')
cursor = conn.cursor()

f = open(r"C:\Users\I321338\PycharmProjects\Trendar\machine_learning\test500.txt",'r', encoding='utf-8')

text = f.readline()
sentiment = [0,0,0,0,0,0,0,0,0,0]
while text!="":
    ###############################
    #如果要把句子根据标点符号分开再来判断，把下面三句话解开注释
    #还要把Snownlp(text)的text改成i，r.write(text)的text改成i
    ###############################

    # file = re.split("\n|，|。|！|\ " ,text)
    # for i in file:
    #      if i != '':
            text_snow = SnowNLP(text)
            score = text_snow.sentiments
            sentiment[int(score*10)] = sentiment[int(score*10)]+1
            text = f.readline()

print(sentiment)
cursor.execute("delete from dashboard_sentiment")
cursor.execute("update sqlite_sequence SET seq = 0 where name ='dashboard_sentiment'")
for num in sentiment:
    # num = int(n)
    # print(num)
    cursor.execute(" insert into dashboard_sentiment (number) values(?)",(num,))
conn.commit()