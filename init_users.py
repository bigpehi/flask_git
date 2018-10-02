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

# db.drop_all()
# db.create_all()
# admin0 = User('陆可','0001','教师')
# admin1 = User('常雨','169094320','学生')
# admin2 = User('代章福','169094321','学生')
# admin3 = User('高忠','169094322','学生')
# admin4 = User('李陈斌','169094325','学生')
# admin5 = User('李雪','169094328','学生')
# admin6 = User('刘兆柱','169094329','学生')
# admin7 = User('柳亚雄','169144114','学生')
# admin8 = User('牛良伟','169094330','学生')
# admin9 = User('潘剑兵','169094331','学生')
# admin10 = User('钱丹丹','169094333','学生')
# admin11 = User('沈福莉','169094334','学生')
# admin12 = User('时微尘','169094336','学生')
# admin13 = User('谈成龙','169094337','学生')
# admin14 = User('汪鹏','169094338','学生')
# admin15 = User('汪艳','169094339','学生')
# admin16 = User('王宇','169094340','学生')
# admin17 = User('吴甜甜','169094341','学生')
# admin18 = User('许淼','169094343','学生')
# admin19 = User('许玉柱','169094344','学生')
# admin20 = User('薛家升','169094345','学生')
# admin21 = User('杨洁','169094346','学生')
# admin22= User('叶甜甜','169094347','学生')
# admin23 = User('张傲','169094348','学生')
# admin24 = User('张程','169094349','学生')
# admin25 = User('张建','169094350','学生')
# admin26 = User('张结宝','169104612','学生')
# admin27 = User('张伟','169094351','学生')
# admin28 = User('周力','169094352','学生')
# admin29 = User('朱海发','169094353','学生')
# admin30 = User('朱泽明','169094354','学生')

# db.session.add_all([admin0,admin1,admin2,admin3,admin4,admin5,admin6,admin7,admin8,admin9,admin10,admin11,admin12,admin13,admin14,admin15,admin16,admin17,admin18,admin19,admin20,admin21,admin22,admin23,admin24,admin25,admin26,admin27,admin28,admin29,admin30])
# db.session.commit()
print("11111111111")
print(User.query.all())
print(User.query.filter_by(username="李陈斌").first().radio)
print(User.query.filter_by(username="李陈").first())

# if User.query.filter_by(username="李陈斌"):
#     print("没有李陈斌")
# else:
#     print("有李陈斌")
# if User.query.filter_by(username="李陈"):
#     print("没有李陈")
# else:
#     print("有李陈")

