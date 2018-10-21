from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from model import Score,Course,Score_plus,Student,db,User
# import matplotlib.pyplot as plt
# import matplotlib as mpl
if User.query.filter_by(username="李四四").first():
        print("有李四四")
if Score_plus.query.filter_by(s_name="李四四").first():
        print("有李四四")
if not Score_plus.query.filter_by(s_name="李五五").first():
        print("wu李五五")

# import xlrd
# import xlwt
# from datetime import date,datetime

# def read_excel():
#     # 打开文件
#     workbook = xlrd.open_workbook(r'C:\Users\lcb\Desktop\test.xlsx')
#     # 获取所有学生信息
#     sheet1 = workbook.sheet_by_index(0) # sheet索引从0开始

#     # 创建一个workbook 设置编码
#     workbook = xlwt.Workbook(encoding = 'utf-8')
#     # 创建一个worksheet
#     worksheet = workbook.add_sheet('My Worksheet')

#     for i in range(0,sheet1.nrows):
#         worksheet.write(i,0,sheet1.cell(i,0).value)
#         worksheet.write(i,1,sheet1.cell(i,1).value)
#         worksheet.write(i,2,sheet1.cell(i,2).value)

#         # 保存
#         workbook.save('C:/Users/lcb/Desktop/Excel_test.xls')
#         # print(sheet1.cell(i,0).value.encode('utf-8'))
#         # print(sheet1.cell(i,1).value.encode('utf-8'))
#         # print(sheet1.cell(i,2).value.encode('utf-8'))

# read_excel()

# # def write_excel():
# #     # 创建一个workbook 设置编码
# #     workbook = xlwt.Workbook(encoding = 'utf-8')
# #     # 创建一个worksheet
# #     worksheet = workbook.add_sheet('My Worksheet')
# #     # 写入excel
# #     # 参数对应 行, 列, 值
# #     worksheet.write(1,0,'uesrname')

# #     # 保存
# #     workbook.save('C:/Users/lcb/Desktop/Excel_test.xls')
# #     # row0 = ['username','password','radio']

# # write_excel()
