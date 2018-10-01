from flask import Flask,render_template,request
# 导入wtf扩展的表单类
from flask_wtf import FlaskForm
# 导入自定义表单需要的字段
from wtforms import SubmitField,StringField,PasswordField,RadioField
# 导入wtf扩展提供的表单验证器
from wtforms.validators import DataRequired,EqualTo
# 导入配置好的相关数据库信息
from flask_sqlalchemy import SQLAlchemy

# 启动
app = Flask(__name__)
# 设置秘钥
app.config['SECRET_KEY'] = 'secret'
# 配置数据库并定义数据库表模型类
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/courses'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
db = SQLAlchemy(app)

# 定义表单类
class Form_test(FlaskForm):
    username = StringField('用户名：',validators=[DataRequired()])
    password = PasswordField('密码：',validators=[DataRequired()])
    radioButton = RadioField('method', choices=[(1,'学生'),(2,'教师')],default=1)

    # input = SubmitField('提交')


# 创建用户类 存储用户信息 用于登录
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

class Student(db.Model):
    __tablename__='student'
    number=db.Column(db.String(9),primary_key=True)
    name=db.Column(db.String(20),unique=False)
    sex=db.Column(db.String(20),unique=False)
    age=db.Column(db.Integer,unique=False)

class Course(db.Model):
    __tablename__='course'
    mingcheng=db.Column(db.String(20),primary_key=True)
    teacher=db.Column(db.String(20),unique=True)
    textbook=db.Column(db.String(20),unique=True)

class Score(db.Model):
    __tablename__='score'
    id=db.Column(db.String(9),db.ForeignKey('student.number'),primary_key=True)
    coursename=db.Column(db.String(20),db.ForeignKey('course.mingcheng'),primary_key=True)
    score=db.Column(db.Integer)
    # gzstudent=db.relationship('SStudent',backref='score')

@app.route('/',methods=['GET','POST'])
def login():
    #实例化表单类
    form = Form_test()
    if request.method == "GET":

        # 测试语句
        print("now is get")
        # 显示登录页面
        return render_template('login.html',form=form)
    if request.method == "POST":
        print("now is post")# 测试语句)
        #从返回的request的值获取表单信息
        username = form.username.data
        password = form.password.data
        radio = "学生"
        if form.radioButton.data == 2:
            radio = "教师"
        #验证该用户是否在数据库中
        if User.query.filter_by(username=username).first():
            return "登陆成功\n你好 "+username
        else:
            return "登录失败"

    #这里缺一个注册功能




if __name__ == "__main__":
    app.run()
