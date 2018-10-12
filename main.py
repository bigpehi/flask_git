from flask import Flask,render_template,request,url_for,redirect
# 导入wtf扩展的表单类
from flask_wtf import FlaskForm
# 导入自定义表单需要的字段
from wtforms import SubmitField,StringField,PasswordField,RadioField
# 导入wtf扩展提供的表单验证器
from wtforms.validators import DataRequired,EqualTo
# 导入配置好的相关数据库信息
from flask_sqlalchemy import SQLAlchemy
# 导入定义好的模型
from model import Score,Course,Score_plus,Student,db,User

# 启动
app = Flask(__name__)
# 设置秘钥
app.config['SECRET_KEY'] = 'secret'
# 配置数据库并定义数据库表模型类
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/courses'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
db = SQLAlchemy(app)

@app.route('/',methods=['GET','POST'])
def login():
    #实例化表单类
    # form = Form_test()
    if request.method == "GET":

        # 测试语句
        print("now is get")
        # 显示登录页面
        return render_template('login1.html')
    if request.method == "POST":
        print("now is post")# 测试语句)
        #从返回的request的值获取表单信息
        user_dict = request.form.to_dict() # {'radio1':'','username':'','password':''}

        print(user_dict)
        username = user_dict['username']
        password = user_dict['password']
        radio = user_dict['radio']
        # radio = "学生"
        # if 'radio2' in user_dict:
        #     radio = "教师"

        #验证该用户是否在数据库中
        if User.query.filter_by(username=username).first():
            #验证密码是否正确
            if User.query.filter_by(username=username).first().password==password:#登陆成功
                # 验证身份是否有误
                if User.query.filter_by(username=username).first().radio==radio:#身份正确
                    # 根据身份返回对应的页面
                    if radio=="教师":                      
                        return  redirect(url_for('teacher',t_name=username))  
                        # return render_template('teacher_hello.html',t_name=username)
                    else:
                        return  redirect(url_for('student',s_name=username))
                        # return render_template('student_index.html',s_name=username)
                else:#身份错误
                    return "身份错误"#待改成flash
            else:#登陆成功
                return "用户名或密码错误"#待改成flash
        else:
            return "登录失败"

    #这里缺一个注册功能

@app.route('/student/<s_name>',methods=['GET','POST'])
def student(s_name):
    courses = Course.query.all()
    for course in courses:
        print(course.textbook)
    return render_template('student_index.html',s_name=s_name,courses=courses)

@app.route('/teacher/<t_name>',methods=['GET','POST'])
def teacher(t_name):
    # students = Student.query.all()
    # return render_template('teacher2.html',t_name=t_name,students=students)
    if request.method == "GET":
        students = Student.query.all()
        return render_template('teacher2.html',t_name=t_name,students=students)
    if request.method == "POST":
        mydict = request.form.to_dict()
        print(mydict)# 测试


        students = Student.query.all()
        return render_template('teacher2.html',t_name=t_name,students=students)


@app.route('/delete/<t_name>/<s_number>',methods=['GET','POST'])
def delete_stu(s_number,t_name):
    #先删除student表里的内容——score表里的相关内容会自动删除
    del_stu = Student.query.filter_by(s_number=s_number).first()
    db.session.delete(del_stu)
    db.session.commit()
    #再删除score_plus表里的内容
    del_scores = Score_plus.query.filter_by(s_number=s_number).all()
    for del_score in del_scores:
        db.session.delete(del_score)
        db.session.commit()
    return redirect(url_for('teacher',t_name=t_name))

@app.route('/show/<t_name>/<s_number>',methods=['GET','POST'])
def show_stu(s_number,t_name):
    #规定当前学期为第三学期 此后改参数可以通过函数参数传入
    student_scores = Score_plus.query.filter_by(s_number=s_number).filter_by(s_semester=3).all() # 获取该学生成绩信息
    print(student_scores)
    s_name = Student.query.filter_by(s_number=s_number).first().s_name # 获取该学生姓名

    #查询该门课最高分
    max_scores = []
    all_courses = ["语文",'数学','英语','物理','化学','生物','政治','历史','地理']
    for coursename in all_courses:
        max_scores.append( Score_plus.query.filter_by(coursename=coursename,s_semester=3).order_by('-score').first().score )
    
    #计算平均分
    scores_average = []
    for coursename in all_courses:
        student_scores = Score_plus.query.filter_by(coursename=coursename,s_semester=3).all()
        sum = 0
        i = 0
        for student_score in student_scores:
            sum += student_score.score
            i+=1
        scores_average.append(sum/i)

    return render_template('show_student.html',s_name=s_name,t_name=t_name,student_scores=student_scores,max_scores=max_scores,scores_average=scores_average)


@app.route('/alter/<s_number>',methods=['GET','POST'])
def alter_stu(s_number):
    # del_stu=Student.query.filter_by(s_number=s_number).first()
    # db.session.delete(del_stu)
    # db.session.commit() 
    pass

@app.route('/add_stu',methods=['GET','POST'])
def add_stu():
    # stu_dict = request.form.to_dict()
    # print(stu_dict)
    return 'ok'
    # s_name = request.form.

    # if request.method=="GET":
    #     return
    # if request.method=="POST":
    



if __name__ == "__main__":
    app.run()
