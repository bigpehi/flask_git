# from flask import Flask,render_template,request
# # 导入wtf扩展的表单类
# from flask_wtf import FlaskForm
# # 导入自定义表单需要的字段
# from wtforms import SubmitField,StringField,PasswordField
# # 导入wtf扩展提供的表单验证器
# from wtforms.validators import DataRequired,EqualTo
# # 导入配置好的相关数据库信息
# from flask_sqlalchemy import SQLAlchemy

# # 启动
# app = Flask(__name__)
# # 设置秘钥
# app.config['SECRET_KEY'] = 'secret'


# # 定义表单类
# class Form_test(FlaskForm):
#     username = StringField('用户名：',validators=[DataRequired()])
#     password = PasswordField('密码：',validators=[DataRequired()])
#     input = SubmitField('提交')

# # 配置数据库并定义数据库表模型类
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/flask1'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
# db = SQLAlchemy(app)


# @app.route('/',methods=['GET','POST'])
# def login():
#     if request.method == "GET":
#         # 显示登录页面
#         form = Form_test()# 测试语句
#         print("now is get")
#         return render_template('login.html',form=form)
#     if request.method == "POST":
#         db.create_all()
#         print("now is post")# 测试语句
#         #从返回的request的值获取表单信息
#         username = request.form.get('username')
#         password = request.form.get('password')
        
#         admin = User(username,password)
#         db.session.add(admin)
#         db.session.commit()
#         return "成功添加一个信息"




# if __name__ == "__main__":
#     app.run()

from flask import Flask,render_template,request
# 导入wtf扩展的表单类
from flask_wtf import FlaskForm
# 导入自定义表单需要的字段
from wtforms import SubmitField,StringField,PasswordField
# 导入wtf扩展提供的表单验证器
from wtforms.validators import DataRequired,EqualTo
# 导入配置好的相关数据库信息
from flask_sqlalchemy import SQLAlchemy

# 启动
app = Flask(__name__)
# 设置秘钥
app.config['SECRET_KEY'] = 'secret'


# 定义表单类
class Form_test(FlaskForm):
    username = StringField('用户名：',validators=[DataRequired()])
    password = PasswordField('密码：',validators=[DataRequired()])
    # input = SubmitField('提交')

# 配置数据库并定义数据库表模型类
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/flask1'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
db = SQLAlchemy(app)
# 定义的类必须要继承db对象中的model类
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),unique=False)
    password = db.Column(db.String(120),unique=False)

    def __init__(self,username,password):
        self.username = username
        self.password = password

@app.route('/index')
def hello():
    return 'hello'
@app.route('/',methods=['GET','POST'])
def login():
    if request.method == "GET":
        # 显示登录页面
        form = Form_test()
        # 测试语句
        print("now is get")
        return render_template('login.html',form=form)
    if request.method == "POST":
        print("now is post")# 测试语句
        db.create_all()
        #从返回的request的值获取表单信息
        username = request.form.get('username')
        password = request.form.get('password')
        
        admin = User(username,password)
        db.session.add(admin)
        db.session.commit()
        return "成功添加一个信息"




if __name__ == "__main__":
    app.run()
