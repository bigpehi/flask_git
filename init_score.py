from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from model import Score,Course,Score_plus,Student,db,app
import random
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.drop_all()
db.create_all()

admin1 = Student('常雨','169094320',"男",18,4)
admin2 = Student('代章福','169094321',"男",18,4)
admin3 = Student('高忠','169094322',"男",18,4)
admin4 = Student('李陈斌','169094325',"男",18,4)
admin5 = Student('李雪','169094328',"女",18,4)
admin6 = Student('刘兆柱','169094329',"男",18,4)
admin7 = Student('柳亚雄','169144114',"男",18,4)
admin8 = Student('牛良伟','169094330',"男",18,4)
admin9 = Student('潘剑兵','169094331',"男",18,4)
admin10 = Student('钱丹丹','169094333',"女",18,4)
admin11 = Student('沈福莉','169094334',"女",18,4)
admin12 = Student('时微尘','169094336',"女",18,4)
admin13 = Student('谈成龙','169094337',"男",18,4)
admin14 = Student('汪鹏','169094338',"男",18,4)
admin15 = Student('汪艳','169094339',"女",18,4)
admin16 = Student('王宇','169094340',"男",18,4)
admin17 = Student('吴甜甜','169094341',"女",18,4)
admin18 = Student('许淼','169094343',"男",18,4)
admin19 = Student('许玉柱','169094344',"男",18,4)
admin20 = Student('薛家升','169094345',"男",18,4)
admin21 = Student('杨洁','169094346',"女",18,4)
admin22= Student('叶甜甜','169094347',"女",18,4)
admin23 = Student('张傲','169094348',"男",18,4)
admin24 = Student('张程','169094349',"男",18,4)
admin25 = Student('张建','169094350',"男",18,4)
admin26 = Student('张结宝','169104612',"男",18,4)
admin27 = Student('张伟','169094351',"男",18,4)
admin28 = Student('周力','169094352',"男",18,4)
admin29 = Student('朱海发','169094353',"男",18,4)
admin30 = Student('朱泽明','169094354',"男",18,4)


course1_1 = Course('语文',1,'语文老师','语文_一年级上')
course2_1 = Course('数学',1,'数学老师','数学_一年级上')
course3_1 = Course('英语',1,'英语老师','英语_一年级上')
course4_1 = Course('物理',1,'物理老师','物理_一年级上')
course5_1 = Course('化学',1,'化学老师','化学_一年级上')
course6_1 = Course('生物',1,'生物老师','生物_一年级上')
course7_1 = Course('地理',1,'地理老师','地理_一年级上')
course8_1 = Course('政治',1,'政治老师','政治_一年级上')
course9_1 = Course('历史',1,'历史老师','历史_一年级上')


course1_2 = Course('语文',2,'语文老师','语文_一年级下')
course2_2 = Course('数学',2,'数学老师','数学_一年级下')
course3_2 = Course('英语',2,'英语老师','英语_一年级下')
course4_2 = Course('物理',2,'物理老师','物理_一年级下')
course5_2 = Course('化学',2,'化学老师','化学_一年级下')
course6_2 = Course('生物',2,'生物老师','生物_一年级下')
course7_2 = Course('地理',2,'地理老师','地理_一年级下')
course8_2 = Course('政治',2,'政治老师','政治_一年级下')
course9_2 = Course('历史',2,'历史老师','历史_一年级下')

course1_3 = Course('语文',3,'语文老师','语文_二年级上')
course2_3 = Course('数学',3,'数学老师','数学_二年级上')
course3_3 = Course('英语',3,'英语老师','英语_二年级上')
course4_3 = Course('物理',3,'物理老师','物理_二年级上')
course5_3 = Course('化学',3,'化学老师','化学_二年级上')
course6_3 = Course('生物',3,'生物老师','生物_二年级上')
course7_3 = Course('地理',3,'地理老师','地理_二年级上')
course8_3 = Course('政治',3,'政治老师','政治_二年级上')
course9_3 = Course('历史',3,'历史老师','历史_二年级上')


course1_4 = Course('语文',4,'语文老师','语文_二年级下')
course2_4 = Course('数学',4,'数学老师','数学_二年级下')
course3_4 = Course('英语',4,'英语老师','英语_二年级下')
course4_4 = Course('物理',4,'物理老师','物理_二年级下')
course5_4 = Course('化学',4,'化学老师','化学_二年级下')
course6_4 = Course('生物',4,'生物老师','生物_二年级下')
course7_4 = Course('地理',4,'地理老师','地理_二年级下')
course8_4 = Course('政治',4,'政治老师','政治_二年级下')
course9_4 = Course('历史',4,'历史老师','历史_二年级下')


course1_5 = Course('语文',5,'语文老师','语文_三年级上')
course2_5 = Course('数学',5,'数学老师','数学_三年级上')
course3_5 = Course('英语',5,'英语老师','英语_三年级上')
course4_5 = Course('物理',5,'物理老师','物理_三年级上')
course5_5 = Course('化学',5,'化学老师','化学_三年级上')
course6_5 = Course('生物',5,'生物老师','生物_三年级上')
course7_5 = Course('地理',5,'地理老师','地理_三年级上')
course8_5 = Course('政治',5,'政治老师','政治_三年级上')
course9_5 = Course('历史',5,'历史老师','历史_三年级上')


