from time import sleep
from selenium5_2_login import Login
import xlrd
from xml.dom import minidom

# ###########################直接写入用户名密码###########################
# # 创建Login类对象
# user_login = Login()

# # 患者1登录
# user_login.login("12200000000", "123456")
# # 患者登出
# user_login.logout()
# sleep(2)
#
# # 患者2登录
# user_login.login("12200000001", "123456")
# sleep(2)
#
# # 关闭浏览器
# user_login.quit()


# ##########################通过txt文件读取用户名密码################################
# # 创建Login类对象
# user_login = Login()
#
# users = open('E:\PycharmProjects\selenium2\selenium5_2_userfile.txt', 'r').readlines()
# for user in users:
#     # strip()为 去掉首尾处的空格
#     username = user.split(',')[0].strip()
#     password = user.split(',')[1].strip()
#     # 患者登录
#     user_login.login(username, password)
#     # 患者登出
#     user_login.logout()
#
# user_login.quit()


# ########################通过excel文件读取用户名密码##############################
# # 创建Login类对象
# user_login = Login()
#
# # 打开文件
# workbook = xlrd.open_workbook('E:\PycharmProjects\selenium2\selenium5_2_userfile.xlsx')
# # 获取第一个sheet的内容
# sheet = workbook.sheet_by_index(0)
# users = []
# # 获取excel中数据，并将数据中.0去掉
# for i in range(sheet.nrows):
#     if i != 0:
#         t = sheet.row_values(i)
#         s = []
#         for j in t:
#             j = str(j).split('.')[0]
#             s.append(j)
#
#         users.append(s)
#
# for user in users:
#     # strip()为 去掉首尾处的空格
#     username = user[0]
#     password = user[1]
#     # 患者登录
#     user_login.login(username, password)
#     # 患者登出
#     user_login.logout()
#
# user_login.quit()


# ##########################通过xml文件读取用户名密码################################
# 创建Login类对象
user_login = Login()

# 打开xml文件
xml = minidom.parse('E:\PycharmProjects\selenium2\selenium5_2_userfile.xml')

# 获取xml中元素对象
trees = xml.documentElement
# 打印节点名称
print(trees.nodeName)
# 打印tagname
tagname = trees.getElementsByTagName('path')
print(tagname[0].tagName)
# 打印标签属性值
print(tagname[0].firstChild.data)

logins = trees.getElementsByTagName('login')
for i in range(len(logins)):
    username = logins[i].getAttribute("username")
    password = logins[i].getAttribute("password")
    # 患者登录
    user_login.login(username, password)
    # 患者登出
    user_login.logout()

user_login.quit()

