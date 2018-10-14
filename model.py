from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
# 启动
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/courses'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
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


# 定义表单类
# class Form_test(FlaskForm):
#     username = StringField('用户名：',validators=[DataRequired()])
#     password = PasswordField('密码：',validators=[DataRequired()])
#     radioButton = RadioField('method', choices=[(1,'学生'),(2,'教师')],default=1)

#     # input = SubmitField('提交')



def figure(s_number,s_semester):
    #计算某位同学的每一次成绩
    scores1 = Score_plus.query.filter_by(s_number=s_number,s_semester=s_semester).all()
    #计算平均成绩
    all_courses = ["语文",'数学','英语','物理','化学','生物','政治','历史','地理']
    scores_average = []
    for coursename in all_courses:
        student_scores = Score_plus.query.filter_by(coursename=coursename,s_semester=s_semester).all()
        sum,i = 0,0
        for student_score in student_scores:
            sum += student_score.score
            i+=1
        scores_average.append(sum/i)
    x,y1,y2=[],[],[]
    for score in scores1:
        x.append(score.coursename)
        y1.append(score.score)   
    for score in scores_average:
        y2.append(score) 
    plt.plot(x,y1)
    plt.plot(x,y2)
    plt.savefig('C:/Users/lcb/gitpro/flask_git/static/figure/new_plot.png')
    plt.show()