course1_6 = Course('语文',6,'语文老师','语文_三年级下')
course2_6 = Course('数学',6,'数学老师','数学_三年级下')
course3_6 = Course('英语',6,'英语老师','英语_三年级下')
course4_6 = Course('物理',6,'物理老师','物理_三年级下')
course5_6 = Course('化学',6,'化学老师','化学_三年级下')
course6_6 = Course('生物',6,'生物老师','生物_三年级下')
course7_6 = Course('地理',6,'地理老师','地理_三年级下')
course8_6 = Course('政治',6,'政治老师','政治_三年级下')
course9_6 = Course('历史',6,'历史老师','历史_三年级下')
db.session.add_all([course1_1,course2_1,course3_1,course4_1,course5_1,course6_1,course8_1,course9_1,course1_2,course2_2,course3_2,course4_2,course5_2,course6_2,course7_2,course8_2,course9_2,course1_3,course2_3,course3_3,course4_3,course5_3,course6_3,course7_3,course8_3,course9_3,course1_4,course2_4,course3_4,course4_4,course5_4,course6_4,course7_4,course8_4,course9_4,course1_5,course2_5,course3_5,course4_5,course5_5,course6_5,course7_5,course8_5,course9_5,course1_6,course2_6,course3_6,course4_6,course5_6,course6_6,course7_6,course8_6,course9_6])
db.session.add_all([admin1,admin2,admin3,admin4,admin5,admin6,admin7,admin8,admin9,admin10,admin11,admin12,admin13,admin14,admin15,admin16,admin17,admin18,admin19,admin20,admin21,admin22,admin23,admin24,admin25,admin26,admin27,admin28,admin29,admin30])


