from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from model import Score,Course,Score_plus,Student,db
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
app = Flask(__name__)
def figure(coursename,s_number): #参数：科目 学号————>学生该门课多学期分数折线图+全部学生平均成绩折线图
    # all_scores = Score_plus.query.filter_by(s_number=s_number,coursename=coursename).all()#该学生的所有次成绩
    s_scores=[] # y1 该学生所有学期的该门课分数
    for semester in range(1,7):
        s_score = Score_plus.query.filter_by(s_number=s_number,coursename=coursename,s_semester=semester).first()
        s_scores.append(s_score.score)

    average_scores=[] # y2
    for semester in range(1,7):
        scores = Score_plus.query.filter_by(coursename=coursename,s_semester=semester).all() #所有人该门课的成绩
        # 计算平均成绩
        sum,i=0,0
        for score in scores:
            sum+=score.score # 累计分数
            i+=1 # 累计人数
        average_scores.append(round(sum/i,2))
    # 横坐标x
    x = [1,2,3,4,5,6]

    return x,s_scores,average_scores
@app.route('/')
def hello():
    x,s_scores,average_scores = figure("语文","169094334")
    return render_template('112.html',x=x,s_scores=s_scores,average_scores=average_scores)

app.run()

# if __name__ == "__main__":
#     app.run()

# max_score = Score_plus.query.filter_by(coursename="语文",s_semester=3).order_by('-score').first()
# print(max_score.s_name)

# student_scores = Score_plus.query.filter_by(s_number="169094325").filter_by(s_semester=3).all()
# print(student_scores)
# for student_score in student_scores:
#     print(student_scores.query.filter_by(coursename="语文").first().s_semester)
# for i in range(0,9):
#     print(Score_plus.query.filter_by(s_number="169094325",s_semester=3).order_by('-score').filter_by(coursename=["语文",'数学','英语','物理','化学','生物','政治','历史','地理'].pop(i)).first().s_semester)

# student_scores = Score_plus.query.filter_by(coursename="语文").filter_by(s_semester=3).first()
# print(student_scores.s_name,student_scores.s_semester)


# def figure(coursename,s_number): #参数：科目 学号————>学生该门课多学期分数折线图+全部学生平均成绩折线图
#     # all_scores = Score_plus.query.filter_by(s_number=s_number,coursename=coursename).all()#该学生的所有次成绩
#     s_scores=[] # y1 该学生所有学期的该门课分数
#     for semester in range(1,7):
#         s_score = Score_plus.query.filter_by(s_number=s_number,coursename=coursename,s_semester=semester).first()
#         s_scores.append(s_score.score)

#     average_scores=[] # y2
#     for semester in range(1,7):
#         scores = Score_plus.query.filter_by(coursename=coursename,s_semester=semester).all() #所有人该门课的成绩
#         # 计算平均成绩
#         sum,i=0,0
#         for score in scores:
#             sum+=score.score # 累计分数
#             i+=1 # 累计人数
#         average_scores.append(round(sum/i,2))
#     # 横坐标x
#     x = range(1,7)

#     return x,s_scores,average_scores

#作图
# x,s_scores,average_scores = figure("语文","169094334")
# plt.plot(x,s_scores)
# plt.plot(x,average_scores)
# plt.savefig('C:/Users/lcb/gitpro/flask_git/static/figure/new_plot.png')
# plt.show()



    















# scores_average = [] # 九门课平均成绩
# all_courses = ["语文",'数学','英语','物理','化学','生物','政治','历史','地理']
# text_semester=3 # 考试的学期
# score_all = [] #某个人该学期的九门成绩
# for coursename in all_courses:
#     #计算某位同学该门课的所有次成绩
#     scores = Score_plus.query.filter_by(s_number="169094349",coursename=coursename).all()

#     for i in range (0,7):#(0,s_semester)
#         score_all[index][i](scores[i].query.filter_by(s_semester=i).first()) # 某门课（coursename）的i次成绩

#     # 计算平均成绩
#     sum,j = 0,0
#     for i in range (0,7):#(0,s_semester)
#         student_scores = Score_plus.query.filter_by(coursename=coursename,s_semester=i).all()
#         for student_score in student_scores:
#             sum += student_score.score
#             i+=1
#         scores_average[index][j] = sum/i
#         j+=1
#     index+=1
    

    

# x,y1,y2=[],[],[]
# for score in score_all[0]:
#     x.append(score.coursename)
#     y1.append(score.score)   

# for score in scores_average[0]:
#     y2.append(score) 
# plt.plot(x,y1)
# plt.plot(x,y2)
# plt.savefig('C:/Users/lcb/gitpro/flask_git/static/figure/new_plot.png')
# plt.show()





# from flask import Flask,render_template,request
# from flask_sqlalchemy import SQLAlchemy
# from model import Score,Course,Score_plus,Student,db
# import matplotlib.pyplot as plt
# import matplotlib as mpl
# mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
# mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
# # app = Flask(__name__)
# # @app.route('/')
# # def hello():
# #     return render_template('add_student.html')

# # if __name__ == "__main__":
# #     app.run()

# # max_score = Score_plus.query.filter_by(coursename="语文",s_semester=3).order_by('-score').first()
# # print(max_score.s_name)

# # student_scores = Score_plus.query.filter_by(s_number="169094325").filter_by(s_semester=3).all()
# # print(student_scores)
# # for student_score in student_scores:
# #     print(student_scores.query.filter_by(coursename="语文").first().s_semester)
# # for i in range(0,9):
# #     print(Score_plus.query.filter_by(s_number="169094325",s_semester=3).order_by('-score').filter_by(coursename=["语文",'数学','英语','物理','化学','生物','政治','历史','地理'].pop(i)).first().s_semester)

# # student_scores = Score_plus.query.filter_by(coursename="语文").filter_by(s_semester=3).first()
# # print(student_scores.s_name,student_scores.s_semester)


# scores_average,index = [[0]*9 for i in range(6)],0
# all_courses = ["语文",'数学','英语','物理','化学','生物','政治','历史','地理'],[]
# score_all=[[0]*9 for i in range(6)] # 某门课（coursename）的所有次成绩   9门*6次
# for coursename in all_courses:
#     #计算某位同学该门课的所有次成绩
#     scores = Score_plus.query.filter_by(s_number="169094349",coursename=coursename).all()

#     for i in range (0,7):#(0,s_semester)
#         score_all[index][i](scores[i].query.filter_by(s_semester=i).first()) # 某门课（coursename）的i次成绩

#     # 计算平均成绩
#     sum,j = 0,0
#     for i in range (0,7):#(0,s_semester)
#         student_scores = Score_plus.query.filter_by(coursename=coursename,s_semester=i).all()
#         for student_score in student_scores:
#             sum += student_score.score
#             i+=1
#         scores_average[index][j] = sum/i
#         j+=1
#     index+=1
    

    

# x,y1,y2=[],[],[]
# for score in score_all[0]:
#     x.append(score.coursename)
#     y1.append(score.score)   

# for score in scores_average[0]:
#     y2.append(score) 
# plt.plot(x,y1)
# plt.plot(x,y2)
# plt.savefig('C:/Users/lcb/gitpro/flask_git/static/figure/new_plot.png')
# plt.show()

