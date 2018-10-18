from flask import Flask,render_template,request,url_for,redirect,flash
# 导入wtf扩展的表单类
from flask_wtf import FlaskForm
# 导入自定义表单需要的字段
from wtforms import SubmitField,StringField,PasswordField,RadioField
# 导入wtf扩展提供的表单验证器
from wtforms.validators import DataRequired,EqualTo
# 导入配置好的相关数据库信息
from flask_sqlalchemy import SQLAlchemy
# 导入定义好的模型
from model import Score,Course,Score_plus,Student,User,default_semester,db,app

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
                        return  redirect(url_for('student',s_number=password,semester=default_semester))
                        # return render_template('student_index.html',s_name=username)
                else:#身份错误
                    return "身份错误"#待改成flash
            else:#登陆成功
                return "用户名或密码错误"#待改成flash
        else:
            return "登录失败"

    #这里缺一个注册功能

@app.route('/student/<s_number>/<semester>/',methods=['GET','POST'])
def student(s_number,semester):
    semester=int(semester)
    student_scores = Score_plus.query.filter_by(s_number=s_number).filter_by(s_semester=semester).all() # 获取该学生成绩信息

    s_name = Student.query.filter_by(s_number=s_number).first().s_name # 获取该学生姓名
    print(s_name)
    #查询该门课最高分
    max_scores = []
    all_courses = ["语文",'数学','英语','物理','化学','生物','政治','历史','地理']

    # print(semester)
    # student = Score_plus.query.filter_by(coursename="语文",s_semester=semester).order_by('-score').first().
    
    for coursename in all_courses:
        max_scores.append( Score_plus.query.filter_by(coursename=coursename,s_semester=semester).order_by('-score').first().score )
    
    #计算平均分
    scores_average = []
    for coursename in all_courses:
        student_scores = Score_plus.query.filter_by(coursename=coursename,s_semester=semester).all()
        sum = 0
        i = 0
        for student_score in student_scores:
            sum += student_score.score
            i+=1
        scores_average.append(sum/i)
    return render_template('student_index.html',s_name=s_name,s_number=s_number,student_scores=student_scores,max_scores=max_scores,scores_average=scores_average,semester=semester)

@app.route('/teacher/<t_name>/',methods=['GET','POST'])
def teacher(t_name):
    # students = Student.query.all()
    # return render_template('teacher_info.html',t_name=t_name,students=students)
    if request.method == "GET":
        students = Student.query.all()
        return render_template('teacher_info.html',t_name=t_name,students=students)
    if request.method == "POST":
        mydict = request.form.to_dict()
        print(mydict)# 测试


        students = Student.query.all()
        return render_template('teacher_info.html',t_name=t_name,students=students)


@app.route('/delete/<t_name>/<s_number>/',methods=['GET','POST'])
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

@app.route('/show/<t_name>/<s_number>/<semester>/',methods=['GET','POST'])
def show_stu(s_number,t_name,semester):
    semester=int(semester)
    student_scores = Score_plus.query.filter_by(s_number=s_number).filter_by(s_semester=semester).all() # 获取该学生成绩信息

    s_name = Student.query.filter_by(s_number=s_number).first().s_name # 获取该学生姓名
    print(s_name)
    #查询该门课最高分
    max_scores = []
    all_courses = ["语文",'数学','英语','物理','化学','生物','政治','历史','地理']

    # print(semester)
    # student = Score_plus.query.filter_by(coursename="语文",s_semester=semester).order_by('-score').first().
    
    for coursename in all_courses:
        max_scores.append( Score_plus.query.filter_by(coursename=coursename,s_semester=semester).order_by('-score').first().score )
    
    #计算平均分
    scores_average = []
    for coursename in all_courses:
        student_scores = Score_plus.query.filter_by(coursename=coursename,s_semester=semester).all()
        sum = 0
        i = 0
        for student_score in student_scores:
            sum += student_score.score
            i+=1
        scores_average.append(round(sum/i,2))

    return render_template('show_student.html',s_number=s_number,s_name=s_name,t_name=t_name,student_scores=student_scores,max_scores=max_scores,scores_average=scores_average)


@app.route('/alter_stu/<s_number>/',methods=['GET','POST'])
def alter_stu(s_number):
    alter_stu=Student.query.filter_by(s_number=s_number).first()
    return render_template("alter_student.html",alter_stu=alter_stu)

@app.route('/alter_stu_sql/<s_number>/',methods=['GET','POST'])
def alter_stu_sql(s_number):
    alter_stu=Student.query.filter_by(s_number=s_number).first()
    if alter_stu:
        try:
            student = request.form.to_dict()
            alter_stu.s_number = student['s_number']
            alter_stu.s_name = student['s_name']
            alter_stu.s_semester = student['semester']
            alter_stu.s_sex = student['radio']
            alter_stu.s_age = student['s_age']
            db.session.commit()
        except Exception as e:
            flash("修改错误")
            db.session.rollback()
    else:
        flash("找不到该学生信息")    
        # return redirect(url_for('alter_stu_sql',s_number=s_number))
    return redirect(url_for("alter_stu",s_number=s_number) )

@app.route('/add_stu/<t_name>/',methods=['POST'])
def add_stu(t_name):
    return render_template('add_student.html',t_name=t_name)
    
@app.route('/add_stu_sql/<t_name>/',methods=['POST'])
def add_stu_sql(t_name):
    print(request.form)
    student = request.form.to_dict()
    print(student)
    s_number = student['s_number']
    s_name = student['s_name']
    s_semester = student['s_semester']
    s_sex = student['radio']
    s_age = student['s_age']
    add_student = Student(s_name=s_name,s_number=s_number,s_sex=s_sex,s_age=s_age,s_semester=s_semester)
    db.session.add(add_student)
    db.session.commit()
    return redirect(url_for("teacher",t_name=t_name))

@app.route('/add_score/<t_name>',methods=["POST"])
def add_score(t_name):
    return render_template('add_score.html',t_name=t_name)

@app.route('/add_score_sql/<t_name>',methods=['POST'])
def add_score_sql(t_name):
    score1=request.form.to_dict()
    s_number=score1['s_number']
    s_name=score1['s_name']
    s_semester=score1['s_semester']
    coursename=score1['coursename']
    score=score1['score']
    add_score=Score_plus(s_number=s_number,s_name=s_name,s_semester=s_semester)
    db.session.add(add_score)
    db.session.commit()
    return redirect(url_for("teacher",t_name=t_name))

if __name__ == "__main__":
    app.run()
