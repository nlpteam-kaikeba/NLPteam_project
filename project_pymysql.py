import pymysql
import pandas as pd
import time
import numpy as np
file_name = "/Users/lingrowzhang/Documents/Artificial-Intelligence-for-NLP/"
# 由于残缺数据的错误读取方式
# data = []
# with open(filename + 'news_chinese.csv', 'r') as f:
#     for a in f.readlines():
#         data.append(a.split("','"))
# data_table = pd.DataFrame(data = data)
# data = pd.read_csv(filename + "news_chinese.csv")

db = pymysql.connect("rm-8vbwj6507z6465505ro.mysql.zhangbei.rds.aliyuncs.com",
                     "root",
                     "AI@2019@ai",
                     "stu_db")
# 表名：news_chinese
cursor = db.cursor()
sql_test = """
        SELECT id, author, source, content, feature, title, url
        FROM news_chinese WHERE id < 10
        """
sql = """
        SELECT id, author, source, content, feature, title, url
        FROM news_chinese 
        """
# # SQL 删除语句
# # sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 提交修改
#    db.commit()
# except:
#    # 发生错误时回滚
#    db.rollback()

data_cursor = cursor.execute(sql)
result = cursor.fetchall()
all_result = list(result)

# # 残缺数据读取办法
# def str_error_to_dict(tmp):
#     str_data = tmp[2:].split("\",\"")
#     result = {}
#     for i, the_data in enumerate(str_data):
#         if i == 0:
#             result_str = "{\"" + the_data + "\""
#         elif the_data == "":
#             result_str = result_str + "}"
#         elif i == len(str_data) - 1:
#             tmp_str = the_data.split("\":")
#             if len(tmp_str) < 2:
#                 result_str = result_str + "}"
#             else:
#                 if tmp_str[1] == ""  or tmp_str[1] == "\"":
#                     result_str = result_str + "}"
#                 elif tmp_str[1][-1] == "}":
#                     result_str = result_str + ",\"" + the_data
#                 elif tmp_str[1][-1] == "\"":
#                     result_str = result_str + ",\"" + the_data + "}"
#                 elif tmp_str[1][-2] == "\"" and tmp_str[1][-1] == ",":
#                     result_str = result_str + ",\"" + the_data[:len(the_data) - 1] + "}"
#                 else:
#                     result_str = result_str + ",\"" + the_data + "\"}"
#         else:
#             result_str = result_str + ",\"" + the_data + "\""
#     result = eval(result_str)
#     return result
# data_list = []
# data_list_error = []
# error_label = 0
# for i_the_result, the_result in enumerate(all_result):
#     the_data_list = []
#     for i, tmp in enumerate(list(the_result)):
#         if i == 4:
#             try:
#                 the_data_list.append(str_error_to_dict(tmp))
#             except:
#                 print(i_the_result)
#                 print(the_result)
#                 error_label = 1
#                 the_data_list.append(all_result[i_the_result][4][:-1])
#         else:
#             the_data_list.append(tmp)
#     if error_label == 1:
#         the_data_list = list(all_result[i_the_result][:4])
#         the_data_list.append(all_result[i_the_result][4][:-1])
#         the_data_list += list(all_result[i_the_result][5:])
#         data_list.append(the_data_list)
#         error_label = 0
#     else:
#         data_list.append(the_data_list)
# data_table = pd.DataFrame(data=data_list)

data_table = pd.read_csv(file_name + "data/news_chinese.csv")




data_table.to_csv(file_name + "news_chinese.csv", encoding="utf-8", index=False)



