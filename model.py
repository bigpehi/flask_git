# 该文件中存储数据库模型、表单模型以及常用的函数等
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# 启动
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/courses'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
app.config['secret_key']='secret'
app.config['SESSION_TYPE'] = 'filesystem'
db = SQLAlchemy(app)

default_semester=3 # 默认学期

Score = db.Table("score",
    db.Column("s_number",db.String(9),db.ForeignKey('student.s_number')),
    db.Column("s_type",db.String(9),unique=False),
    db.Column("courseName",db.String(20),db.ForeignKey('course.textbook')),
    db.Column("score",db.Integer,unique=False)
)
class Student(db.Model):
    __tablename__='student'
    s_number=db.Column(db.String(9),primary_key=True)
    s_name=db.Column(db.String(20),unique=False)
    s_sex=db.Column(db.String(20),unique=False)
    s_age=db.Column(db.Integer,unique=False)
    s_semester=db.Column(db.Integer,unique=False)
    course = db.relationship(
        "Course",
        secondary = Score,
        backref = db.backref('student')
    )
    def __init__(self,s_name,s_number,s_sex,s_age,s_semester):
        self.s_number = s_number
        self.s_name = s_name
        self.s_sex  = s_sex
        self.s_age  = s_age
        self.s_semester  = s_semester

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
class Score_plus(db.Model):
    __tablename__='score_plus'
    id = db.Column(db.Integer,primary_key=True)
    s_number=db.Column(db.String(9),unique=False)
    s_name=db.Column(db.String(9),unique=False)
    s_semester=db.Column(db.Integer,unique=False)
    # s_type=db.Column(db.String(9),unique=False)
    coursename=db.Column(db.String(20),unique=False)
    score=db.Column(db.Integer)
    def __init__(self,s_number,s_name,s_semester,coursename,score):
        self.s_number=s_number
        self.s_name=s_name
        self.s_semester=s_semester
        self.coursename=coursename
        self.score=score

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),unique=False)
    password = db.Column(db.String(120),unique=False)
    radio = db.Column(db.String(20),unique=False)

    def __init__(self,username,password,radio):
        self.username = username
        self.password = password
        self.radio  = radio

#这个函数用来提供折线图的数据        
def figure(s_number): #参数：科目 学号————>学生该门课多学期总分分数折线图+全部学生总分平均成绩折线图
    s_scores=[] # y1 该学生所有学期的总分数
    for semester in range(1,7):
        s_scores_semester = Score_plus.query.filter_by(s_number=s_number,s_semester=semester).all() #某学期该学生的所有分数
        sum_semester = 0
        for score in s_scores_semester:
            sum_semester += score.score
        s_scores.append(sum_semester)

    average_scores=[] # y2
    for semester in range(1,7):
        scores = Score_plus.query.filter_by(s_semester=semester).all() #所有人某学期的所有成绩
        # 计算平均成绩
        sum,i=0,0
        for score in scores:
            sum+=score.score # 累计分数
            i+=1 # 累计人数
        average_scores.append(round(sum/(i//9),2))
    # 横坐标x
    # x = [1,2,3,4,5,6]

    return s_scores,average_scores
