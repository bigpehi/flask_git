from flask import Flask
# 导入配置好的相关数据库信息
from flask_sqlalchemy import SQLAlchemy

# 启动
app = Flask(__name__)


# 配置数据库并定义数据库表模型类
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/courses'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
db = SQLAlchemy(app)
# 创建用户类 存储用户信息 用于登录
class Course(db.Model):
    __tablename__='course'
    mingcheng=db.Column(db.String(20),unique=False)
    semester=db.Column(db.Integer,unique=False)
    teacher=db.Column(db.String(20),unique=False)
    textbook=db.Column(db.String(20),primary_key=True)
    def __init__(self,mingcheng,semester,teacher,textbook):
        self.mingcheng = mingcheng
        self.semester = semester
        self.teacher  = teacher
        self.textbook  = textbook

db.create_all()
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
db.session.commit()
# print("11111111111")
# print(User.query.all())
# print(User.query.filter_by(username="李陈斌").first())
# print(User.query.filter_by(username="李陈").first())

# if User.query.filter_by(username="李陈斌"):
#     print("没有李陈斌")
# else:
#     print("有李陈斌")
# if User.query.filter_by(username="李陈"):
#     print("没有李陈")
# else:
#     print("有李陈")

