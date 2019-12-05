# _*_ coding : UTF-8 _*_
# 开发人员："夏沫丶"
# 开发时间： 2019/12/5 22:54
# 文件名称： run.py.py
# 开发工具： PyCharm
from flask import Flask,render_template

app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")
@app.route('/')
def index():
    return render_template("index.html")

# if __name__=="__main__":
#     app.run(debug=Flask, port=80,host="0.0.0.0")