admin1.course = [course1_1,course2_1,course3_1,course4_1,course5_1,course6_1,course7_1,course8_1,course9_1,course1_2,course2_2,course3_2,course4_2,course5_2,course6_2,course7_2,course8_2,course9_2,course1_3,course2_3,course3_3,course4_3,course5_3,course6_3,course7_3,course8_3,course9_3,course1_4,course2_4,course3_4,course4_4,course5_4,course6_4,course7_4,course8_4,course9_4,course1_5,course2_5,course3_5,course4_5,course5_5,course6_5,course7_5,course8_5,course9_5,course1_6,course2_6,course3_6,course4_6,course5_6,course6_6,course7_6,course8_6,course9_6]
admin2.course = [course1_1,course2_1,course3_1,course4_1,course5_1,course6_1,course7_1,course8_1,course9_1,course1_2,course2_2,course3_2,course4_2,course5_2,course6_2,course7_2,course8_2,course9_2,course1_3,course2_3,course3_3,course4_3,course5_3,course6_3,course7_3,course8_3,course9_3,course1_4,course2_4,course3_4,course4_4,course5_4,course6_4,course7_4,course8_4,course9_4,course1_5,course2_5,course3_5,course4_5,course5_5,course6_5,course7_5,course8_5,course9_5,course1_6,course2_6,course3_6,course4_6,course5_6,course6_6,course7_6,course8_6,course9_6]
admin3.course = [course1_1,course2_1,course3_1,course4_1,course5_1,course6_1,course7_1,course8_1,course9_1,course1_2,course2_2,course3_2,course4_2,course5_2,course6_2,course7_2,course8_2,course9_2,course1_3,course2_3,course3_3,course4_3,course5_3,course6_3,course7_3,course8_3,course9_3,course1_4,course2_4,course3_4,course4_4,course5_4,course6_4,course7_4,course8_4,course9_4,course1_5,course2_5,course3_5,course4_5,course5_5,course6_5,course7_5,course8_5,course9_5,course1_6,course2_6,course3_6,course4_6,course5_6,course6_6,course7_6,course8_6,course9_6]
admin4.course = [course1_1,course2_1,course3_1,course4_1,course5_1,course6_1,course7_1,course8_1,course9_1,course1_2,course2_2,course3_2,course4_2,course5_2,course6_2,course7_2,course8_2,course9_2,course1_3,course2_3,course3_3,course4_3,course5_3,course6_3,course7_3,course8_3,course9_3,course1_4,course2_4,course3_4,course4_4,course5_4,course6_4,course7_4,course8_4,course9_4,course1_5,course2_5,course3_5,course4_5,course5_5,course6_5,course7_5,course8_5,course9_5,course1_6,course2_6,course3_6,course4_6,course5_6,course6_6,course7_6,course8_6,course9_6]
admin5.course = [course1_1,course2_1,course3_1,course4_1,course5_1,course6_1,course7_1,course8_1,course9_1,course1_2,course2_2,course3_2,course4_2,course5_2,course6_2,course7_2,course8_2,course9_2,course1_3,course2_3,course3_3,course4_3,course5_3,course6_3,course7_3,course8_3,course9_3,course1_4,course2_4,course3_4,course4_4,course5_4,course6_4,course7_4,course8_4,course9_4,course1_5,course2_5,course3_5,course4_5,course5_5,course6_5,course7_5,course8_5,course9_5,course1_6,course2_6,course3_6,course4_6,course5_6,course6_6,course7_6,course8_6,course9_6]
admin6.course = [course1_1,course2_1,course3_1,course4_1,course5_1,course6_1,course7_1,course8_1,course9_1,course1_2,course2_2,course3_2,course4_2,course5_2,course6_2,course7_2,course8_2,course9_2,course1_3,course2_3,course3_3,course4_3,course5_3,course6_3,course7_3,course8_3,course9_3,course1_4,course2_4,course3_4,course4_4,course5_4,course6_4,course7_4,course8_4,course9_4,course1_5,course2_5,course3_5,course4_5,course5_5,course6_5,course7_5,course8_5,course9_5,course1_6,course2_6,course3_6,course4_6,course5_6,course6_6,course7_6,course8_6,course9_6]
admin7.course = [course1_1,course2_1,course3_1,course4_1,course5_1,course6_1,course7_1,course8_1,course9_1,course1_2,course2_2,course3_2,course4_2,course5_2,course6_2,course7_2,course8_2,course9_2,course1_3,course2_3,course3_3,course4_3,course5_3,course6_3,course7_3,course8_3,course9_3,course1_4,course2_4,course3_4,course4_4,course5_4,course6_4,course7_4,course8_4,course9_4,course1_5,course2_5,course3_5,course4_5,course5_5,course6_5,course7_5,course8_5,course9_5,course1_6,course2_6,course3_6,course4_6,course5_6,course6_6,course7_6,course8_6,course9_6]
admin8.course = [course1_1,course2_1,course3_1,course4_1,course5_1,course6_1,course7_1,course8_1,course9_1,course1_2,course2_2,course3_2,course4_2,course5_2,course6_2,course7_2,course8_2,course9_2,course1_3,course2_3,course3_3,course4_3,course5_3,course6_3,course7_3,course8_3,course9_3,course1_4,course2_4,course3_4,course4_4,course5_4,course6_4,course7_4,course8_4,course9_4,course1_5,course2_5,course3_5,course4_5,course5_5,course6_5,course7_5,course8_5,course9_5,course1_6,course2_6,course3_6,course4_6,course5_6,course6_6,course7_6,course8_6,course9_6]
admin9.course = [course1_1,course2_1,course3_1,course4_1,course5_1,course6_1,course7_1,course8_1,course9_1,course1_2,course2_2,course3_2,course4_2,course5_2,course6_2,course7_2,course8_2,course9_2,course1_3,course2_3,course3_3,course4_3,course5_3,course6_3,course7_3,course8_3,course9_3,course1_4,course2_4,course3_4,course4_4,course5_4,course6_4,course7_4,course8_4,course9_4,course1_5,course2_5,course3_5,course4_5,course5_5,course6_5,course7_5,course8_5,course9_5,course1_6,course2_6,course3_6,course4_6,course5_6,course6_6,course7_6,course8_6,course9_6]
admin10.course = [course1_1,course2_1,course3_1,course4_1,course5_1,course6_1,course7_1,course8_1,course9_1,course1_2,course2_2,course3_2,course4_2,course5_2,course6_2,course7_2,course8_2,course9_2,course1_3,course2_3,course3_3,course4_3,course5_3,course6_3,course7_3,course8_3,course9_3,course1_4,course2_4,course3_4,course4_4,course5_4,course6_4,course7_4,course8_4,course9_4,course1_5,course2_5,course3_5,course4_5,course5_5,course6_5,course7_5,course8_5,course9_5,course1_6,course2_6,course3_6,course4_6,course5_6,course6_6,course7_6,course8_6,course9_6]
admin11.course = [course1_1,course2_1,course3_1,course4_1,course5_1,course6_1,course7_1,course8_1,course9_1,course1_2,course2_2,course3_2,course4_2,course5_2,course6_2,course7_2,course8_2,course9_2,course1_3,course2_3,course3_3,course4_3,course5_3,course6_3,course7_3,course8_3,course9_3,course1_4,course2_4,course3_4,course4_4,course5_4,course6_4,course7_4,course8_4,course9_4,course1_5,course2_5,course3_5,course4_5,course5_5,course6_5,course7_5,course8_5,course9_5,course1_6,course2_6,course3_6,course4_6,course5_6,course6_6,course7_6,course8_6,course9_6]
admin12.course = [course1_1,course2_1,course3_1,course4_1,course5_1,course6_1,course7_1,course8_1,course9_1,course1_2,course2_2,course3_2,course4_2,course5_2,course6_2,course7_2,course8_2,course9_2,course1_3,course2_3,course3_3,course4_3,course5_3,course6_3,course7_3,course8_3,course9_3,course1_4,course2_4,course3_4,course4_4,course5_4,course6_4,course7_4,course8_4,course9_4,course1_5,course2_5,course3_5,course4_5,course5_5,course6_5,course7_5,course8_5,course9_5,course1_6,course2_6,course3_6,course4_6,course5_6,course6_6,course7_6,course8_6,course9_6]
admin13.course = [course1_1,course2_1,course3_1,course4_1,course5_1,course6_1,course7_1,course8_1,course9_1,course1_2,course2_2,course3_2,course4_2,course5_2,course6_2,course7_2,course8_2,course9_2,course1_3,course2_3,course3_3,course4_3,course5_3,course6_3,course7_3,course8_3,course9_3,course1_4,course2_4,course3_4,course4_4,course5_4,course6_4,course7_4,course8_4,course9_4,course1_5,course2_5,course3_5,course4_5,course5_5,course6_5,course7_5,course8_5,course9_5,course1_6,course2_6,course3_6,course4_6,course5_6,course6_6,course7_6,course8_6,course9_6]
admin14.course = [course1_1,course2_1,course3_1,course4_1,course5_1,course6_1,course7_1,course8_1,course9_1,course1_2,course2_2,course3_2,course4_2,course5_2,course6_2,course7_2,course8_2,course9_2,course1_3,course2_3,course3_3,course4_3,course5_3,course6_3,course7_3,course8_3,course9_3,course1_4,course2_4,course3_4,course4_4,course5_4,course6_4,course7_4,course8_4,course9_4,course1_5,course2_5,course3_5,course4_5,course5_5,course6_5,course7_5,course8_5,course9_5,course1_6,course2_6,course3_6,course4_6,course5_6,course6_6,course7_6,course8_6,course9_6]
admin15.course = [course1_1,course2_1,course3_1,course4_1,course5_1,course6_1,course7_1,course8_1,course9_1,course1_2,course2_2,course3_2,course4_2,course5_2,course6_2,course7_2,course8_2,course9_2,course1_3,course2_3,course3_3,course4_3,course5_3,course6_3,course7_3,course8_3,course9_3,course1_4,course2_4,course3_4,course4_4,course5_4,course6_4,course7_4,course8_4,course9_4,course1_5,course2_5,course3_5,course4_5,course5_5,course6_5,course7_5,course8_5,course9_5,course1_6,course2_6,course3_6,course4_6,course5_6,course6_6,course7_6,course8_6,course9_6]
admin16.course = [course1_1,course2_1,course3_1,course4_1,course5_1,course6_1,course7_1,course8_1,course9_1,course1_2,course2_2,course3_2,course4_2,course5_2,course6_2,course7_2,course8_2,course9_2,course1_3,course2_3,course3_3,course4_3,course5_3,course6_3,course7_3,course8_3,course9_3,course1_4,course2_4,course3_4,course4_4,course5_4,course6_4,course7_4,course8_4,course9_4,course1_5,course2_5,course3_5,course4_5,course5_5,course6_5,course7_5,course8_5,course9_5,course1_6,course2_6,course3_6,course4_6,course5_6,course6_6,course7_6,course8_6,course9_6]
admin17.course = [course1_1,course2_1,course3_1,course4_1,course5_1,course6_1,course7_1,course8_1,course9_1,course1_2,course2_2,course3_2,course4_2,course5_2,course6_2,course7_2,course8_2,course9_2,course1_3,course2_3,course3_3,course4_3,course5_3,course6_3,course7_3,course8_3,course9_3,course1_4,course2_4,course3_4,course4_4,course5_4,course6_4,course7_4,course8_4,course9_4,course1_5,course2_5,course3_5,course4_5,course5_5,course6_5,course7_5,course8_5,course9_5,course1_6,course2_6,course3_6,course4_6,course5_6,course6_6,course7_6,course8_6,course9_6]
admin18.course = [course1_1,course2_1,course3_1,course4_1,course5_1,course6_1,course7_1,course8_1,course9_1,course1_2,course2_2,course3_2,course4_2,course5_2,course6_2,course7_2,course8_2,course9_2,course1_3,course2_3,course3_3,course4_3,course5_3,course6_3,course7_3,course8_3,course9_3,course1_4,course2_4,course3_4,course4_4,course5_4,course6_4,course7_4,course8_4,course9_4,course1_5,course2_5,course3_5,course4_5,course5_5,course6_5,course7_5,course8_5,course9_5,course1_6,course2_6,course3_6,course4_6,course5_6,course6_6,course7_6,course8_6,course9_6]
admin19.course = [course1_1,course2_1,course3_1,course4_1,course5_1,course6_1,course7_1,course8_1,course9_1,course1_2,course2_2,course3_2,course4_2,course5_2,course6_2,course7_2,course8_2,course9_2,course1_3,course2_3,course3_3,course4_3,course5_3,course6_3,course7_3,course8_3,course9_3,course1_4,course2_4,course3_4,course4_4,course5_4,course6_4,course7_4,course8_4,course9_4,course1_5,course2_5,course3_5,course4_5,course5_5,course6_5,course7_5,course8_5,course9_5,course1_6,course2_6,course3_6,course4_6,course5_6,course6_6,course7_6,course8_6,course9_6]
admin20.course = [course1_1,course2_1,course3_1,course4_1,course5_1,course6_1,course7_1,course8_1,course9_1,course1_2,course2_2,course3_2,course4_2,course5_2,course6_2,course7_2,course8_2,course9_2,course1_3,course2_3,course3_3,course4_3,course5_3,course6_3,course7_3,course8_3,course9_3,course1_4,course2_4,course3_4,course4_4,course5_4,course6_4,course7_4,course8_4,course9_4,course1_5,course2_5,course3_5,course4_5,course5_5,course6_5,course7_5,course8_5,course9_5,course1_6,course2_6,course3_6,course4_6,course5_6,course6_6,course7_6,course8_6,course9_6]
admin21.course = [course1_1,course2_1,course3_1,course4_1,course5_1,course6_1,course7_1,course8_1,course9_1,course1_2,course2_2,course3_2,course4_2,course5_2,course6_2,course7_2,course8_2,course9_2,course1_3,course2_3,course3_3,course4_3,course5_3,course6_3,course7_3,course8_3,course9_3,course1_4,course2_4,course3_4,course4_4,course5_4,course6_4,course7_4,course8_4,course9_4,course1_5,course2_5,course3_5,course4_5,course5_5,course6_5,course7_5,course8_5,course9_5,course1_6,course2_6,course3_6,course4_6,course5_6,course6_6,course7_6,course8_6,course9_6]
admin22.course = [course1_1,course2_1,course3_1,course4_1,course5_1,course6_1,course7_1,course8_1,course9_1,course1_2,course2_2,course3_2,course4_2,course5_2,course6_2,course7_2,course8_2,course9_2,course1_3,course2_3,course3_3,course4_3,course5_3,course6_3,course7_3,course8_3,course9_3,course1_4,course2_4,course3_4,course4_4,course5_4,course6_4,course7_4,course8_4,course9_4,course1_5,course2_5,course3_5,course4_5,course5_5,course6_5,course7_5,course8_5,course9_5,course1_6,course2_6,course3_6,course4_6,course5_6,course6_6,course7_6,course8_6,course9_6]
admin23.course = [course1_1,course2_1,course3_1,course4_1,course5_1,course6_1,course7_1,course8_1,course9_1,course1_2,course2_2,course3_2,course4_2,course5_2,course6_2,course7_2,course8_2,course9_2,course1_3,course2_3,course3_3,course4_3,course5_3,course6_3,course7_3,course8_3,course9_3,course1_4,course2_4,course3_4,course4_4,course5_4,course6_4,course7_4,course8_4,course9_4,course1_5,course2_5,course3_5,course4_5,course5_5,course6_5,course7_5,course8_5,course9_5,course1_6,course2_6,course3_6,course4_6,course5_6,course6_6,course7_6,course8_6,course9_6]
admin24.course = [course1_1,course2_1,course3_1,course4_1,course5_1,course6_1,course7_1,course8_1,course9_1,course1_2,course2_2,course3_2,course4_2,course5_2,course6_2,course7_2,course8_2,course9_2,course1_3,course2_3,course3_3,course4_3,course5_3,course6_3,course7_3,course8_3,course9_3,course1_4,course2_4,course3_4,course4_4,course5_4,course6_4,course7_4,course8_4,course9_4,course1_5,course2_5,course3_5,course4_5,course5_5,course6_5,course7_5,course8_5,course9_5,course1_6,course2_6,course3_6,course4_6,course5_6,course6_6,course7_6,course8_6,course9_6]
admin25.course = [course1_1,course2_1,course3_1,course4_1,course5_1,course6_1,course7_1,course8_1,course9_1,course1_2,course2_2,course3_2,course4_2,course5_2,course6_2,course7_2,course8_2,course9_2,course1_3,course2_3,course3_3,course4_3,course5_3,course6_3,course7_3,course8_3,course9_3,course1_4,course2_4,course3_4,course4_4,course5_4,course6_4,course7_4,course8_4,course9_4,course1_5,course2_5,course3_5,course4_5,course5_5,course6_5,course7_5,course8_5,course9_5,course1_6,course2_6,course3_6,course4_6,course5_6,course6_6,course7_6,course8_6,course9_6]
admin26.course = [course1_1,course2_1,course3_1,course4_1,course5_1,course6_1,course7_1,course8_1,course9_1,course1_2,course2_2,course3_2,course4_2,course5_2,course6_2,course7_2,course8_2,course9_2,course1_3,course2_3,course3_3,course4_3,course5_3,course6_3,course7_3,course8_3,course9_3,course1_4,course2_4,course3_4,course4_4,course5_4,course6_4,course7_4,course8_4,course9_4,course1_5,course2_5,course3_5,course4_5,course5_5,course6_5,course7_5,course8_5,course9_5,course1_6,course2_6,course3_6,course4_6,course5_6,course6_6,course7_6,course8_6,course9_6]
admin27.course = [course1_1,course2_1,course3_1,course4_1,course5_1,course6_1,course7_1,course8_1,course9_1,course1_2,course2_2,course3_2,course4_2,course5_2,course6_2,course7_2,course8_2,course9_2,course1_3,course2_3,course3_3,course4_3,course5_3,course6_3,course7_3,course8_3,course9_3,course1_4,course2_4,course3_4,course4_4,course5_4,course6_4,course7_4,course8_4,course9_4,course1_5,course2_5,course3_5,course4_5,course5_5,course6_5,course7_5,course8_5,course9_5,course1_6,course2_6,course3_6,course4_6,course5_6,course6_6,course7_6,course8_6,course9_6]
admin28.course = [course1_1,course2_1,course3_1,course4_1,course5_1,course6_1,course7_1,course8_1,course9_1,course1_2,course2_2,course3_2,course4_2,course5_2,course6_2,course7_2,course8_2,course9_2,course1_3,course2_3,course3_3,course4_3,course5_3,course6_3,course7_3,course8_3,course9_3,course1_4,course2_4,course3_4,course4_4,course5_4,course6_4,course7_4,course8_4,course9_4,course1_5,course2_5,course3_5,course4_5,course5_5,course6_5,course7_5,course8_5,course9_5,course1_6,course2_6,course3_6,course4_6,course5_6,course6_6,course7_6,course8_6,course9_6]
admin29.course = [course1_1,course2_1,course3_1,course4_1,course5_1,course6_1,course7_1,course8_1,course9_1,course1_2,course2_2,course3_2,course4_2,course5_2,course6_2,course7_2,course8_2,course9_2,course1_3,course2_3,course3_3,course4_3,course5_3,course6_3,course7_3,course8_3,course9_3,course1_4,course2_4,course3_4,course4_4,course5_4,course6_4,course7_4,course8_4,course9_4,course1_5,course2_5,course3_5,course4_5,course5_5,course6_5,course7_5,course8_5,course9_5,course1_6,course2_6,course3_6,course4_6,course5_6,course6_6,course7_6,course8_6,course9_6]
admin30.course = [course1_1,course2_1,course3_1,course4_1,course5_1,course6_1,course7_1,course8_1,course9_1,course1_2,course2_2,course3_2,course4_2,course5_2,course6_2,course7_2,course8_2,course9_2,course1_3,course2_3,course3_3,course4_3,course5_3,course6_3,course7_3,course8_3,course9_3,course1_4,course2_4,course3_4,course4_4,course5_4,course6_4,course7_4,course8_4,course9_4,course1_5,course2_5,course3_5,course4_5,course5_5,course6_5,course7_5,course8_5,course9_5,course1_6,course2_6,course3_6,course4_6,course5_6,course6_6,course7_6,course8_6,course9_6]
db.session.commit()
# ######################################################


