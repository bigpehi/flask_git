from flask import Flask
# 导入配置好的相关数据库信息
from flask_sqlalchemy import SQLAlchemy

# 启动
app = Flask(__name__)


# 配置数据库并定义数据库表模型类
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/courses'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
db = SQLAlchemy(app)
scores = db.Table("scores",
    db.Column("s_number",db.Integer,db.ForeignKey(Student.s_number)),
    db.Column("courseName",db.String(20),db.ForeignKey(Course.courseName))
)
class Student(db.Model):
    __tablename__='student'
    s_number=db.Column(db.String(9),primary_key=True)
    s_name=db.Column(db.String(20),unique=False)
    s_sex=db.Column(db.String(20),unique=False)
    s_type=db.Column(db.String(9))
    s_age=db.Column(db.Integer,unique=False)
    Course = db.relationship('Course',
                            secondary=scores,
                            backref=db.backref('Student',lazy='dynamic'),
                            lazy='dynamic')

class Course(db.Model):
    __tablename__='course'
    courseName=db.Column(db.String(20),primary_key=True)
    teacher=db.Column(db.String(20),unique=True)
    textbook=db.Column(db.String(20),unique=True)


db.create_all()

