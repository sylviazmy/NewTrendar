from snownlp import SnowNLP
from collections import OrderedDict
import jieba
import jieba.analyse
import sqlite3
import re
jieba.load_userdict("mydict.txt")

###############################
#情感分析，判断筛选出负面评论
###############################

typ = [[],[],[],[],[],[],[],[]]
typ[0] = []
for word in open ("C:\\Users\\I321338\\PycharmProjects\\Trendar\\machine_learning\\type1.txt","r",encoding="utf8"):
    typ[0].append(word.strip())
    typ[0].append(' ')
typ[1] = []
for word in open ("C:\\Users\\I321338\\PycharmProjects\\Trendar\\machine_learning\\type2.txt","r",encoding="utf8"):
    typ[1].append(word.strip())
    typ[1].append(' ')
typ[2] = []
for word in open ("C:\\Users\\I321338\\PycharmProjects\\Trendar\\machine_learning\\type3.txt","r",encoding="utf8"):
    typ[2].append(word.strip())
    typ[2].append(' ')
typ[3] = []
for word in open ("C:\\Users\\I321338\\PycharmProjects\\Trendar\\machine_learning\\type4.txt","r",encoding="utf8"):
    typ[3].append(word.strip())
    typ[3].append(' ')
typ[4] = []
for word in open ("C:\\Users\\I321338\\PycharmProjects\\Trendar\\machine_learning\\type5.txt","r",encoding="utf8"):
    typ[4].append(word.strip())
    typ[4].append(' ')
typ[5] = []
for word in open ("C:\\Users\\I321338\\PycharmProjects\\Trendar\\machine_learning\\type6.txt","r",encoding="utf8"):
    typ[5].append(word.strip())
    typ[5].append(' ')
typ[6] = []
for word in open ("C:\\Users\\I321338\\PycharmProjects\\Trendar\\machine_learning\\type7.txt","r",encoding="utf8"):
    typ[6].append(word.strip())
    typ[6].append(' ')
typ[7] = []
for word in open ("C:\\Users\\I321338\\PycharmProjects\\Trendar\\machine_learning\\type8.txt","r",encoding="utf8"):
    typ[7].append(word.strip())
    typ[7].append(' ')

conn = sqlite3.connect(r'C:\Users\I321338\PycharmProjects\Trendar\db.sqlite3')
cursor = conn.cursor()
cursor.execute("delete from dashboard_negative")
cursor.execute("update sqlite_sequence SET seq = 0 where name ='dashboard_negative'")
cursor.execute("delete from dashboard_neg_total")
cursor.execute("update sqlite_sequence SET seq = 0 where name ='dashboard_neg_total'")
result = [[],[],[],[]]
f = open(r"C:\Users\I321338\PycharmProjects\Trendar\machine_learning\Demo_Ver0.1_500.txt",'r', encoding='utf-8')
total = OrderedDict()
total['物流'] = 0
total['掉毛'] = 0
total['鞋底'] = 0
total['客服'] = 0
total['包装'] = 0
total['有味道'] = 0
total['鞋码'] = 0
total['外观'] = 0
total['其他'] = 0

text = f.readline()
while text!="":
    text_snow = SnowNLP(text)
    score = text_snow.sentiments
    if score < 0.4:
        flag = True
        for index,val in enumerate(typ):
            seg_list = jieba.cut(text, cut_all=False)
            for j in seg_list:
                if (j in val) and (j != ' '):
                    if (index == 0):
                        typeof = '物流'
                        total['物流'] = total['物流']+1
                    elif (index == 1):
                        typeof = '掉毛'
                        total['掉毛'] = total['掉毛']+1
                    elif (index == 2):
                        typeof = '鞋底'
                        total['鞋底'] = total['鞋底']+1
                    elif (index == 3):
                        typeof = '客服'
                        total['客服'] = total['客服']+1
                    elif (index == 4):
                        typeof = '包装'
                        total['包装'] = total['包装']+1
                    elif (index == 5):
                        typeof = '有味道'
                        total['有味道'] = total['有味道']+1
                    elif (index == 6):
                        typeof = '鞋码'
                        total['鞋码'] = total['鞋码']+1
                    elif (index == 7):
                        typeof = '外观'
                        total['外观'] = total['外观']+1
                    #result[index].write(str(score) + ' ' + text)
                    cursor.execute('insert into dashboard_negative (typeof,score,content) values (?,?,?)', (typeof,score,text))
                    flag = False
                    break
        if flag:
            typeof = '其他'
            total['其他'] = total['其他']+1
            cursor.execute('insert into dashboard_negative (typeof,score,content) values (?,?,?)', (typeof,score,text))
        #r.write(text)
    text = f.readline()
for (k,v) in total.items():
    cursor.execute('insert into dashboard_neg_total (typeof,number) values (?,?)', (k,v))
f.close()
conn.commit()
# text = f.readline()
# while text!="":
#     seg_list = jieba.cut(text, cut_all=False)
#     output = " ".join(list(seg_list))
#     print("result: " + "/ ".join(seg_list))
#     r.write(output + '\n')
#     text = f.readline()




##############################
#负评分词
##############################
# f = open(r"C:\Users\I321338\PycharmProjects\Segmentation\Demo_Ver0.1_Sentiment500.txt",'r', encoding='utf-8').read()
# r = open(r"C:\Users\I321338\PycharmProjects\Segmentation\Demo_Ver0.1_Seg500.txt", 'w', encoding='utf-8')
# stopwords = []
# for word in open ("C:\\Users\\I321338\\PycharmProjects\\Segmentation\\stop_words.txt","r",encoding="utf8"):
#     stopwords.append(word.strip())
#     stopwords.append(' ')
# seg_list = jieba.cut(f, cut_all=False)
# final =""
# for word in seg_list:
#     if word not in stopwords:
#         if word == '\n':
#             final += word
#         else:
#             final += word + " "
# output = "".join(list(final))
# r.write(output + '\n')
# r.close()