#初始化分数表
students = Student.query.all()

for student in students:
   
    courses = student.course
    for course in courses:
        i=random.uniform(60,100)
        score = Score_plus(student.s_number,student.s_name,course.semester,course.mingcheng,i)
        db.session.add(score)
        db.session.commit()



# student=Student.query.filter_by(s_name='常雨').first()
# print(student.course)
# # student.course.remove_all()
# db.session.delete(student)
# # print(student.course)
# db.session.commit() 






























# score1= Score('169094320','理','语文_一年级上',121)
# score2= Score('169094320','理','数学_一年级上',113)
# score3= Score('169094320','理','英语_一年级上',110)
# score4= Score('169094320','理','物理_一年级上',87)
# score5= Score('169094320','理','化学_一年级上',79)
# score6= Score('169094320','理','生物_一年级上',77)
# score7= Score('169094321','理','语文_一年级上',121)
# score8= Score('169094321','理','数学_一年级上',113)
# score9= Score('169094321','理','英语_一年级上',110)
# score10= Score('169094321','理','物理_一年级上',87)
# score11= Score('169094321','理','化学_一年级上',79)
# score12= Score('169094321','理','生物_一年级上',77)
# score13= Score('169094322','理','语文_一年级上',121)
# score14= Score('169094322','理','数学_一年级上',113)
# score15= Score('169094322','理','英语_一年级上',110)
# score16= Score('169094322','理','物理_一年级上',87)
# score17= Score('169094322','理','化学_一年级上',79)
# score18= Score('169094322','理','生物_一年级上',77)
# score19= Score('169094325','理','语文_一年级上',121)
# score20= Score('169094325','理','数学_一年级上',113)
# score21= Score('169094325','理','英语_一年级上',110)
# score22= Score('169094325','理','物理_一年级上',87)
# score23= Score('169094325','理','化学_一年级上',79)
# score24= Score('169094325','理','生物_一年级上',77)
# score25= Score('169094328','理','语文_一年级上',121)
# score26= Score('169094328','理','数学_一年级上',113)
# score27= Score('169094328','理','英语_一年级上',110)
# score28= Score('169094328','理','物理_一年级上',87)
# score29= Score('169094328','理','化学_一年级上',79)
# score30= Score('169094328','理','生物_一年级上',77)
# score31= Score('169094329','理','语文_一年级上',121)
# score32= Score('169094329','理','数学_一年级上',113)
# score33= Score('169094329','理','英语_一年级上',110)
# score34= Score('169094329','理','物理_一年级上',87)
# score35= Score('169094329','理','化学_一年级上',79)
# score36= Score('169094329','理','生物_一年级上',77)
# score37= Score('169144114','理','语文_一年级上',121)
# score38= Score('169144114','理','数学_一年级上',113)
# score39= Score('169144114','理','英语_一年级上',110)
# score40= Score('169144114','理','物理_一年级上',87)
# score41= Score('169144114','理','化学_一年级上',79)
# score42= Score('169144114','理','生物_一年级上',77)
# score43= Score('169094330','理','语文_一年级上',121)
# score44= Score('169094330','理','数学_一年级上',113)
# score45= Score('169094330','理','英语_一年级上',110)
# score46= Score('169094330','理','物理_一年级上',87)
# score47= Score('169094330','理','化学_一年级上',79)
# score48= Score('169094330','理','生物_一年级上',77)
# score49= Score('169094331','理','语文_一年级上',121)
# score50= Score('169094331','理','数学_一年级上',113)
# score51= Score('169094331','理','英语_一年级上',110)
# score52= Score('169094331','理','物理_一年级上',87)
# score53= Score('169094331','理','化学_一年级上',79)
# score54= Score('169094331','理','生物_一年级上',77)
# score55= Score('169094333','理','语文_一年级上',121)
# score56= Score('169094333','理','数学_一年级上',113)
# score57= Score('169094333','理','英语_一年级上',110)
# score58= Score('169094333','理','物理_一年级上',87)
# score59= Score('169094333','理','化学_一年级上',79)
# score60= Score('169094333','理','生物_一年级上',77)
# score61= Score('169094334','理','语文_一年级上',121)
# score62= Score('169094334','理','数学_一年级上',113)
# score63= Score('169094334','理','英语_一年级上',110)
# score64= Score('169094334','理','物理_一年级上',87)
# score65= Score('169094334','理','化学_一年级上',79)
# score66= Score('169094334','理','生物_一年级上',77)
# score67= Score('169094336','理','语文_一年级上',121)
# score68= Score('169094336','理','数学_一年级上',113)
# score69= Score('169094336','理','英语_一年级上',110)
# score70= Score('169094336','理','物理_一年级上',87)
# score71= Score('169094336','理','化学_一年级上',79)
# score72= Score('169094336','理','生物_一年级上',77)
# score73= Score('169094337','理','语文_一年级上',121)
# score74= Score('169094337','理','数学_一年级上',113)
# score75= Score('169094337','理','英语_一年级上',110)
# score76= Score('169094337','理','物理_一年级上',87)
# score77= Score('169094337','理','化学_一年级上',79)
# score78= Score('169094337','理','生物_一年级上',77)
# score79= Score('169094338','理','语文_一年级上',121)
# score80= Score('169094338','理','数学_一年级上',113)
# score81= Score('169094338','理','英语_一年级上',110)
# score82= Score('169094338','理','物理_一年级上',87)
# score83= Score('169094338','理','化学_一年级上',79)
# score84= Score('169094338','理','生物_一年级上',77)
# score85= Score('169094339','理','语文_一年级上',121)
# score86= Score('169094339','理','数学_一年级上',113)
# score87= Score('169094339','理','英语_一年级上',110)
# score88= Score('169094339','理','物理_一年级上',87)
# score89= Score('169094339','理','化学_一年级上',79)
# score90= Score('169094339','理','生物_一年级上',77)
# score91= Score('169094340','理','语文_一年级上',121)
# score92= Score('169094340','理','数学_一年级上',113)
# score93= Score('169094340','理','英语_一年级上',110)
# score94= Score('169094340','理','物理_一年级上',87)
# score95= Score('169094340','理','化学_一年级上',79)
# score96= Score('169094340','理','生物_一年级上',77)
# score97= Score('169094341','文','语文_一年级上',121)
# score98= Score('169094341','文','数学_一年级上',113)
# score99= Score('169094341','文','英语_一年级上',110)
# score100= Score('169094341','文','历史_一年级上',87)
# score101= Score('169094341','文','政治_一年级上',79)
# score102= Score('169094341','文','地理_一年级上',77)
# score103= Score('169094343','文','语文_一年级上',121)
# score104= Score('169094343','文','数学_一年级上',113)
# score105= Score('169094343','文','英语_一年级上',110)
# score106= Score('169094343','文','历史_一年级上',87)
# score107= Score('169094343','文','政治_一年级上',79)
# score108= Score('169094343','文','地理_一年级上',77)
# score109= Score('169094344','文','语文_一年级上',121)
# score110= Score('169094344','文','数学_一年级上',113)
# score111= Score('169094344','文','英语_一年级上',110)
# score112= Score('169094344','文','历史_一年级上',87)
# score113= Score('169094344','文','政治_一年级上',79)
# score114= Score('169094344','文','地理_一年级上',77)
# score115= Score('169094345','文','语文_一年级上',121)
# score116= Score('169094345','文','数学_一年级上',113)
# score117= Score('169094345','文','英语_一年级上',110)
# score118= Score('169094345','文','历史_一年级上',87)
# score119= Score('169094345','文','政治_一年级上',79)
# score120= Score('169094345','文','地理_一年级上',77)
# score121= Score('169094346','文','语文_一年级上',121)
# score122= Score('169094346','文','数学_一年级上',113)
# score123= Score('169094346','文','英语_一年级上',110)
# score124= Score('169094346','文','历史_一年级上',87)
# score125= Score('169094346','文','政治_一年级上',79)
# score126= Score('169094346','文','地理_一年级上',77)
# score127= Score('169094347','文','语文_一年级上',121)
# score128= Score('169094347','文','数学_一年级上',113)
# score129= Score('169094347','文','英语_一年级上',110)
# score130= Score('169094347','文','历史_一年级上',87)
# score131= Score('169094347','文','政治_一年级上',79)
# score132= Score('169094347','文','地理_一年级上',77)
# score133= Score('169094348','文','语文_一年级上',121)
# score134= Score('169094348','文','数学_一年级上',113)
# score135= Score('169094348','文','英语_一年级上',110)
# score136= Score('169094348','文','历史_一年级上',87)
# score137= Score('169094348','文','政治_一年级上',79)
# score138= Score('169094348','文','地理_一年级上',77)
# score139= Score('169094349','文','语文_一年级上',121)
# score140= Score('169094349','文','数学_一年级上',113)
# score141= Score('169094349','文','英语_一年级上',110)
# score142= Score('169094349','文','历史_一年级上',87)
# score143= Score('169094349','文','政治_一年级上',79)
# score144= Score('169094349','文','地理_一年级上',77)
# score145= Score('169094350','文','语文_一年级上',121)
# score146= Score('169094350','文','数学_一年级上',113)
# score147= Score('169094350','文','英语_一年级上',110)
# score148= Score('169094350','文','历史_一年级上',87)
# score149= Score('169094350','文','政治_一年级上',79)
# score150= Score('169094350','文','地理_一年级上',77)
# score151= Score('169104612','文','语文_一年级上',121)
# score152= Score('169104612','文','数学_一年级上',113)
# score153= Score('169104612','文','英语_一年级上',110)
# score154= Score('169104612','文','历史_一年级上',87)
# score155= Score('169104612','文','政治_一年级上',79)
# score156= Score('169104612','文','地理_一年级上',77)
# score157= Score('169094351','文','语文_一年级上',121)
# score158= Score('169094351','文','数学_一年级上',113)
# score159= Score('169094351','文','英语_一年级上',110)
# score160= Score('169094351','文','历史_一年级上',87)
# score161= Score('169094351','文','政治_一年级上',79)
# score162= Score('169094351','文','地理_一年级上',77)
# score163= Score('169094352','文','语文_一年级上',121)
# score164= Score('169094352','文','数学_一年级上',113)
# score165= Score('169094352','文','英语_一年级上',110)
# score166= Score('169094352','文','历史_一年级上',87)
# score167= Score('169094352','文','政治_一年级上',79)
# score168= Score('169094352','文','地理_一年级上',77)
# score169= Score('169094353','文','语文_一年级上',121)
# score170= Score('169094353','文','数学_一年级上',113)
# score171= Score('169094353','文','英语_一年级上',110)
# score172= Score('169094353','文','历史_一年级上',87)
# score173= Score('169094353','文','政治_一年级上',79)
# score174= Score('169094353','文','地理_一年级上',77)
# score175= Score('169094354','文','语文_一年级上',121)
# score176= Score('169094354','文','数学_一年级上',113)
# score177= Score('169094354','文','英语_一年级上',110)
# score178= Score('169094354','文','历史_一年级上',87)
# score179= Score('169094354','文','政治_一年级上',79)
# score180= Score('169094354','文','地理_一年级上',77)

