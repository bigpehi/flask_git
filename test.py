from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from model import Score,Course,Score_plus,Student,db
app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('add_student.html')

if __name__ == "__main__":
    app.run()

# max_score = Score_plus.query.filter_by(coursename="语文",s_semester=3).order_by('-score').first()
# print(max_score.s_name)

student_scores = Score_plus.query.filter_by(s_number="169094325").filter_by(s_semester=3).all()
# print(student_scores)
# for student_score in student_scores:
#     print(student_scores.query.filter_by(coursename="语文").first().s_semester)
# for i in range(0,9):
#     print(Score_plus.query.filter_by(s_number="169094325",s_semester=3).order_by('-score').filter_by(coursename=["语文",'数学','英语','物理','化学','生物','政治','历史','地理'].pop(i)).first().s_semester)

# student_scores = Score_plus.query.filter_by(coursename="语文").filter_by(s_semester=3).first()
# print(student_scores.s_name,student_scores.s_semester)
