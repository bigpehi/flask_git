from flask import Flask,render_template,request
# 启动
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('teacher2.html')

if __name__ == "__main__":
    app.run()