# db.session.add_all([score1,score2,score3,score4,score5,score6,score7,score8,score9,score10,
# score11,score12,score13,score14,score15,score16,score17,score18,score19,score20,
# score21,score22,score23,score24,score25,score26,score27,score28,score29,score30,
# score31,score32,score33,score34,score35,score36,score37,score38,score39,score40,
# score41,score42,score43,score44,score45,score46,score47,score48,score49,score50,
# score51,score52,score53,score54,score55,score56,score57,score58,score59,score60,
# score61,score62,score63,score64,score65,score66,score67,score68,score69,score70,
# score71,score72,score73,score74,score75,score76,score77,score78,score79,score80,
# score81,score82,score83,score84,score85,score86,score87,score88,score89,score90,
# score91,score92,score93,score94,score95,score96,score97,score98,score99,score100,
# score101,score102,score103,score104,score105,score106,score107,score108,score109,score110,
# score111,score112,score113,score114,score115,score116,score117,score118,score119,score120,
# score121,score122,score123,score124,score125,score126,score127,score128,score129,score130,
# score131,score132,score133,score134,score135,score136,score137,score138,score139,score140,
# score141,score142,score143,score144,score145,score146,score147,score148,score149,score150,
# score151,score152,score153,score154,score155,score156,score157,score158,score159,score160,
# score161,score162,score163,score164,score165,score166,score167,score168,score169,score170,
# score171,score172,score173,score174,score175,score176,score177,score178,score179,score180,]
# )

# db.session.commit()