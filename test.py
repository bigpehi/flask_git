from flask import Flask,render_template,request
# 启动
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('student_index.html')

if __name__ == "__main__":
    app.run()