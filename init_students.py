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
# 创建学生类
class Student(db.Model):
    __tablename__='student'
    s_number=db.Column(db.String(9),primary_key=True)
    s_name=db.Column(db.String(20),unique=False)
    s_sex=db.Column(db.String(20),unique=False)
    s_age=db.Column(db.Integer,unique=False)
    s_semester=db.Column(db.Integer,unique=False)

    def __init__(self,s_name,s_number,s_sex,s_age,s_semester):
        self.s_number = s_number
        self.s_name = s_name
        self.s_sex  = s_sex
        self.s_age  = s_age
        self.s_semester  = s_semester

db.create_all()
# admin1 = Student('常雨','169094320',"男",18)
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

# db.session.add(admin1)
db.session.add_all([admin1,admin2,admin3,admin4,admin5,admin6,admin7,admin8,admin9,admin10,admin11,admin12,admin13,admin14,admin15,admin16,admin17,admin18,admin19,admin20,admin21,admin22,admin23,admin24,admin25,admin26,admin27,admin28,admin29,admin30])
db.session.commit()
# print("11111111111")
# print(User.query.all())
# print(User.query.filter_by(username="李陈斌").first().radio)
# print(User.query.filter_by(username="李陈").first())

# if User.query.filter_by(username="李陈斌"):
#     print("没有李陈斌")
# else:
#     print("有李陈斌")
# if User.query.filter_by(username="李陈"):
#     print("没有李陈")
# else:
#     print("有李陈")

